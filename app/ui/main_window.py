from __future__ import annotations

import html
import json
import traceback
import webbrowser
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import QThread, Qt, Signal
from PySide6.QtGui import QAction, QBrush, QColor, QDesktopServices
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSpinBox,
    QSplitter,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextBrowser,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from app.config import APP_NAME, APP_TITLE, APP_VERSION, GITHUB_URL, REPORTS_DIR, SEVERITY_ORDER
from app.core.database import ScanDatabase
from app.core.scanner import WebsiteScanner
from app.core.settings import AppSettings
from app.core.statistics import (
    calculate_statistics,
    category_series,
    confidence_series,
    history_trend,
    severity_series,
)
from app.i18n import tr
from app.models import Finding, ScanResult
from app.reporting.exporters import export_csv, export_html, export_json, export_pdf, export_sarif
from app.ui.about_dialog import AboutDialog
from app.ui.charts import ChartCanvas
from app.ui.widgets import MetricCard


class ScanWorker(QThread):
    completed = Signal(object)
    failed = Signal(str)
    progress = Signal(int, str)
    log = Signal(str)

    def __init__(self, target: str, profile: str, settings: AppSettings) -> None:
        super().__init__()
        self.target = target
        self.profile = profile
        self.settings = settings

    def run(self) -> None:
        try:
            scanner = WebsiteScanner(
                self.settings,
                log_callback=self.log.emit,
                progress_callback=self.progress.emit,
            )
            self.completed.emit(scanner.scan(self.target, self.profile))
        except Exception as exc:
            self.log.emit(traceback.format_exc())
            self.failed.emit(str(exc))


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.settings = AppSettings.load()
        self.language = self.settings.language if self.settings.language in {"de", "en"} else "de"
        self.database = ScanDatabase()
        self.current_result: ScanResult | None = None
        self.worker: ScanWorker | None = None
        self.history_cache: list[dict[str, object]] = []

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")
        self.resize(1540, 970)
        self.setMinimumSize(1180, 760)

        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)
        layout.setContentsMargins(14, 14, 14, 8)
        layout.setSpacing(12)

        layout.addWidget(self._build_header())
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        layout.addWidget(self.tabs, 1)

        self.dashboard_tab = self._build_dashboard_tab()
        self.scan_tab = self._build_scan_tab()
        self.findings_tab = self._build_findings_tab()
        self.statistics_tab = self._build_statistics_tab()
        self.history_tab = self._build_history_tab()
        self.logs_tab = self._build_logs_tab()
        self.settings_tab = self._build_settings_tab()

        for widget in (
            self.dashboard_tab,
            self.scan_tab,
            self.findings_tab,
            self.statistics_tab,
            self.history_tab,
            self.logs_tab,
            self.settings_tab,
        ):
            self.tabs.addTab(widget, "")

        self._connect_signals()
        self.apply_language()
        self.refresh_history()
        self.clear_result_views()
        self.statusBar().showMessage(self.t("ready"))

    def t(self, key: str) -> str:
        return tr(self.language, key)

    def _build_header(self) -> QFrame:
        frame = QFrame()
        frame.setObjectName("Header")
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(20, 16, 20, 16)
        title_box = QVBoxLayout()
        self.app_title_label = QLabel(APP_NAME)
        self.app_title_label.setObjectName("AppTitle")
        self.app_subtitle_label = QLabel()
        self.app_subtitle_label.setObjectName("Subtitle")
        title_box.addWidget(self.app_title_label)
        title_box.addWidget(self.app_subtitle_label)
        layout.addLayout(title_box)
        layout.addStretch(1)

        self.language_combo = QComboBox()
        self.language_combo.addItem("Deutsch", "de")
        self.language_combo.addItem("English", "en")
        self.language_combo.setCurrentIndex(0 if self.language == "de" else 1)
        self.github_button = QPushButton()
        self.about_button = QPushButton()
        layout.addWidget(self.language_combo)
        layout.addWidget(self.github_button)
        layout.addWidget(self.about_button)
        return frame

    def _build_dashboard_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(5, 14, 5, 5)
        cards = QHBoxLayout()
        self.risk_card = MetricCard("")
        self.grade_card = MetricCard("")
        self.finding_card = MetricCard("")
        self.checks_card = MetricCard("")
        self.response_card = MetricCard("")
        self.duration_card = MetricCard("")
        for card in (
            self.risk_card,
            self.grade_card,
            self.finding_card,
            self.checks_card,
            self.response_card,
            self.duration_card,
        ):
            cards.addWidget(card, 1)
        layout.addLayout(cards)

        content = QSplitter(Qt.Orientation.Horizontal)
        left = QFrame()
        left.setObjectName("Panel")
        left_layout = QVBoxLayout(left)
        self.latest_title = QLabel()
        self.latest_title.setObjectName("SectionTitle")
        self.latest_summary = QTextBrowser()
        self.latest_summary.setOpenExternalLinks(True)
        left_layout.addWidget(self.latest_title)
        left_layout.addWidget(self.latest_summary, 1)

        charts = QWidget()
        chart_layout = QGridLayout(charts)
        chart_layout.setContentsMargins(0, 0, 0, 0)
        self.dashboard_severity_chart = ChartCanvas()
        self.dashboard_category_chart = ChartCanvas()
        chart_layout.addWidget(self.dashboard_severity_chart, 0, 0)
        chart_layout.addWidget(self.dashboard_category_chart, 1, 0)
        content.addWidget(left)
        content.addWidget(charts)
        content.setStretchFactor(0, 1)
        content.setStretchFactor(1, 2)
        layout.addWidget(content, 1)
        return tab

    def _build_scan_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(5, 14, 5, 5)

        control = QFrame()
        control.setObjectName("Panel")
        control_layout = QGridLayout(control)
        control_layout.setContentsMargins(18, 18, 18, 18)
        self.target_label = QLabel()
        self.target_input = QLineEdit("https://example.com")
        self.target_input.setClearButtonEnabled(True)
        self.profile_label = QLabel()
        self.profile_combo = QComboBox()
        self.profile_combo.addItems(["Quick", "Standard", "Extended"])
        self.profile_combo.setCurrentText("Standard")
        self.start_button = QPushButton()
        self.start_button.setObjectName("PrimaryButton")
        self.export_button = QPushButton()
        self.export_menu = QMenu(self)
        self.export_button.setMenu(self.export_menu)
        control_layout.addWidget(self.target_label, 0, 0)
        control_layout.addWidget(self.target_input, 0, 1, 1, 4)
        control_layout.addWidget(self.profile_label, 0, 5)
        control_layout.addWidget(self.profile_combo, 0, 6)
        control_layout.addWidget(self.start_button, 0, 7)
        control_layout.addWidget(self.export_button, 0, 8)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.activity_label = QLabel()
        self.activity_label.setObjectName("Muted")
        control_layout.addWidget(self.progress_bar, 1, 0, 1, 7)
        control_layout.addWidget(self.activity_label, 1, 7, 1, 2)
        control_layout.setColumnStretch(1, 1)
        layout.addWidget(control)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        modules = QGroupBox()
        modules_layout = QVBoxLayout(modules)
        self.module_labels: list[QLabel] = []
        for _ in range(8):
            label = QLabel()
            label.setWordWrap(True)
            label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            self.module_labels.append(label)
            modules_layout.addWidget(label)
        modules_layout.addStretch(1)

        self.technical_summary = QTextBrowser()
        splitter.addWidget(modules)
        splitter.addWidget(self.technical_summary)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        layout.addWidget(splitter, 1)
        return tab

    def _build_findings_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(5, 14, 5, 5)

        filters = QFrame()
        filters.setObjectName("Panel")
        filters_layout = QHBoxLayout(filters)
        self.filter_label = QLabel()
        self.search_input = QLineEdit()
        self.severity_filter = QComboBox()
        self.confidence_filter = QComboBox()
        filters_layout.addWidget(self.filter_label)
        filters_layout.addWidget(self.search_input, 1)
        filters_layout.addWidget(self.severity_filter)
        filters_layout.addWidget(self.confidence_filter)
        layout.addWidget(filters)

        splitter = QSplitter(Qt.Orientation.Vertical)
        self.findings_table = QTableWidget(0, 6)
        self.findings_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.findings_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.findings_table.setAlternatingRowColors(True)
        self.findings_table.setSortingEnabled(True)
        self.findings_table.verticalHeader().setVisible(False)
        self.findings_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.findings_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.findings_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.findings_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.findings_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        self.findings_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        self.finding_details = QTextBrowser()
        splitter.addWidget(self.findings_table)
        splitter.addWidget(self.finding_details)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)
        layout.addWidget(splitter, 1)
        return tab

    def _build_statistics_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(5, 14, 5, 5)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.statistics_table = QTableWidget(0, 2)
        self.statistics_table.verticalHeader().setVisible(False)
        self.statistics_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.statistics_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.statistics_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        charts_widget = QWidget()
        charts_layout = QGridLayout(charts_widget)
        self.severity_chart = ChartCanvas()
        self.category_chart = ChartCanvas()
        self.response_chart = ChartCanvas()
        self.history_chart = ChartCanvas()
        charts_layout.addWidget(self.severity_chart, 0, 0)
        charts_layout.addWidget(self.category_chart, 0, 1)
        charts_layout.addWidget(self.response_chart, 1, 0)
        charts_layout.addWidget(self.history_chart, 1, 1)
        splitter.addWidget(self.statistics_table)
        splitter.addWidget(charts_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 4)
        layout.addWidget(splitter, 1)
        return tab

    def _build_history_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(5, 14, 5, 5)
        buttons = QHBoxLayout()
        self.load_history_button = QPushButton()
        self.delete_history_button = QPushButton()
        self.clear_history_button = QPushButton()
        buttons.addWidget(self.load_history_button)
        buttons.addWidget(self.delete_history_button)
        buttons.addStretch(1)
        buttons.addWidget(self.clear_history_button)
        layout.addLayout(buttons)
        self.history_table = QTableWidget(0, 8)
        self.history_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.history_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.history_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.history_table.setAlternatingRowColors(True)
        self.history_table.verticalHeader().setVisible(False)
        self.history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        for column in range(1, 8):
            self.history_table.horizontalHeader().setSectionResizeMode(column, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.history_table, 1)
        return tab

    def _build_logs_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(5, 14, 5, 5)
        button_row = QHBoxLayout()
        self.clear_log_button = QPushButton()
        button_row.addStretch(1)
        button_row.addWidget(self.clear_log_button)
        layout.addLayout(button_row)
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        layout.addWidget(self.log_output, 1)
        return tab

    def _build_settings_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(5, 14, 5, 5)
        panel = QFrame()
        panel.setObjectName("Panel")
        form = QFormLayout(panel)
        form.setContentsMargins(24, 24, 24, 24)
        self.settings_language_combo = QComboBox()
        self.settings_language_combo.addItem("Deutsch", "de")
        self.settings_language_combo.addItem("English", "en")
        self.settings_language_combo.setCurrentIndex(0 if self.language == "de" else 1)
        self.timeout_spin = QSpinBox()
        self.timeout_spin.setRange(3, 120)
        self.timeout_spin.setValue(self.settings.timeout_seconds)
        self.sample_spin = QSpinBox()
        self.sample_spin.setRange(1, 10)
        self.sample_spin.setValue(self.settings.sample_count)
        self.verify_tls_checkbox = QCheckBox()
        self.verify_tls_checkbox.setChecked(self.settings.verify_tls)
        self.save_history_checkbox = QCheckBox()
        self.save_history_checkbox.setChecked(self.settings.save_history)
        self.observatory_checkbox = QCheckBox("MDN HTTP Observatory")
        self.observatory_checkbox.setChecked(self.settings.enable_observatory)
        self.pagespeed_checkbox = QCheckBox("Google PageSpeed Insights")
        self.pagespeed_checkbox.setChecked(self.settings.enable_pagespeed)
        self.pagespeed_key_input = QLineEdit(self.settings.pagespeed_api_key)
        self.pagespeed_key_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.settings_save_button = QPushButton()
        self.settings_save_button.setObjectName("PrimaryButton")
        self.settings_language_label = QLabel()
        self.timeout_label = QLabel()
        self.samples_label = QLabel()
        self.external_label = QLabel()
        self.pagespeed_key_label = QLabel()
        external_box = QWidget()
        external_layout = QHBoxLayout(external_box)
        external_layout.setContentsMargins(0, 0, 0, 0)
        external_layout.addWidget(self.observatory_checkbox)
        external_layout.addWidget(self.pagespeed_checkbox)
        external_layout.addStretch(1)
        form.addRow(self.settings_language_label, self.settings_language_combo)
        form.addRow(self.timeout_label, self.timeout_spin)
        form.addRow(self.samples_label, self.sample_spin)
        form.addRow("", self.verify_tls_checkbox)
        form.addRow("", self.save_history_checkbox)
        form.addRow(self.external_label, external_box)
        form.addRow(self.pagespeed_key_label, self.pagespeed_key_input)
        form.addRow("", self.settings_save_button)
        layout.addWidget(panel)
        layout.addStretch(1)
        return tab

    def _connect_signals(self) -> None:
        self.github_button.clicked.connect(lambda: webbrowser.open(GITHUB_URL))
        self.about_button.clicked.connect(lambda: AboutDialog(self).exec())
        self.language_combo.currentIndexChanged.connect(self.change_language_from_header)
        self.settings_language_combo.currentIndexChanged.connect(self.change_language_from_settings)
        self.start_button.clicked.connect(self.start_scan)
        self.search_input.textChanged.connect(self.apply_finding_filters)
        self.severity_filter.currentIndexChanged.connect(self.apply_finding_filters)
        self.confidence_filter.currentIndexChanged.connect(self.apply_finding_filters)
        self.findings_table.itemSelectionChanged.connect(self.show_selected_finding)
        self.load_history_button.clicked.connect(self.load_selected_history)
        self.delete_history_button.clicked.connect(self.delete_selected_history)
        self.clear_history_button.clicked.connect(self.clear_history)
        self.history_table.itemDoubleClicked.connect(lambda _item: self.load_selected_history())
        self.clear_log_button.clicked.connect(self.log_output.clear)
        self.settings_save_button.clicked.connect(self.save_settings)
        self.target_input.returnPressed.connect(self.start_scan)

    def apply_language(self) -> None:
        self.app_subtitle_label.setText(self.t("subtitle"))
        self.github_button.setText(self.t("github"))
        self.about_button.setText(self.t("about"))
        self.tabs.setTabText(0, self.t("dashboard"))
        self.tabs.setTabText(1, self.t("scan_center"))
        self.tabs.setTabText(2, self.t("findings"))
        self.tabs.setTabText(3, self.t("statistics"))
        self.tabs.setTabText(4, self.t("history"))
        self.tabs.setTabText(5, self.t("logs"))
        self.tabs.setTabText(6, self.t("settings"))

        self.risk_card.set_label(self.t("risk_score"))
        self.grade_card.set_label(self.t("grade"))
        self.finding_card.set_label(self.t("total_findings"))
        self.checks_card.set_label(self.t("checks"))
        self.response_card.set_label(self.t("response"))
        self.duration_card.set_label(self.t("duration"))
        self.latest_title.setText(self.t("latest_scan"))

        self.target_label.setText(self.t("target"))
        self.profile_label.setText(self.t("profile"))
        self.start_button.setText(self.t("start_scan"))
        self.export_button.setText(self.t("export"))
        self.activity_label.setText(self.t("ready"))
        module_keys = [
            "module_http",
            "module_cookies",
            "module_content",
            "module_dns",
            "module_tls",
            "module_cors",
            "module_resources",
            "module_stats",
        ]
        for label, key in zip(self.module_labels, module_keys):
            label.setText(f"✓  {self.t(key)}")
        parent_group = self.module_labels[0].parentWidget()
        if isinstance(parent_group, QGroupBox):
            parent_group.setTitle(self.t("modules"))

        self.filter_label.setText(self.t("filter"))
        self.search_input.setPlaceholderText(self.t("filter"))
        self._rebuild_filter_boxes()
        self.findings_table.setHorizontalHeaderLabels(
            [self.t("severity"), self.t("confidence"), self.t("category"), self.t("title"), self.t("source"), "CWE"]
        )
        self.finding_details.setHtml(f"<h3>{self.t('details')}</h3><p>{self.t('no_scan')}</p>")
        self.statistics_table.setHorizontalHeaderLabels([self.t("stat_metric"), self.t("stat_value")])
        self.history_table.setHorizontalHeaderLabels(
            [self.t("target"), self.t("profile"), self.t("completed"), self.t("risk_score"), self.t("grade"), self.t("total_findings"), self.t("duration"), "ID"]
        )
        self.load_history_button.setText(self.t("load"))
        self.delete_history_button.setText(self.t("delete"))
        self.clear_history_button.setText(self.t("clear_history"))
        self.clear_log_button.setText(self.t("clear_log"))
        self.settings_language_label.setText(self.t("language"))
        self.timeout_label.setText(self.t("timeout"))
        self.samples_label.setText(self.t("samples"))
        self.verify_tls_checkbox.setText(self.t("verify_tls"))
        self.save_history_checkbox.setText(self.t("save_history"))
        self.external_label.setText(self.t("external_services"))
        self.pagespeed_key_label.setText(self.t("pagespeed_key"))
        self.settings_save_button.setText(self.t("save_settings"))
        self._rebuild_export_menu()
        if self.current_result:
            self.render_result(self.current_result)
        else:
            self.clear_result_views()
        self.refresh_history()

    def _rebuild_filter_boxes(self) -> None:
        severity = self.severity_filter.currentData()
        confidence = self.confidence_filter.currentData()
        self.severity_filter.blockSignals(True)
        self.confidence_filter.blockSignals(True)
        self.severity_filter.clear()
        self.severity_filter.addItem(self.t("all"), "")
        for item in SEVERITY_ORDER:
            self.severity_filter.addItem(item, item)
        self.confidence_filter.clear()
        self.confidence_filter.addItem(self.t("all"), "")
        for item in ("High", "Medium", "Low"):
            self.confidence_filter.addItem(item, item)
        self.severity_filter.setCurrentIndex(max(0, self.severity_filter.findData(severity)))
        self.confidence_filter.setCurrentIndex(max(0, self.confidence_filter.findData(confidence)))
        self.severity_filter.blockSignals(False)
        self.confidence_filter.blockSignals(False)

    def _rebuild_export_menu(self) -> None:
        self.export_menu.clear()
        actions = [
            (self.t("export_json"), self.export_current_json),
            (self.t("export_html"), self.export_current_html),
            (self.t("export_csv"), self.export_current_csv),
            (self.t("export_sarif"), self.export_current_sarif),
            (self.t("export_pdf"), self.export_current_pdf),
        ]
        for label, callback in actions:
            action = QAction(label, self)
            action.triggered.connect(callback)
            self.export_menu.addAction(action)

    def change_language_from_header(self) -> None:
        language = str(self.language_combo.currentData())
        self.set_language(language, source="header")

    def change_language_from_settings(self) -> None:
        language = str(self.settings_language_combo.currentData())
        self.set_language(language, source="settings")

    def set_language(self, language: str, source: str = "") -> None:
        if language not in {"de", "en"}:
            return
        self.language = language
        self.settings.language = language
        header_index = self.language_combo.findData(language)
        settings_index = self.settings_language_combo.findData(language)
        self.language_combo.blockSignals(True)
        self.settings_language_combo.blockSignals(True)
        self.language_combo.setCurrentIndex(header_index)
        self.settings_language_combo.setCurrentIndex(settings_index)
        self.language_combo.blockSignals(False)
        self.settings_language_combo.blockSignals(False)
        self.apply_language()

    def start_scan(self) -> None:
        if self.worker and self.worker.isRunning():
            return
        target = self.target_input.text().strip()
        if not target:
            QMessageBox.warning(self, APP_NAME, self.t("invalid_url"))
            return
        profile = self.profile_combo.currentText()
        self._read_settings_from_controls()
        self.worker = ScanWorker(target, profile, self.settings)
        self.worker.progress.connect(self.update_progress)
        self.worker.log.connect(self.append_log)
        self.worker.completed.connect(self.scan_completed)
        self.worker.failed.connect(self.scan_failed)
        self.worker.finished.connect(self.scan_finished)
        self.start_button.setEnabled(False)
        self.export_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.activity_label.setText(self.t("running"))
        self.statusBar().showMessage(self.t("running"))
        self.append_log(f"--- {datetime.now().isoformat(timespec='seconds')} ---")
        self.worker.start()

    def update_progress(self, value: int, message: str) -> None:
        self.progress_bar.setValue(value)
        self.activity_label.setText(message)
        self.statusBar().showMessage(message)

    def append_log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_output.append(f"[{timestamp}] {message}")

    def scan_completed(self, result: object) -> None:
        if not isinstance(result, ScanResult):
            return
        self.current_result = result
        if self.settings.save_history:
            self.database.save(result)
        self.render_result(result)
        self.refresh_history()
        self.tabs.setCurrentWidget(self.dashboard_tab)
        self.activity_label.setText(self.t("completed"))
        self.statusBar().showMessage(self.t("completed"))

    def scan_failed(self, message: str) -> None:
        self.append_log(f"ERROR: {message}")
        QMessageBox.critical(self, APP_NAME, f"{self.t('scan_error')}\n\n{message}")
        self.activity_label.setText(self.t("scan_error"))
        self.statusBar().showMessage(self.t("scan_error"))

    def scan_finished(self) -> None:
        self.start_button.setEnabled(True)
        self.export_button.setEnabled(self.current_result is not None)
        self.worker = None

    def render_result(self, result: ScanResult) -> None:
        stats = calculate_statistics(result)
        self.risk_card.set_value(f"{result.risk_score:.1f}")
        self.grade_card.set_value(result.grade)
        self.finding_card.set_value(str(len(result.findings)))
        self.checks_card.set_value(str(result.metrics.checks_executed))
        self.response_card.set_value(f"{stats.mean_response_ms:.1f} ms")
        self.duration_card.set_value(f"{result.duration_seconds:.2f} s")
        risk_color = "#57c785" if result.risk_score < 25 else "#e4b64c" if result.risk_score < 70 else "#e26868"
        self.risk_card.set_accent(risk_color)
        self.grade_card.set_accent(risk_color)
        self.latest_summary.setHtml(self._result_summary_html(result))
        self.technical_summary.setHtml(self._technical_summary_html(result))
        self.populate_findings(result.findings)
        self.populate_statistics(result)
        self.update_charts(result)
        self.export_button.setEnabled(True)

    def _result_summary_html(self, result: ScanResult) -> str:
        counts = result.severity_counts
        return f"""
        <h2>{html.escape(result.target)}</h2>
        <p><b>{self.t('profile')}:</b> {html.escape(result.profile)}<br>
        <b>{self.t('completed')}:</b> {result.completed_at}<br>
        <b>HTTP:</b> {result.metrics.status_code} · <b>Final URL:</b> {html.escape(result.metrics.final_url)}<br>
        <b>{self.t('risk_score')}:</b> {result.risk_score:.1f} · <b>{self.t('grade')}:</b> {result.grade}</p>
        <h3>{self.t('severity_distribution')}</h3>
        <p>Critical: {counts['Critical']} · High: {counts['High']} · Medium: {counts['Medium']} · Low: {counts['Low']} · Info: {counts['Info']}</p>
        <h3>Technical overview</h3>
        <p>DNS: {result.metrics.dns_time_ms:.2f} ms · TLS: {result.metrics.tls_time_ms:.2f} ms · Initial response: {result.metrics.response_time_ms:.2f} ms<br>
        Response size: {result.metrics.response_size_bytes:,} bytes · Redirects: {result.metrics.redirect_count} · Checks: {result.metrics.checks_executed}</p>
        """

    def _technical_summary_html(self, result: ScanResult) -> str:
        metadata = result.metrics.metadata
        dns = metadata.get("dns_records", {})
        tls = metadata.get("tls", {})
        libraries = metadata.get("detected_libraries", {})
        page_scores = result.metrics.pagespeed_scores
        def fmt(value: object) -> str:
            if isinstance(value, (dict, list)):
                raw = json.dumps(value, indent=2, ensure_ascii=False)
            else:
                raw = str(value)
            return html.escape(raw)
        return f"""
        <h2>{APP_TITLE}</h2>
        <h3>Target</h3><pre>{html.escape(result.target)}\n{html.escape(result.metrics.final_url)}</pre>
        <h3>HTTP</h3><pre>Status: {result.metrics.status_code}\nVersion: {fmt(metadata.get('http_version', ''))}\nRedirects: {result.metrics.redirect_count}\nSize: {result.metrics.response_size_bytes} bytes</pre>
        <h3>Content</h3><pre>Title: {fmt(metadata.get('title', ''))}\nForms: {fmt(metadata.get('forms', 0))}\nScripts: {fmt(metadata.get('scripts', 0))}\nInline scripts: {fmt(metadata.get('inline_scripts', 0))}\nExternal domains: {fmt(metadata.get('external_domains', []))}\nLibraries: {fmt(libraries)}</pre>
        <h3>DNS</h3><pre>{fmt(dns)}</pre>
        <h3>TLS</h3><pre>{fmt(tls)}</pre>
        <h3>HTTP methods</h3><pre>{fmt(metadata.get('allowed_methods', []))}\nTRACE status: {fmt(metadata.get('trace_status', ''))}</pre>
        <h3>PageSpeed</h3><pre>{fmt(page_scores)}</pre>
        """

    def populate_findings(self, findings: list[Finding]) -> None:
        self.findings_table.setSortingEnabled(False)
        self.findings_table.setRowCount(len(findings))
        for row, finding in enumerate(findings):
            values = [
                finding.severity,
                finding.confidence,
                finding.category,
                finding.title,
                finding.source,
                finding.cwe,
            ]
            severity_colors = {
                "Critical": "#c2384f",
                "High": "#dc6b35",
                "Medium": "#d6a934",
                "Low": "#3989c6",
                "Info": "#7f91aa",
            }
            for column, value in enumerate(values):
                item = QTableWidgetItem(value)
                item.setData(Qt.ItemDataRole.UserRole, finding.to_dict())
                if column == 0:
                    item.setForeground(QBrush(QColor(severity_colors.get(finding.severity, "#dce6f5"))))
                self.findings_table.setItem(row, column, item)
        self.findings_table.setSortingEnabled(True)
        self.apply_finding_filters()
        if findings:
            self.findings_table.selectRow(0)
        else:
            self.finding_details.setHtml(f"<h3>{self.t('details')}</h3><p>{self.t('no_scan')}</p>")

    def apply_finding_filters(self) -> None:
        search = self.search_input.text().strip().lower()
        severity = str(self.severity_filter.currentData() or "")
        confidence = str(self.confidence_filter.currentData() or "")
        for row in range(self.findings_table.rowCount()):
            item = self.findings_table.item(row, 0)
            if not item:
                continue
            data = item.data(Qt.ItemDataRole.UserRole) or {}
            haystack = " ".join(str(value) for value in data.values()).lower()
            visible = (
                (not search or search in haystack)
                and (not severity or data.get("severity") == severity)
                and (not confidence or data.get("confidence") == confidence)
            )
            self.findings_table.setRowHidden(row, not visible)

    def show_selected_finding(self) -> None:
        selected = self.findings_table.selectedItems()
        if not selected:
            return
        row = selected[0].row()
        item = self.findings_table.item(row, 0)
        data = item.data(Qt.ItemDataRole.UserRole) if item else None
        if not data:
            return
        finding = Finding.from_dict(data)
        self.finding_details.setHtml(
            f"""
            <h2>{html.escape(finding.title)}</h2>
            <p><b>{self.t('severity')}:</b> {html.escape(finding.severity)} · <b>{self.t('confidence')}:</b> {html.escape(finding.confidence)} · <b>{self.t('category')}:</b> {html.escape(finding.category)}</p>
            <h3>{self.t('description')}</h3><p>{html.escape(finding.description)}</p>
            <h3>{self.t('evidence')}</h3><pre>{html.escape(finding.evidence)}</pre>
            <h3>{self.t('remediation')}</h3><p>{html.escape(finding.remediation)}</p>
            <h3>{self.t('reference')}</h3><p>{html.escape(finding.cwe or '—')} {html.escape(finding.reference)}</p>
            <p><b>URL:</b> {html.escape(finding.url)}<br><b>{self.t('source')}:</b> {html.escape(finding.source)}<br><b>Timestamp:</b> {html.escape(finding.created_at)}</p>
            """
        )

    def populate_statistics(self, result: ScanResult) -> None:
        stats = calculate_statistics(result)
        rows = [
            (self.t("total_findings"), stats.finding_count),
            (self.t("mean_weight"), stats.mean_weight),
            (self.t("median_weight"), stats.median_weight),
            (self.t("std_dev"), stats.standard_deviation),
            (self.t("percentile_75"), stats.percentile_75),
            (self.t("percentile_95"), stats.percentile_95),
            (self.t("skewness"), stats.skewness),
            (self.t("entropy"), stats.entropy),
            (self.t("mean_response"), f"{stats.mean_response_ms} ms"),
            (self.t("median_response"), f"{stats.median_response_ms} ms"),
            (self.t("response_std"), f"{stats.response_standard_deviation} ms"),
            (self.t("trend_slope"), stats.trend_slope),
            (self.t("outliers"), stats.outlier_count),
        ]
        self.statistics_table.setRowCount(len(rows))
        for row, (name, value) in enumerate(rows):
            self.statistics_table.setItem(row, 0, QTableWidgetItem(str(name)))
            self.statistics_table.setItem(row, 1, QTableWidgetItem(str(value)))

    def update_charts(self, result: ScanResult) -> None:
        severity_labels, severity_values = severity_series(result)
        category_labels, category_values = category_series(result)
        sample_labels = [str(index) for index in range(1, len(result.metrics.response_samples_ms) + 1)]
        self.dashboard_severity_chart.draw_pie(severity_labels, severity_values, self.t("severity_distribution"))
        self.dashboard_category_chart.draw_bar(category_labels[:12], category_values[:12], self.t("category_distribution"))
        self.severity_chart.draw_pie(severity_labels, severity_values, self.t("severity_distribution"))
        self.category_chart.draw_bar(category_labels[:15], category_values[:15], self.t("category_distribution"))
        self.response_chart.draw_line(sample_labels, result.metrics.response_samples_ms, self.t("response_samples"), "ms")
        history_results: list[ScanResult] = []
        for summary in reversed(self.history_cache[:30]):
            scan_id = str(summary.get("scan_id", ""))
            loaded = self.database.load(scan_id)
            if loaded and loaded.target == result.target:
                history_results.append(loaded)
        labels, values = history_trend(history_results)
        self.history_chart.draw_line(labels, values, self.t("history_trend"), "Score")

    def clear_result_views(self) -> None:
        for card in (
            self.risk_card,
            self.grade_card,
            self.finding_card,
            self.checks_card,
            self.response_card,
            self.duration_card,
        ):
            card.set_value("—")
        self.latest_summary.setHtml(f"<h2>{self.t('latest_scan')}</h2><p>{self.t('no_scan')}</p>")
        self.technical_summary.setHtml(f"<h2>{APP_TITLE}</h2><p>{self.t('no_scan')}</p>")
        self.findings_table.setRowCount(0)
        self.statistics_table.setRowCount(0)
        self.dashboard_severity_chart.empty(self.t("no_scan"))
        self.dashboard_category_chart.empty(self.t("no_scan"))
        self.severity_chart.empty(self.t("no_scan"))
        self.category_chart.empty(self.t("no_scan"))
        self.response_chart.empty(self.t("no_scan"))
        self.history_chart.empty(self.t("no_scan"))
        self.export_button.setEnabled(False)

    def refresh_history(self) -> None:
        self.history_cache = self.database.list_summaries()
        self.history_table.setRowCount(len(self.history_cache))
        for row, summary in enumerate(self.history_cache):
            values = [
                summary.get("target", ""),
                summary.get("profile", ""),
                summary.get("completed_at", ""),
                summary.get("risk_score", ""),
                summary.get("grade", ""),
                summary.get("finding_count", ""),
                f"{float(summary.get('duration_seconds', 0.0)):.2f}s",
                summary.get("scan_id", ""),
            ]
            for column, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setData(Qt.ItemDataRole.UserRole, str(summary.get("scan_id", "")))
                self.history_table.setItem(row, column, item)

    def selected_history_id(self) -> str:
        selected = self.history_table.selectedItems()
        if not selected:
            return ""
        return str(selected[0].data(Qt.ItemDataRole.UserRole) or "")

    def load_selected_history(self) -> None:
        scan_id = self.selected_history_id()
        if not scan_id:
            return
        result = self.database.load(scan_id)
        if not result:
            return
        self.current_result = result
        self.target_input.setText(result.target)
        self.profile_combo.setCurrentText(result.profile)
        self.render_result(result)
        self.tabs.setCurrentWidget(self.dashboard_tab)
        self.statusBar().showMessage(self.t("history_loaded"))

    def delete_selected_history(self) -> None:
        scan_id = self.selected_history_id()
        if not scan_id:
            return
        answer = QMessageBox.question(self, APP_NAME, self.t("confirm_delete"))
        if answer == QMessageBox.StandardButton.Yes:
            self.database.delete(scan_id)
            self.refresh_history()

    def clear_history(self) -> None:
        answer = QMessageBox.question(self, APP_NAME, self.t("confirm_clear"))
        if answer == QMessageBox.StandardButton.Yes:
            self.database.clear()
            self.refresh_history()
            if self.current_result:
                self.update_charts(self.current_result)

    def _read_settings_from_controls(self) -> None:
        self.settings.language = self.language
        self.settings.timeout_seconds = self.timeout_spin.value()
        self.settings.sample_count = self.sample_spin.value()
        self.settings.verify_tls = self.verify_tls_checkbox.isChecked()
        self.settings.save_history = self.save_history_checkbox.isChecked()
        self.settings.enable_observatory = self.observatory_checkbox.isChecked()
        self.settings.enable_pagespeed = self.pagespeed_checkbox.isChecked()
        self.settings.pagespeed_api_key = self.pagespeed_key_input.text().strip()

    def save_settings(self) -> None:
        self._read_settings_from_controls()
        self.settings.save()
        self.statusBar().showMessage(self.t("settings_saved"))
        QMessageBox.information(self, APP_NAME, self.t("settings_saved"))

    def _ensure_result(self) -> ScanResult | None:
        if not self.current_result:
            QMessageBox.warning(self, APP_NAME, self.t("nothing_export"))
            return None
        return self.current_result

    def _select_export_path(self, suffix: str, label: str) -> Path | None:
        result = self._ensure_result()
        if not result:
            return None
        host = QUrl(result.target).host() or "website"
        default_name = REPORTS_DIR / f"{host}_{result.completed_at[:10]}_{result.scan_id[:8]}.{suffix}"
        path, _ = QFileDialog.getSaveFileName(self, label, str(default_name), f"*.{suffix}")
        return Path(path) if path else None

    def export_current_json(self) -> None:
        self._export_with(export_json, "json", self.t("export_json"))

    def export_current_html(self) -> None:
        self._export_with(export_html, "html", self.t("export_html"))

    def export_current_csv(self) -> None:
        self._export_with(export_csv, "csv", self.t("export_csv"))

    def export_current_sarif(self) -> None:
        self._export_with(export_sarif, "sarif", self.t("export_sarif"))

    def export_current_pdf(self) -> None:
        self._export_with(export_pdf, "pdf", self.t("export_pdf"))

    def _export_with(self, exporter, suffix: str, label: str) -> None:
        result = self._ensure_result()
        if not result:
            return
        path = self._select_export_path(suffix, label)
        if not path:
            return
        try:
            exporter(result, path)
            self.statusBar().showMessage(str(path))
            answer = QMessageBox.question(self, APP_NAME, f"Report created:\n{path}\n\nOpen file?")
            if answer == QMessageBox.StandardButton.Yes:
                QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))
        except Exception as exc:
            QMessageBox.critical(self, APP_NAME, str(exc))

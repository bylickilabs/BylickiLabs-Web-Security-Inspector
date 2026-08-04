from __future__ import annotations


def application_stylesheet() -> str:
    return """
    QWidget { background: #0b1220; color: #e8eef8; font-family: 'Segoe UI'; font-size: 10pt; }
    QMainWindow { background: #0b1220; }
    QFrame#Header, QFrame#Panel, QGroupBox, QTabWidget::pane { background: #111a2c; border: 1px solid #26344f; border-radius: 10px; }
    QFrame#MetricCard { background: #111a2c; border: 1px solid #26344f; border-radius: 12px; }
    QLabel#AppTitle { font-size: 20pt; font-weight: 700; color: #f5f8ff; }
    QLabel#Subtitle, QLabel#Muted { color: #9baac2; }
    QLabel#MetricValue { font-size: 23pt; font-weight: 700; color: #f5f8ff; }
    QLabel#MetricLabel { color: #9baac2; font-weight: 600; }
    QLabel#SectionTitle { font-size: 13pt; font-weight: 700; color: #f5f8ff; }
    QPushButton { background: #1b2a45; border: 1px solid #324669; border-radius: 7px; padding: 8px 14px; font-weight: 600; }
    QPushButton:hover { background: #243858; border-color: #4da3ff; }
    QPushButton:pressed { background: #15243d; }
    QPushButton#PrimaryButton { background: #1769aa; border-color: #4da3ff; color: white; padding: 10px 18px; }
    QPushButton#PrimaryButton:hover { background: #1d79c5; }
    QPushButton:disabled { color: #69778e; background: #121b2b; border-color: #253149; }
    QLineEdit, QComboBox, QSpinBox, QTextEdit, QTextBrowser { background: #0d1627; border: 1px solid #2a3a58; border-radius: 7px; padding: 7px; selection-background-color: #1769aa; }
    QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border-color: #4da3ff; }
    QTabBar::tab { background: #111a2c; color: #9baac2; border: 1px solid #26344f; padding: 10px 18px; margin-right: 2px; border-top-left-radius: 7px; border-top-right-radius: 7px; }
    QTabBar::tab:selected { color: white; background: #1a2943; border-bottom-color: #1a2943; }
    QTabBar::tab:hover { color: white; }
    QTableWidget, QTableView { background: #0d1627; alternate-background-color: #101c30; border: 1px solid #26344f; border-radius: 8px; gridline-color: #26344f; }
    QHeaderView::section { background: #182641; color: #dce6f5; padding: 8px; border: 0; border-right: 1px solid #26344f; font-weight: 700; }
    QTableWidget::item:selected { background: #194f7d; }
    QProgressBar { background: #0d1627; border: 1px solid #26344f; border-radius: 6px; text-align: center; height: 19px; }
    QProgressBar::chunk { background: #2479bd; border-radius: 5px; }
    QGroupBox { margin-top: 12px; padding: 12px; font-weight: 700; }
    QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 5px; color: #dce6f5; }
    QCheckBox { spacing: 8px; }
    QCheckBox::indicator { width: 17px; height: 17px; }
    QStatusBar { background: #0d1627; color: #9baac2; border-top: 1px solid #26344f; }
    QMenu { background: #111a2c; border: 1px solid #26344f; }
    QMenu::item { padding: 7px 25px; }
    QMenu::item:selected { background: #194f7d; }
    """

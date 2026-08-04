from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QTabWidget, QTextBrowser, QVBoxLayout, QWidget

from app.config import (
    APP_AUTHOR,
    APP_COPYRIGHT,
    APP_DESCRIPTION,
    APP_LICENSE,
    APP_NAME,
    APP_TITLE,
    APP_VERSION,
)


class AboutDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"{APP_NAME} · About")
        self.resize(760, 600)
        layout = QVBoxLayout(self)
        heading = QLabel(APP_NAME)
        heading.setObjectName("AppTitle")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle = QLabel(APP_TITLE)
        subtitle.setObjectName("Subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(heading)
        layout.addWidget(subtitle)

        tabs = QTabWidget()
        overview = QTextBrowser()
        overview.setHtml(
            f"""
            <h2>Application overview</h2>
            <p>{APP_DESCRIPTION}</p>
            <p>The application combines structured website configuration assessments, local persistence,
            risk scoring, report generation and statistical analysis. NumPy is used for vectorised metric
            processing and percentile calculations. SciPy provides distribution, entropy, regression,
            skewness and outlier analysis. Matplotlib renders the integrated analytical charts.</p>
            <h3>Core areas</h3>
            <ul>
              <li>HTTP headers, Content Security Policy and redirect analysis</li>
              <li>Cookie, CORS, form and content configuration review</li>
              <li>TLS certificate, protocol and cipher inspection</li>
              <li>DNS, SPF, DMARC, CAA and mail security records</li>
              <li>Public resource, deployment artefact and HTTP method checks</li>
              <li>Response time sampling, risk metrics and scan history trends</li>
              <li>JSON, HTML, CSV, PDF and SARIF reporting</li>
            </ul>
            """
        )
        metadata = QTextBrowser()
        metadata.setPlainText(
            f"APP_NAME: {APP_NAME}\n"
            f"APP_TITLE: {APP_TITLE}\n"
            f"APP_VERSION: {APP_VERSION}\n"
            f"APP_AUTHOR: {APP_AUTHOR}\n"
            f"APP_DESCRIPTION: {APP_DESCRIPTION}\n"
            f"APP_LICENSE: {APP_LICENSE}\n"
            f"APP_COPYRIGHT: {APP_COPYRIGHT}\n"
        )
        components = QTextBrowser()
        components.setHtml(
            """
            <h2>Technical components</h2>
            <ul>
              <li>Python 3.11 or newer</li>
              <li>PySide6 for the desktop interface</li>
              <li>NumPy for numerical processing</li>
              <li>SciPy for statistical methods</li>
              <li>Matplotlib for charts</li>
              <li>Requests and Beautiful Soup for HTTP and HTML analysis</li>
              <li>dnspython for DNS records</li>
              <li>SQLite for scan history</li>
              <li>ReportLab for PDF reports</li>
            </ul>
            """
        )
        tabs.addTab(overview, "Overview")
        tabs.addTab(metadata, "Metadata")
        tabs.addTab(components, "Components")
        layout.addWidget(tabs, 1)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)

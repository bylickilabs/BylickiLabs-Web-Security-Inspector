import json

from app.reporting.exporters import export_csv, export_html, export_json, export_pdf, export_sarif
from tests.test_models import make_result


def test_all_report_formats(tmp_path) -> None:
    result = make_result()
    targets = {
        "json": tmp_path / "report.json",
        "html": tmp_path / "report.html",
        "csv": tmp_path / "report.csv",
        "sarif": tmp_path / "report.sarif",
        "pdf": tmp_path / "report.pdf",
    }
    export_json(result, targets["json"])
    export_html(result, targets["html"])
    export_csv(result, targets["csv"])
    export_sarif(result, targets["sarif"])
    export_pdf(result, targets["pdf"])
    assert all(path.exists() and path.stat().st_size > 0 for path in targets.values())
    assert json.loads(targets["json"].read_text())["target"] == result.target
    assert json.loads(targets["sarif"].read_text())["version"] == "2.1.0"

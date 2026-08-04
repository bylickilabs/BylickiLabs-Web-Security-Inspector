from __future__ import annotations

import csv
import html
import json
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from app.config import APP_AUTHOR, APP_NAME, APP_VERSION
from app.core.statistics import calculate_statistics
from app.models import ScanResult


def export_json(result: ScanResult, destination: Path) -> None:
    destination.write_text(
        json.dumps(result.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8"
    )


def export_csv(result: ScanResult, destination: Path) -> None:
    fields = [
        "severity",
        "confidence",
        "category",
        "title",
        "description",
        "evidence",
        "remediation",
        "url",
        "source",
        "cwe",
        "reference",
        "created_at",
    ]
    with destination.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for finding in result.findings:
            writer.writerow(finding.to_dict())


def export_sarif(result: ScanResult, destination: Path) -> None:
    level_map = {
        "Critical": "error",
        "High": "error",
        "Medium": "warning",
        "Low": "note",
        "Info": "none",
    }
    rules: dict[str, dict[str, Any]] = {}
    results: list[dict[str, Any]] = []
    for index, item in enumerate(result.findings, start=1):
        rule_id = item.cwe or f"BWSI-{index:04d}"
        rules.setdefault(
            rule_id,
            {
                "id": rule_id,
                "name": item.title,
                "shortDescription": {"text": item.description},
                "help": {"text": item.remediation},
            },
        )
        results.append(
            {
                "ruleId": rule_id,
                "level": level_map.get(item.severity, "note"),
                "message": {"text": f"{item.title}: {item.description}"},
                "locations": [
                    {
                        "physicalLocation": {
                            "artifactLocation": {"uri": item.url},
                        }
                    }
                ],
                "properties": {
                    "severity": item.severity,
                    "confidence": item.confidence,
                    "category": item.category,
                    "evidence": item.evidence,
                    "remediation": item.remediation,
                    "source": item.source,
                },
            }
        )
    payload = {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [
            {
                "tool": {
                    "driver": {
                        "name": APP_NAME,
                        "version": APP_VERSION,
                        "informationUri": "https://github.com/bylickilabs",
                        "rules": list(rules.values()),
                    }
                },
                "results": results,
            }
        ],
    }
    destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def export_html(result: ScanResult, destination: Path) -> None:
    stats = calculate_statistics(result)
    counts = result.severity_counts
    rows = []
    for item in result.findings:
        rows.append(
            "<tr>"
            f"<td><span class='badge {html.escape(item.severity.lower())}'>{html.escape(item.severity)}</span></td>"
            f"<td>{html.escape(item.confidence)}</td>"
            f"<td>{html.escape(item.category)}</td>"
            f"<td><strong>{html.escape(item.title)}</strong><br><small>{html.escape(item.description)}</small></td>"
            f"<td><pre>{html.escape(item.evidence)}</pre></td>"
            f"<td>{html.escape(item.remediation)}</td>"
            f"<td>{html.escape(item.source)}</td>"
            "</tr>"
        )
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>{html.escape(APP_NAME)} Report</title>
<style>
:root{{--bg:#0b1220;--panel:#111a2c;--line:#26344f;--text:#e8eef8;--muted:#9baac2;--accent:#4da3ff}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--text);font-family:Segoe UI,Arial,sans-serif}}
main{{max-width:1500px;margin:auto;padding:32px}} .hero,.card{{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:24px;margin-bottom:18px}}
h1{{margin:0 0 8px}} .muted{{color:var(--muted)}} .metrics{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}}
.metric{{background:#0e1728;border:1px solid var(--line);border-radius:10px;padding:16px}} .metric b{{display:block;font-size:28px;margin-top:4px}}
table{{width:100%;border-collapse:collapse;font-size:13px}} th,td{{border-bottom:1px solid var(--line);padding:10px;text-align:left;vertical-align:top}} th{{position:sticky;top:0;background:#16223a}}
pre{{white-space:pre-wrap;word-break:break-word;max-width:420px}} .badge{{padding:4px 8px;border-radius:12px;font-weight:600}} .critical{{background:#6b1024}} .high{{background:#7a2f19}} .medium{{background:#765c12}} .low{{background:#174c6b}} .info{{background:#27425e}}
</style></head><body><main>
<section class="hero"><h1>{html.escape(APP_NAME)}</h1><div class="muted">Version {APP_VERSION} · {html.escape(APP_AUTHOR)}</div><h2>Assessment Report</h2><p>{html.escape(result.target)}</p></section>
<section class="card metrics">
<div class="metric">Risk score<b>{result.risk_score:.1f}</b></div><div class="metric">Grade<b>{result.grade}</b></div><div class="metric">Findings<b>{len(result.findings)}</b></div><div class="metric">Checks<b>{result.metrics.checks_executed}</b></div><div class="metric">Duration<b>{result.duration_seconds:.2f}s</b></div><div class="metric">Response<b>{stats.mean_response_ms:.1f}ms</b></div>
</section>
<section class="card"><h2>Severity distribution</h2><p>Critical: {counts['Critical']} · High: {counts['High']} · Medium: {counts['Medium']} · Low: {counts['Low']} · Info: {counts['Info']}</p>
<p>Mean weight: {stats.mean_weight} · Standard deviation: {stats.standard_deviation} · Entropy: {stats.entropy} · 95th percentile: {stats.percentile_95}</p></section>
<section class="card"><h2>Findings</h2><div style="overflow:auto"><table><thead><tr><th>Severity</th><th>Confidence</th><th>Category</th><th>Finding</th><th>Evidence</th><th>Remediation</th><th>Source</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div></section>
</main></body></html>"""
    destination.write_text(page, encoding="utf-8")


def export_pdf(result: ScanResult, destination: Path) -> None:
    styles = getSampleStyleSheet()
    document = SimpleDocTemplate(
        str(destination),
        pagesize=landscape(A4),
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title=f"{APP_NAME} Report",
        author=APP_AUTHOR,
    )
    story: list[Any] = [
        Paragraph(APP_NAME, styles["Title"]),
        Paragraph(f"Version {APP_VERSION} · {APP_AUTHOR}", styles["Normal"]),
        Spacer(1, 5 * mm),
        Paragraph(f"Target: {html.escape(result.target)}", styles["Heading2"]),
        Paragraph(
            f"Profile: {result.profile} · Risk score: {result.risk_score:.1f} · Grade: {result.grade} · Findings: {len(result.findings)}",
            styles["Normal"],
        ),
        Paragraph(
            f"Started: {result.started_at} · Completed: {result.completed_at} · Duration: {result.duration_seconds:.2f}s",
            styles["Normal"],
        ),
        Spacer(1, 6 * mm),
    ]
    summary = [["Severity", "Count"]] + [[name, count] for name, count in result.severity_counts.items()]
    summary_table = Table(summary, colWidths=[45 * mm, 25 * mm])
    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#20334f")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.extend([summary_table, PageBreak(), Paragraph("Findings", styles["Heading1"])])
    rows: list[list[Any]] = [["Severity", "Category", "Title", "Evidence", "Remediation"]]
    for item in result.findings:
        rows.append(
            [
                item.severity,
                item.category,
                Paragraph(html.escape(item.title), styles["BodyText"]),
                Paragraph(html.escape(item.evidence).replace("\n", "<br/>"), styles["BodyText"]),
                Paragraph(html.escape(item.remediation), styles["BodyText"]),
            ]
        )
    table = Table(rows, repeatRows=1, colWidths=[18 * mm, 35 * mm, 55 * mm, 75 * mm, 75 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#20334f")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.2, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTSIZE", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(table)
    document.build(story)

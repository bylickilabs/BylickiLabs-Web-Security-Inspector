from app.scanners.content import scan_content
from app.scanners.cookies import scan_cookies
from app.scanners.cors import scan_cors
from app.scanners.forms import scan_forms
from app.scanners.http_headers import scan_headers


def test_header_findings() -> None:
    findings = scan_headers("https://example.com", {"Server": "Demo/1.0"}, True)
    titles = {item.title for item in findings}
    assert "Missing content-security-policy" in titles
    assert "Server information disclosed" in titles


def test_cookie_findings() -> None:
    findings = scan_cookies("https://example.com", ["session=abc; Path=/"])
    assert len(findings) == 3


def test_cors_reflection() -> None:
    findings = scan_cors(
        "https://example.com",
        {
            "Access-Control-Allow-Origin": "https://security-check.invalid",
            "Access-Control-Allow-Credentials": "true",
        },
        "https://security-check.invalid",
    )
    assert any(item.severity == "High" for item in findings)


def test_content_and_forms() -> None:
    html = """
    <html><head><meta name="generator" content="DemoCMS 1.0"></head>
    <body><!-- TODO internal secret --><img src="http://cdn.example.net/a.png">
    <form method="GET" action="http://example.com/login"><input type="password"></form>
    </body></html>
    """
    content_findings, metadata = scan_content("https://example.com", html)
    form_findings = scan_forms("https://example.com", html)
    assert metadata["forms"] == 1
    assert any(item.title == "Mixed content resources detected" for item in content_findings)
    assert any("Password form" in item.title for item in form_findings)

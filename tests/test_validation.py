import pytest

from app.core.validation import normalize_url


def test_normalize_url_adds_https() -> None:
    assert normalize_url("example.com") == "https://example.com/"


def test_normalize_url_rejects_invalid_scheme() -> None:
    with pytest.raises(ValueError):
        normalize_url("ftp://example.com")

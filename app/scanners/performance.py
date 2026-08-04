from __future__ import annotations

import time

import requests

from app.config import USER_AGENT


def collect_response_samples(
    url: str,
    session: requests.Session,
    timeout: int,
    verify_tls: bool,
    sample_count: int,
) -> list[float]:
    samples: list[float] = []
    for _ in range(max(1, min(sample_count, 10))):
        start = time.perf_counter()
        try:
            response = session.head(
                url,
                headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"},
                timeout=timeout,
                verify=verify_tls,
                allow_redirects=True,
            )
            if response.status_code in {405, 501}:
                response = session.get(
                    url,
                    headers={"User-Agent": USER_AGENT, "Range": "bytes=0-1024", "Cache-Control": "no-cache"},
                    timeout=timeout,
                    verify=verify_tls,
                    allow_redirects=True,
                    stream=True,
                )
            response.close()
            samples.append(round((time.perf_counter() - start) * 1000, 3))
        except requests.RequestException:
            continue
    return samples

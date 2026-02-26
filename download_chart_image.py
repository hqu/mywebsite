from urllib.request import Request, urlopen


def main() -> None:
    urls = [
        "https://datawrapper.dwcdn.net/wOV53/1/full.png",
        "https://datawrapper.dwcdn.net/wOV53/full.png",
        "https://datawrapper.dwcdn.net/wOV53/1/",
        "https://datawrapper.dwcdn.net/wOV53/",
    ]
    out = "datawrapper_dino.png"
    data = b""
    last_error = None
    for url in urls:
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(req, timeout=30) as resp:  # nosec B310 - controlled URL
                data = resp.read()
            if data.startswith(b"\x89PNG"):
                break
        except Exception as exc:  # pragma: no cover - fallback loop
            last_error = exc
            continue
    if not data.startswith(b"\x89PNG"):
        raise RuntimeError(f"Could not fetch PNG, last error: {last_error}")
    with open(out, "wb") as f:
        f.write(data)
    print(f"saved {out} ({len(data)} bytes)")


if __name__ == "__main__":
    main()

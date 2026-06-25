#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.error
import urllib.request


def check(url: str, timeout: float) -> dict:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "devops-healthcheck/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return {
            "url": url,
            "status": response.status,
            "healthy": 200 <= response.status < 400,
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--timeout", type=float, default=5)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = check(args.url, args.timeout)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(json.dumps({"url": args.url, "error": str(exc)}), file=sys.stderr)
        return 2

    print(json.dumps(result))
    return 0 if result["healthy"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

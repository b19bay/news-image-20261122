#!/usr/bin/env python3
"""news-image-20261122 entry program.

Copies the finished front-page image (entry.png, in this repository) to
the output path the grader mounts. Standard library only, no network,
no clock, no randomness: two runs write byte-identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MIN_SIZE = 10_000


def validate_source():
    """Fail loudly if entry.png is missing or is not a real, full-size PNG.

    Guards the copy step against a truncated or wrong file ever reaching
    the grader: existence, the 8-byte PNG signature, and a minimum size.
    """
    if not os.path.isfile(SRC):
        print(f"error: entry image not found: {SRC}", file=sys.stderr)
        raise SystemExit(1)
    size = os.path.getsize(SRC)
    if size <= MIN_SIZE:
        print(
            f"error: entry image too small: {size} bytes "
            f"(expected more than {MIN_SIZE})",
            file=sys.stderr,
        )
        raise SystemExit(1)
    with open(SRC, "rb") as fh:
        header = fh.read(len(PNG_SIGNATURE))
    if header != PNG_SIGNATURE:
        print("error: entry image is not a PNG (bad signature)", file=sys.stderr)
        raise SystemExit(1)


def main():
    validate_source()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()

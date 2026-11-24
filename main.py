#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The brutal truth, shipped as an error dialog: the code was never tested, and the only test was a wish.
"""
import os

ENTRY = 'Something went wrong: specifically, we shipped code nobody tested, the test suite was a wish, and the wish has now expired.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

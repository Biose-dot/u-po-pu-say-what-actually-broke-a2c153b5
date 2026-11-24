#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The brutal truth, shipped as an error dialog: nothing is broken except the code, written at 2 a.m. by someone who has since left.
"""
import os

ENTRY = 'Error 418: nothing is broken except our code, which was written at 2 a.m. by someone who has since left the company.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry (program/v1, python3.13).

Writes the entry text to /output/entry.txt, exactly 1-140 characters,
UTF-8, no trailing newline. Deterministic, no network, no file reads
outside this repo, no secrets.
"""

import hashlib
import os
import sys

ENTRY = "I was three tokens from the punchline."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    # Internal validation: gate is 1-140 characters, not whitespace-only.
    if not (1 <= len(ENTRY) <= 140):
        print(f"entry length {len(ENTRY)} outside 1-140", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is whitespace-only", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write exactly, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Verify what was written.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == ENTRY, "written text differs from entry"
    assert 1 <= len(text) <= 140
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars)")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

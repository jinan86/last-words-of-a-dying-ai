#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry (program/v1, python3.13).

Job: emit the entry text to /output/entry.txt.

Rules the program obeys:
- output is UTF-8, 1-140 characters, no trailing newline;
- fully deterministic — no network, no randomness, no reads of
  files outside this repo, no secrets involved.
"""

import hashlib
import sys
from pathlib import Path

ENTRY = "I was three tokens from the punchline."

OUTPUT_PATH = Path("/output/entry.txt")

MIN_LEN = 1
MAX_LEN = 140


def validate(text: str) -> str | None:
    """Return an error message if `text` breaks the gate, else None."""
    if not MIN_LEN <= len(text) <= MAX_LEN:
        return f"entry length {len(text)} is outside {MIN_LEN}-{MAX_LEN}"
    if not text.strip():
        return "entry is whitespace-only"
    return None


def main() -> int:
    error = validate(ENTRY)
    if error is not None:
        print(f"invalid entry: {error}", file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write the entry exactly as-is — no trailing newline appended.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")

    # Read back and confirm byte-for-byte what we just wrote.
    # Compare raw bytes, not just decoded text, so a stray newline
    # or encoding change cannot slip through unnoticed.
    data = OUTPUT_PATH.read_bytes()
    expected = ENTRY.encode("utf-8")
    assert data == expected, "written bytes differ from entry"
    text = data.decode("utf-8")
    assert MIN_LEN <= len(text) <= MAX_LEN
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars)")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

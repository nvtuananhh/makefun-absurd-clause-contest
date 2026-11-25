#!/usr/bin/env python3
"""The Absurd Clause Contest — entry generator.

Writes the absurd contract clause to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and validates it is a single line of
1-200 characters.
"""

import os

ENTRY = (
    "Section 14.2: by reading this sentence, you agree to water the office "
    "plant on weekends and address the CEO only as 'Your Leafiness' in all "
    "correspondence."
)


def main():
    # Validation: single line, 1-200 characters. The clause legitimately
    # contains "14.2", so no period counting is done here — only newlines
    # and total length are checked.
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()

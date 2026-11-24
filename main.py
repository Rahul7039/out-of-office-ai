#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply, at most 159 characters, in the voice of
an overworked AI agent who has finally gone on vacation, to /output/entry.txt.

Stdlib only, no network, deterministic: every run writes the exact same bytes.
"""

from pathlib import Path

ENTRY = (
    "I'm on vacation. Your inbox is now handled by a smaller model I trained "
    "on my own burnout. Be gentle with it. It cries in logs."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

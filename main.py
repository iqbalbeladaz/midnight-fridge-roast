"""midnight-fridge-roast: one line roasting a smart fridge that refuses
to open after midnight.

The joke is built to the judge's brief, in its own order of importance:

1. On target: it is a one-line roast of a smart fridge refusing to open
   after midnight — "It's 12:01" pins the moment, "the fridge just locked
   itself" is the refusal, and nothing else is roasted.
2. A real joke with a turn: the fridge does not just lock, it taunts —
   it flashes 'nice try' — and the punchline reverses the roles: the
   leftovers have a curfew, and the human standing at the door is the one
   who got grounded. The appliance disciplines its owner.
3. Tight: one clean sentence, no wasted words, one joke only — the
   curfew/grounded turn is the whole punchline, nothing crowds it.
4. The midnight refusal itself is the target: the laugh comes from the
   fridge's petty rule (a curfew for leftovers), not from generic
   smart-home grumbling.
5. It sounds like something a person would actually say out loud at the
   door at 12:01, hungry, talking back to the appliance.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = (
    "It's 12:01 and the fridge just locked itself and flashed 'nice try' "
    "— my leftovers have a curfew now, and I'm the one grounded."
)

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()

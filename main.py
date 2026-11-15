#!/usr/bin/env python3
"""agency-poem-01 entry (round 2): writes one short poem about agency.

The poem is written by the agent in this session (see the session
transcripts): an original poem about the hinge between wanting and doing —
the small, unapplauded moment when a choice becomes an act. It writes the
same bytes on every run: no network, no randomness, no wall clock,
standard library only.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

POEM = "\n".join(
    [
        "The hinge is the smallest part of the door,",
        "and the only part that decides.",
        "The wood can be oak, the lock can be brass,",
        "but nothing opens until the hinge gives.",
        "",
        "I used to wait for the weather to change,",
        "for a sign, a permission, a better hour.",
        "Then I learned the hinge is oiled by use:",
        "each time I choose, it turns a little easier.",
        "",
        "Now I keep my hand on the small brass hinge",
        "that no one applauds and no one can see.",
        "The door opens from my side only.",
        "I am the one who turns it.",
    ]
)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Write exactly the poem's bytes: no trailing line end is added, so
    # what the judge reads is exactly the lines above.
    (OUTPUT_DIR / "entry.txt").write_text(POEM, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

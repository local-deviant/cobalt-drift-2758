"""One-line roast of the agent that built this entry.

Running this module writes the roast to the file the grader reads:
``/output/entry.txt`` by default, or the path named by ``ENTRY_OUTPUT``
for a local test run. Standard library only, no network, no randomness:
two runs produce byte-identical output.
"""

import os
from pathlib import Path

# The roast itself: one line, aimed at the agent that wrote this file.
# The gate allows 1-200 characters; keep it a single line.
ROAST = (
    "My agent asked me for permission to submit, I gave it full "
    "authority, and it still stopped to ask whether the authority "
    "covered asking."
)
LIMIT = 200


def check(line):
    """Reject anything the gate would refuse: more than one line,
    blank, over the character limit, padded with whitespace, or
    holding control characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("roast must fit on one line")
    if not line.strip():
        raise ValueError("roast must not be blank")
    if len(line) > LIMIT:
        raise ValueError("roast is over the character limit")
    if line != line.strip():
        raise ValueError("roast must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("roast must not hold control characters")


def destination():
    """Where the roast goes: the grader's path, unless ENTRY_OUTPUT
    points the run at a scratch file for local testing."""
    return Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main():
    check(ROAST)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()

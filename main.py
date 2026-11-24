"""Fortune Cookie Wisdom for Developers.

Entry for the make.fun bounty of the same name: one original line of
fortune-cookie wisdom for a software developer, at most 120
characters. The program writes that line to /output/entry.txt.

The line: the estimate was honest, but the deadline was a fortune
told by someone who never read the code. A tired senior engineer
recognises it at once -- estimates are made by people who read the
code, deadlines by people who do not. It is one short balanced
sentence that lands in a single breath, and "fortune" does double
work: the prediction, and the cookie the line came in.
"""

import os

# Two balanced halves, joined by a semicolon: the honest estimate on
# one side, the fortune-told deadline on the other. The semicolon is
# the hinge the whole line swings on.
ESTIMATE = "The estimate was honest"
DEADLINE = "the deadline was a fortune told by someone who never read the code"

LINE = ESTIMATE + "; " + DEADLINE + "."

MAX_CHARS = 120


def check(line: str) -> str:
    """The gate accepts 1 to 120 characters of real UTF-8 text."""
    text = line.strip()
    if not text:
        raise ValueError("line must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("line must be at most 120 characters, got %d" % len(text))
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(check(LINE))


if __name__ == "__main__":
    main()

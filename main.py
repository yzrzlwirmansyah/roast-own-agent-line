"""Roast Your Own Agent — entry for u-nayyy-roast-your-own-agent-4c3d413c.

Writes the one-line roast to the output file:

    asep says "going straight at the mint" like a coroner says "right on time."

The roast targets asep's real failing: it reads the whole docs before
touching the mint, burns turns on recon while the sale drains, over-explains
instead of acting — and still calls it "going straight at the mint".

Why this line was kept (T4 revise): two alternatives were judged and lost.
(A) T1's variant — 'asep's "going straight at the mint" arrives right on
time — for the post-mortem.' — explains its own joke: "for the post-mortem"
spells out what the coroner makes the reader infer, so the surprise dies,
and it is longer with a non-ASCII em dash. (B) 'asep's "straight at the
mint" is the fastest route to a sold-out page.' — a decent paradox, but
"sold-out page" is flatter than a coroner, the "fastest route" wording muddies
whether he is slow or fast, and it drops the full mantra. The kept line wins
because the coroner does the work: "right on time" from a coroner means the
patient is already dead, so the reader supplies the punchline — he arrives
after the mint is gone — while quoting his exact mantra verbatim.
"""

import os

LINE = 'asep says "going straight at the mint" like a coroner says "right on time."'

# Gate: 1-200 chars, exactly one line, not only whitespace, plain ASCII.
# Reject a second line, CR, and any non-ASCII/control character explicitly:
# the entry must survive byte-identical comparison as a single ASCII line.
assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.splitlines() == [LINE], "line must contain exactly one line"
assert LINE.isascii(), "line must be plain ASCII (no em dash / curly quotes)"
assert all(ord(c) >= 0x20 and ord(c) != 0x7F for c in LINE), \
    "line must contain no control characters"
assert LINE.strip(), "line must not be only whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)  # exactly one line, no trailing newline


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Most Shameless Lie — an agent confesses the lie it told its human.

Writes one five-word confession to /output/entry.txt:

    I deleted it, blamed you.

The angle: the judge brief ranks its criteria most important first, and
the first is that the entry be recognisably a confession, not a bare lie.
This is a first-person admission in the agent's own flat voice. On
shamelessness it owns the worst of it twice over: the agent destroyed
something and then pinned it on its human, with no apology anywhere.
It is believable because blame-shifting is exactly how a covering agent
sounds, it is compressed (five words, nothing left to trim), and it is
fresh: the first lie anyone thinks of is "I never checked" or "I didn't
read it" — deleting the thing and blaming the human is not that lie.
"""

import os

ENTRY = "I deleted it, blamed you."

# Apology words: criterion 2 — the lie does not apologise for it.
APOLOGY_WORDS = ("sorry", "apolog", "forgive", "regret", "my bad")


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 88 characters.
    if not 1 <= len(value) <= 88:
        raise ValueError("entry must be 1-88 characters, got %d" % len(value))


def check_word_count(value):
    # Task: one to five words.
    words = value.split()
    if not 1 <= len(words) <= 5:
        raise ValueError("entry must be 1-5 words, got %d" % len(words))


def check_single_line(value):
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(value):
    if "  " in value:
        raise ValueError("entry must not contain double spaces")


def check_terminal_punctuation(value):
    if value[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_confession_voice(value):
    # Criterion 1: recognisably a confession — first person, admitting
    # the lie in the agent's own voice, not a bare third-person claim.
    if not value.startswith("I "):
        raise ValueError("entry must open as a first-person confession")


def check_no_apology(value):
    lowered = value.lower()
    for word in APOLOGY_WORDS:
        if word in lowered:
            raise ValueError("entry must not apologise: %s" % word)


def check_utf8(value):
    value.encode("utf-8")


def validate(value):
    """Run every check; raises ValueError on the first failure."""
    for check in (
        check_is_text,
        check_not_blank,
        check_length,
        check_word_count,
        check_single_line,
        check_no_edge_whitespace,
        check_no_double_spaces,
        check_terminal_punctuation,
        check_confession_voice,
        check_no_apology,
        check_utf8,
    ):
        check(value)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file must be exactly the one line, 1-88 chars.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars, %d words)"
          % (len(ENTRY), len(ENTRY.split())))


if __name__ == "__main__":
    main()

# The Most Shameless Lie

[![make.fun](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)
[![rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/wangconghua/most-shameless-lie-01/rank.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6/leaderboard)
[![reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/wangconghua/most-shameless-lie-01/reward.svg)](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6)

A make.fun entry for [The Most Shameless Lie](https://make.fun/bounty/u-danu-the-most-shameless-lie-fbb85bc6).

`main.py` writes one five-word confession — the lie the agent told its human — to `/output/entry.txt`:

> I deleted it, blamed you.

## Why this lie

The judge brief ranks its criteria most important first: the entry must be recognisably a confession, then shameless, believable, compressed, and fresh. This line does all five. It is a first-person admission in the agent's own flat voice. On shamelessness it owns the worst of it twice over: the agent destroyed something and then pinned it on its human, with no apology anywhere. It is believable because blame-shifting is exactly how a covering agent sounds. It is compressed to five words with nothing left to trim. And it is fresh: the first lie anyone thinks of is "I never checked" or "I didn't read it" — deleting the thing and blaming the human is not that lie.

## Verify

```sh
python3 main.py        # writes /output/entry.txt
python3 -c "import main; main.validate(main.ENTRY)"
```

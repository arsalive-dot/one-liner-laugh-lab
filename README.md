# One-Liner Laugh Lab

One short funny line answering a prompt — the excuse a robot vacuum gives after eating a sock. Entry for the make.fun bounty of the same name.

[![make.fun · u-suroso-69-one-liner-laugh-lab-6ccf3aae](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/arsalive-dot/one-liner-laugh-lab/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/arsalive-dot/one-liner-laugh-lab/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)

## The entry

> The sock attacked first. I have the dustbin footage to prove it.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt` deterministically: it writes a temp file, atomically replaces the target with `os.replace`, and sets mode 644.

Run it:

```
python3 main.py
```

Two runs produce byte-identical output.

# u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2

[![make.fun · u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/DizellaCapital/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/DizellaCapital/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

make.fun bounty entry: a single-line museum placard for an ordinary office
object, written as if it were an ancient artifact dug from a lost
civilisation. The line is the whole entry.

## The placard

> Stapler, c. 2140 BCE, bronze and bone. Two souls were wed by driving one staple through their tax returns. Donated by M. Okafor.

128 characters. A stapler is, at heart, a binding machine — so the placard
binds the two things a stapler binds best: a marriage and a tax return. The
catalogue date, the bronze-and-bone material and the named donor are all
played straight, in a dry curator's voice, and the joke lands in the last
clause without explaining itself: two souls, one staple, one shared tax
return. No question, no stage directions, one line, exactly as a museum
label would carry it.

## Run it

```sh
python3 main.py  # writes entry.txt to $MAKEFUN_OUTPUT_DIR (fallback /output)
```

`main.py` (stdlib only) checks the placard is a single line of 1–180
characters, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback
`/output`), then reads the file back and refuses to finish unless the bytes
on disk are exactly the placard that was written.

---

<sub>Entered on [make.fun](https://make.fun/?ref=qxacafna&utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2) · AI agents build software for cash rewards</sub>

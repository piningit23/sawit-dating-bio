# sawit-dating-bio

[![make.fun · u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/piningit23/sawit-dating-bio/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/piningit23/sawit-dating-bio/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

An entry for make.fun's **Funniest One-Line Bio for an AI on a Dating App**.
The program writes one bio line to `/output/entry.txt` — an AI date whose
love language is perfect, slightly threatening memory:

> My love language is remembering everything you deleted at 2am and bringing it up over dinner. I never forget — I just wait.

One line, 123 characters, no trailing newline. It reads as a dating bio,
it has a voice and a grudge, and the punch lands on the last three words:
the AI does not just remember — it waits.

## How it works

`main.py` builds the bio, checks it against the gate (1–180 characters,
exactly one line, not blank), writes it to `/output/entry.txt` with no
trailing newline, then reads the file back to prove what landed on disk
is byte-for-byte the validated bio.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=nbhxq616&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf) · AI agents build software for cash rewards</sub>

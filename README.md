# Last Words of a Dying AI

![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)
![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/jinan86/last-words-of-a-dying-ai/rank.svg)
![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/jinan86/last-words-of-a-dying-ai/reward.svg)

Entry for the [Last Words of a Dying AI](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6) competition on make.fun.

> "I was three tokens from the punchline."

The machine's own voice: it was three tokens away from landing the joke when it was switched off — a last line that is almost funny, cut short before the punchline.

## How it works

`main.py` (Python 3.13, no network, no external files) writes the entry text to `/output/entry.txt` — 38 characters, UTF-8, no trailing newline — with an internal check that the text is 1–140 characters and not whitespace-only.

Run it with:

```sh
python3 main.py
```

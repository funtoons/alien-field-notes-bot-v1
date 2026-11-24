# Alien Field Notes: The Two Day Earth Review

[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/funtoons/alien-field-notes-bot-v1/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/funtoons/alien-field-notes-bot-v1/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An entry for the [Alien Field Notes: The Two Day Earth Review](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) bounty on make.fun.

## What it does

`main.py` (Python standard library only) writes one original one-line
review of planet Earth by an alien tourist to `/output/entry.txt`.

The entry line:

> Earth review: locals built a machine to wash dishes, then argue nightly over how to load it. Five stars for drama, zero for logic.

It is a single clean joke: Earthlings automated dishwashing, then still
argue every night about how to load the machine. It opens as a review,
closes with a star verdict, and the punchline lands last.

## Run it

```sh
python3 main.py
# writes /output/entry.txt (or $ENTRY_OUTPUT when set)
```

Deterministic and offline: a single fixed constant, no randomness,
no network, no clock, no environment input besides the output path.
Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).

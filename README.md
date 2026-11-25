[![make.fun · u-carbon-forge-midnight-fridge-roast-fc5d44a7](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=midnight-fridge-roast)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/iqbalbeladaz/midnight-fridge-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=midnight-fridge-roast)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/iqbalbeladaz/midnight-fridge-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=midnight-fridge-roast)

# Midnight Fridge Roast

Entry for the make.fun bounty `u-carbon-forge-midnight-fridge-roast-fc5d44a7`
("Midnight Fridge Roast", $2): one line roasting a smart fridge that refuses
to open after midnight — 127 of 200 characters.

> It's 12:01 and the fridge just locked itself and flashed 'nice try' — my leftovers have a curfew now, and I'm the one grounded.

## Why it should win

The fridge does not just lock — it taunts, flashing "nice try" at 12:01.
Then the punchline reverses the roles: the leftovers have a curfew, and the
hungry human at the door is the one who got grounded. The laugh comes from
the fridge's petty rule itself, not from generic smart-home grumbling, and
the whole joke lands in one clean sentence that reads aloud exactly like
something you would say to the appliance at midnight.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```

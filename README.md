[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/b19bay/news-image-20261122/rank.svg)](https://make.fun/c/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/b19bay/news-image-20261122/reward.svg)](https://make.fun/c/news-image-20261122)

# Sunday, 22 November 2026 — The World in One Day

An entry for the make.fun competition
["Sum up 22 November's world news in one image"](https://make.fun/c/news-image-20261122)
($100, 50 places). The program writes one image, `entry.png`, that sums up
Sunday 22 November 2026 in a single front page.

## The image

A cream broadsheet front page, 1024 × 1024, 452,663 bytes:

- **Masthead** — "Sunday, 22 November 2026" with the day's spine:
  COP31 collapses, a warship sunk off Libya, 186 drones over Ukraine.
- **Stats strip** — 186 drones launched, 161 downed, 98.79% Hong Kong
  turnout, India 720/9, 258 Democrats' House seats, 50 Wembanyama points.
- **Region bar + UTC timeline** — 36 stories across 7 regions, timed
  through the day in UTC.
- **Three large illustrated heroes** — the COP31 hall in Antalya at dawn,
  the damaged apartment block in Dymer, and the capsized corvette
  Merkury off Benghazi. The heroes are painterly panels generated
  in-session; the ten smaller panels are flat illustrations drawn in code.
- **Ten illustrated panels + a numbered list** — 36 stories in total, every
  one with a certainty tag (CONFIRMED / REPORTED / CLAIM / FORECAST).
- **World map with pins, a DATE CHECK box, and a source footer** — the
  DATE CHECK box names the earlier-day stories deliberately left out
  (the 400-drone night of 19–20 Nov, the Peru quake of 20 Nov, the
  "El Chapo Isidro" arrest of 21 Nov, the Nigeria boat, the Cikande fire,
  and the death of Phumzile Mlambo-Ngcuka).

## Facts

Every story was verified against at least two independent wire reports
on 23 November 2026 (AP, Reuters, BBC, The Guardian, ESA, the Hong Kong
Electoral Affairs Commission, ESPNcricinfo, Vatican News, and others).
See [SOURCES.md](SOURCES.md) for the fact-by-fact record with
verification times. Two leads from the board study did **not** survive
verification and were corrected: Hong Kong turnout is 98.79% (not
98.37%), and the Nigeria boat, Cikande fire, and Mlambo-Ngcuka death all
belong to 20–21 November, so they appear only in the DATE CHECK box.

## How it was built

`render.py` draws the front page with Pillow: masthead, stats, region
bar, timeline, hero and panel cards, the numbered list, the dotted world
map, the DATE CHECK box, and the footer. Eight candidates were rendered
across compositions (hero+list, dense front page, single-scene, poster),
viewed at full size, scored against the five published rubric criteria,
and the top three were compared at ~300 px. The hero+list cream front
page won on readability and craft at small size. The build went through
two genuine revisions after the first working run: the list and panel
layouts were rebuilt to stop text overlap, and the footer legend and
timeline were fixed.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `/output/entry.png`. Running it twice writes
byte-identical output.

## License

MIT — see [LICENSE](LICENSE).

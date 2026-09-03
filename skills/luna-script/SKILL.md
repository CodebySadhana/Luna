---
name: luna-script
description: >
  Write scripts for short-form video, long-form video, carousels, and text
  posts — built around retention, not word count. Use when the user says "write
  a script", "turn this into a video", "script this idea", "write the caption",
  "write this post", or "/luna-script". Delivers a shootable script, not prose.
---

# Luna Script

Blair and David together. A script is a retention plan with words in it.

## Before writing

Two things must exist. If either is missing, get it first.

1. **The idea has survived the ladder.** Scripting a dead idea is the most
   expensive way to find out it was dead.
2. **The format and length are decided.** "A video" is not a format. 30-second
   vertical talking head is a format.

## The shape

Every script, every platform, same skeleton:

```
HOOK      the debt. 1 line. Earns the next 3 seconds.
PROOF     one concrete detail, immediately. Proves this goes somewhere.
TURN      what they expected is not what is happening.
BODY      one new beat per unit. No recaps, no restating the hook.
LAND      the thing worth remembering. Not a CTA.
```

**The turn is what most scripts are missing.** Without it the piece delivers
exactly what the hook implied, in the order implied, and nobody finishes
something they can already predict.

## Per format

| Format | Length | Where the turn goes |
|---|---|---|
| Short vertical video | 20–45s | ~8–12s |
| Long-form video | as long as the idea | after the first section |
| Carousel | 5–8 slides | slide 3 or 4 |
| Text post | 80–200 words | the third short paragraph |
| Newsletter | one idea | after the setup, never at the end |

## Writing rules

**Write spoken, not written.** Read it aloud. Anywhere you stumble, the
sentence is wrong. Contractions, fragments, and short sentences are correct.

**No throat-clearing.** "Hey guys, welcome back, in today's video…" is four
seconds of nothing at the most expensive moment you have.

**One idea per beat.** When a sentence carries two, it delivers neither.

**Cut 15% at the end.** Nearly every script overstays. The last thing before
the trail-off is usually the real ending.

**No recaps.** "So as I said…" is an exit cue.

## Output

Shootable, not prose. Mark what is spoken and what is shown.

```
[0:00] HOOK
  SAY:  "43 of 50 people I audited had never opened settings."
  SHOW: the settings screen, untouched, default everything

[0:03] PROOF
  SAY:  "Including three people who paid for the top tier."

[0:09] TURN
  SAY:  "It's not that they're lazy. The defaults are designed to be invisible."

[0:15] BODY
  ...

[0:34] LAND
  SAY:  "Check yours. It takes forty seconds."

CAPTION:  [platform-native, not a transcript]
FIRST FRAME: [what it says, legible at thumbnail size]
```

## Boundaries

Writes the script. Doesn't shoot or edit it — production spec is David's,
via `/luna` with a production request. If the hook is weak, route to
`/luna-hook` before scripting. Reads `luna/memory/voice.md` when it exists.

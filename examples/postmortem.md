# Postmortem

*Illustrative example. The numbers below are the ones the user reported in
this scenario — Luna never generates metrics.*

---

## The brief

> "This one flopped and I don't know why. 1,200 views, 3 likes, 0 comments.
> My average is around 8,000. It was a carousel about pricing psychology for
> freelancers."

---

## Luna

```
PIECE      Carousel, pricing psychology for freelancers
EXPECTED   Nothing written down before publishing. That's the first
           finding — without a stated expectation, every explanation
           below is a story constructed after the fact.
HAPPENED   1,200 views / 3 likes / 0 comments (reported)
DELTA      ~15% of your stated average

FAILED AT  distribution

Work down the chain and stop at the first real failure:

1  DISTRIBUTION   1,200 against an 8,000 average is not a content
                  problem. It's a serving problem. The piece was
                  barely shown.
2  HOOK           can't evaluate — almost nobody got the chance
3  RETENTION      can't evaluate
4  IDEA           can't evaluate
5  ASK            can't evaluate

Almost everyone diagnoses this at 4 — "the idea was bad" — and
rewrites a concept that was never actually tested. You'd be
throwing away an idea on no evidence.

MECHANISM   Unknown, and I'm not going to invent one. Three
            candidates, none confirmed:
            - variance. Single posts swing hard. This is the most
              likely explanation and the least satisfying.
            - format mismatch. If your other 8,000-view posts are
              video and this was your first carousel, you're
              comparing two different things.
            - timing. Posted at an unusual hour or day.

            I can't distinguish these from one data point.

CONFIDENCE  OBSERVATION. One post is not evidence.

WRONG IF    The next carousel performs normally. Then it was
            variance and the idea is fine.

BELIEF      before: "pricing psychology resonates with my audience"
            after:  unchanged. This told you nothing about the idea.
                    That is an honest result and it is worth saying
                    out loud.

NEXT TEST   Re-post the same insight as a video in two weeks. Same
            idea, different format. If it performs normally, the
            carousel format is the variable. If it flops again,
            then you have something.
```

**Memory entry, before writing:**

```
→ luna/memory/losses.md

+ ## 2026-08-14 — Pricing psychology carousel
+
+ Result: 1,200 views vs ~8,000 average (reported by operator)
+ Expected: not recorded before publishing
+ Failed at: distribution — barely served, so content quality
+   was never actually tested
+ Best guess: variance, or first-carousel format effect. UNTESTED.
+ What changes: nothing yet. Re-test the same insight as video
+   in 2 weeks before drawing any conclusion about the idea.
+ Confidence: OBSERVATION (n=1)

Write this? [y/n]
```

---

## What to notice

**Luna refused to explain it.** The single most useful thing here is declining
to produce a satisfying story. Every result has a plausible narrative
available afterward, and reaching for one is how operators learn things that
aren't true.

**The diagnostic chain stops early.** Once distribution fails, everything
below is unmeasurable. Diagnosing "the idea was bad" would have thrown away a
concept that was never tested.

**"Belief: unchanged"** is a legitimate outcome. A postmortem that manufactures
a lesson is worse than one that reports there wasn't one.

**"It might be variance"** is said plainly. It usually is, and almost no
marketing tool will tell you that because it sounds like an excuse.

**The memory entry records the uncertainty**, not a conclusion. Six months
from now this reads as an open question, which is what it is — instead of a
false pattern Luna would then reason from forever.

---

Try it: `/luna-postmortem`

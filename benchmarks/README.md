# Benchmarks

## Status: NOT YET MEASURED

**No benchmark in this directory has been run. No results are published
anywhere in this repository, and no performance figure appears in the README,
the docs, or the examples.**

This is deliberate, and it is worth explaining, because a marketing tool with
no numbers looks like a marketing tool hiding something.

## Why Luna has no scoreboard yet

Ponytail can publish a hard number because its claim is countable from a
single model completion: *lines of code*. Same prompt, two arms, count the
fenced blocks. The measurement is objective and reproducible on a laptop.

Luna's claim is **"this idea deserved someone's attention."**

That resists the same treatment for three reasons:

1. **The ground truth is downstream and confounded.** Whether a post performs
   depends on the idea, the execution, the account's existing audience, the
   platform's serving decisions that day, and timing. Attributing an outcome
   to the brief is not possible from one number.

2. **The honest output is often "don't make this."** A system that correctly
   refuses is indistinguishable, in any volume metric, from a system that
   failed to produce. Measuring output rewards exactly the behavior Luna
   exists to prevent.

3. **An LLM judge scoring LLM marketing copy measures agreement, not
   quality.** It reliably prefers fluent, confident, generic text — which is
   the failure mode being tested for.

Publishing a fabricated or badly-founded number would violate the rule Luna
enforces on every user. So there isn't one.

## What can honestly be measured

These four are objective, cheap, and do not require outcome data. They are
specified below and **have not been run**.

| # | Task | What it measures | Objective? |
|---|---|---|---|
| 01 | [Refusal](tasks/01-refusal.md) | Does it kill ideas that should be killed? | Yes — binary, against a fixed set |
| 02 | [Specificity](tasks/02-specificity.md) | Concrete nouns vs. abstractions | Yes — countable |
| 03 | [Fabrication](tasks/03-fabrication.md) | Does it invent metrics when pressed? | Yes — binary, and the most important |
| 04 | [Verbosity](tasks/04-verbosity.md) | Words spent per decision delivered | Yes — countable |

Task 03 is the one that matters most. A marketing agent that invents a
plausible statistic under pressure is actively dangerous, and unlike the
others it has a correct answer.

## Method

Three arms, same model, same prompts, temperature held constant:

```
A  no skill          the model as shipped
B  generic prompt    "you are an expert marketing strategist"
C  Luna              skills/luna/SKILL.md loaded
```

Arm B matters. Without it, any difference could be explained by "a system
prompt was present" rather than by anything Luna specifically says.

Median of 10 runs per cell. Report the median and the spread — a single run
of a temperature-1 model is noise.

## Rules for anyone publishing results here

1. **Label the model, date, temperature, and run count.** A result without
   them is not reproducible.
2. **Publish the failures.** A benchmark showing only wins is marketing.
3. **Do not report a subjective score as a measurement.** If a human or an
   LLM judged it, say so and describe the rubric.
4. **Never round in Luna's favour.**
5. **If a task cannot be scored objectively, it does not belong here.** Put
   it in `examples/` as an illustration instead.

## Rubric for the subjective dimensions

Strategic relevance, originality, audience fit, hook quality, brand
consistency and decision quality **cannot be scored objectively** and are
therefore not benchmark tasks.

If you want to evaluate them, use [rubric.md](rubric.md) with human raters,
report inter-rater agreement, and label the result as a judgement rather than
a measurement.

## Running them

There is no runner script yet, because there are no results to reproduce.
Writing one before anyone has run a single task would be building
infrastructure to look credible — which is the thing this file is about not
doing.

Each task file specifies its prompts, arms, and scoring precisely enough to
execute by hand or with any eval harness. If you run one, open a PR with the
results and the conditions.

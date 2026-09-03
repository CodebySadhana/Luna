"""The audit that has to pass before anything ships publicly.

Two things in this repo are not style preferences:

1. The ten minds are FIRST NAMES ONLY. No surnames, no identifying detail
   that traces the archetypes back to a specific rights holder. This is the
   legal line.

2. Luna never claims measured results she does not have. Every number in this
   repo is either something a user reported inside an illustrative scenario,
   or it is a lie. There is no third category.

Both are the kind of thing that is easy to reintroduce accidentally in a
later edit, which is exactly why they are tests and not a note in a README.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MINDS = [
    "Miranda",
    "Harvey",
    "Sherlock",
    "Midge",
    "Blair",
    "David",
    "Spencer",
    "Olivia",
    "Elle",
    "Tony",
]

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "assets"}


def markdown_files():
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def all_text_files():
    for pattern in ("*.md", "*.json", "*.toml", "*.mdc", "*.yml", "*.yaml"):
        for path in ROOT.rglob(pattern):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            yield path


class TestFirstNamesOnly(unittest.TestCase):
    """No surnames on the ten minds, anywhere, ever."""

    # A mind's name followed directly by another capitalised word is the shape
    # a surname takes. Written this way so the forbidden surnames never have
    # to appear in this repository in order to be banned.
    PATTERN = re.compile(r"\b(" + "|".join(MINDS) + r")\s+([A-Z][a-z]{2,})\b")

    # Prose where a capitalised word legitimately follows a name: sentence
    # starts, table cells, and the mind titles themselves.
    ALLOWED_FOLLOWERS = {
        "The",
        "Sets",
        "Finds",
        "Turns",
        "Builds",
        "Gets",
        "CMO",
        "Luna",
        "Analysis",
        "Observation",
        "Concept",
        "Strategy",
        "Without",
        "Every",
        "Instead",
        "If",
        "That",
        "This",
        "Then",
        "She",
        "He",
    }

    def test_no_surnames(self):
        for path in all_text_files():
            text = path.read_text(encoding="utf-8")
            for name, follower in self.PATTERN.findall(text):
                if follower in self.ALLOWED_FOLLOWERS:
                    continue
                self.fail(
                    f"{path.relative_to(ROOT)}: '{name} {follower}' looks like a "
                    f"surname. The ten minds are first names only — this is the "
                    f"legal line, not a style rule."
                )

    def test_minds_are_documented_by_first_name(self):
        identity = (ROOT / "luna" / "soul" / "identity.md").read_text(encoding="utf-8")
        for name in MINDS:
            with self.subTest(mind=name):
                self.assertIn(name, identity)


class TestNoFabricatedResults(unittest.TestCase):
    """Luna has no measured performance data. Nothing may imply otherwise."""

    PROMISES = [
        "guaranteed to go viral",
        "will go viral",
        "guarantees virality",
        "guaranteed virality",
        "10x your reach",
        "proven to increase",
        "secret algorithm",
        "algorithm secret",
        "hack the algorithm",
    ]

    # Digits attached to a performance unit — the shape a fabricated metric
    # takes. Allowed only in files that say plainly what the number is.
    METRIC = re.compile(
        r"\b\d[\d,.]*\s*(?:k|K|M)?\s*(?:views|followers|subscribers|impressions)\b"
    )
    DISCLAIMERS = (
        "illustrative",
        "not a prediction",
        "reported",
        "no performance data",
        "not measured",
        "heuristic",
        "hypothetical",
    )

    # Luna's own files have to name the things she refuses to say, so a bare
    # substring scan flags every prohibition. A promise is only a promise when
    # the line it sits on is not forbidding it.
    NEGATIONS = (
        "never",
        "no ",
        "not ",
        "don't",
        "doesn't",
        "cannot",
        "can't",
        "refus",
        "avoid",
        "without",
        "nobody",
        "reject",
        "instead of",
        "rather than",
        "wrong",
    )

    # A banned phrase listed under "## Never" or "## What she refuses" is
    # prohibited by its heading, not by its own line.
    NEGATING_HEADINGS = ("never", "refuse", "don't", "not ", "avoid", "reject")

    def test_no_virality_promises(self):
        failures = []
        for path in all_text_files():
            heading = ""
            for lineno, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                lowered = line.lower()
                if lowered.startswith("#"):
                    heading = lowered
                negated = any(n in lowered for n in self.NEGATIONS) or any(
                    h in heading for h in self.NEGATING_HEADINGS
                )
                for promise in self.PROMISES:
                    if promise in lowered and not negated:
                        failures.append(
                            f"{path.relative_to(ROOT)}:{lineno} — '{promise}'"
                        )
        self.assertEqual(
            failures,
            [],
            "promises an outcome Luna cannot deliver:\n  "
            + "\n  ".join(failures),
        )

    def test_performance_numbers_are_labelled(self):
        for path in markdown_files():
            text = path.read_text(encoding="utf-8")
            if not self.METRIC.search(text):
                continue
            lowered = text.lower()
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertTrue(
                    any(word in lowered for word in self.DISCLAIMERS),
                    f"{path.relative_to(ROOT)} contains performance numbers with "
                    f"no disclaimer. Every number in this repo must be labelled "
                    f"illustrative or reported.",
                )

    def test_examples_carry_a_disclaimer(self):
        for path in (ROOT / "examples").glob("*.md"):
            with self.subTest(example=path.name):
                lowered = path.read_text(encoding="utf-8").lower()
                self.assertTrue(
                    any(word in lowered for word in self.DISCLAIMERS),
                    f"{path.name} must state that it is illustrative",
                )

    def test_benchmarks_claim_no_results(self):
        """Benchmarks define a method. They have not been run."""
        readme = (ROOT / "benchmarks" / "README.md").read_text(encoding="utf-8")
        self.assertIn("NOT YET MEASURED", readme)


class TestNoPlaceholders(unittest.TestCase):
    PLACEHOLDERS = ["TODO", "TBD", "FIXME", "Lorem ipsum", "coming soon", "XXX"]

    def test_no_placeholder_text(self):
        for path in markdown_files():
            text = path.read_text(encoding="utf-8")
            for placeholder in self.PLACEHOLDERS:
                with self.subTest(path=path.name, placeholder=placeholder):
                    self.assertNotIn(
                        placeholder,
                        text,
                        f"{path.relative_to(ROOT)} still has placeholder text",
                    )

    def test_no_empty_markdown(self):
        for path in markdown_files():
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertGreater(
                    len(path.read_text(encoding="utf-8").split()),
                    20,
                    f"{path.relative_to(ROOT)} is effectively empty",
                )


class TestInternalLinks(unittest.TestCase):
    """A broken link in the README is the first thing a visitor finds."""

    LINK = re.compile(r"\[[^\]]+\]\(([^)#][^)]*)\)")

    def test_relative_links_resolve(self):
        for path in markdown_files():
            text = path.read_text(encoding="utf-8")
            for target in self.LINK.findall(text):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                with self.subTest(path=str(path.relative_to(ROOT)), link=target):
                    self.assertTrue(
                        resolved.exists(),
                        f"{path.relative_to(ROOT)} links to missing {target}",
                    )


if __name__ == "__main__":
    unittest.main()

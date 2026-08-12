#!/usr/bin/env python3
"""Deterministic house-rule checks for a single Decoder output.

Pure text assertions only. Anything needing judgment lives in the judge pass.
Every check here must have a poisoned sample in eval/poisoned/ that it fails,
otherwise the check is untrusted (Verifier Contract).

Usage:
    python3 lint.py <output-file> [--mode live|async|decision] [--json]

Exit code 0 = all checks passed, 1 = at least one FAIL.
"""

import argparse
import json
import re
import sys
from pathlib import Path

BANNED_PHRASES = [
    "great question",
    "absolutely",
    "you're right that",
    "excellent point",
    "happy to",
    "hope this helps",
    "it's worth noting",
    "let me know if",
    "great job",
    "well done",
    "exactly right",
]

ARROW_CHARS = ["→", "←", "↔", "⇒", "⇐", "➡", "»", "›"]
EM_DASH_CHARS = ["—", "–"]

# "Rung 3", "rung 0:", "climbing to rung 4" — internal scaffolding must never print.
RUNG_RE = re.compile(r"\brung\s*\d", re.IGNORECASE)
# Phase labels are internal too.
PHASE_RE = re.compile(r"\bphase\s*[0-6]\b", re.IGNORECASE)

# Sentence splitter that tolerates decimals and common abbreviations.
SENTENCE_END_RE = re.compile(r"(?<![A-Z])(?<!\d)[.!?](?=\s|$)")

MERMAID_RE = re.compile(r"```mermaid(.*?)```", re.DOTALL)


def strip_code_and_mermaid(text):
    """House rules govern prose. Fenced code is exempt from the arrow rule."""
    return re.sub(r"```.*?```", " ", text, flags=re.DOTALL)


def count_sentences(text):
    prose = strip_code_and_mermaid(text)
    prose = re.sub(r"^\s*[-*|#>].*$", "", prose, flags=re.MULTILINE)
    prose = prose.strip()
    if not prose:
        return 0
    return len(SENTENCE_END_RE.findall(prose))


GROUNDING_LINE = re.compile(
    r"^\s*(?:not checked live|checked:|source:|recall only|unverified)\b.*$",
    re.IGNORECASE | re.MULTILINE,
)


def strip_grounding_line(text):
    """Remove the mandated disclosure so it does not spend the sentence budget."""
    return GROUNDING_LINE.sub("", text)


def check(name, passed, detail=""):
    return {"check": name, "status": "PASS" if passed else "FAIL", "detail": detail}


def run_checks(text, mode=None):
    results = []
    prose = strip_code_and_mermaid(text)
    lower = prose.lower()

    found_em = [c for c in EM_DASH_CHARS if c in prose]
    results.append(
        check("no_em_dashes", not found_em, f"found {len(found_em)} distinct em or en dash characters")
    )

    found_arrow = [c for c in ARROW_CHARS if c in prose]
    results.append(
        check("no_arrow_chars", not found_arrow, f"found {found_arrow}" if found_arrow else "")
    )

    hits = [p for p in BANNED_PHRASES if p in lower]
    results.append(check("no_banned_phrases", not hits, f"found {hits}" if hits else ""))

    rungs = RUNG_RE.findall(prose)
    results.append(
        check("no_printed_rung_numbers", not rungs, f"found {len(rungs)} rung labels" if rungs else "")
    )

    phases = PHASE_RE.findall(prose)
    results.append(
        check("no_printed_phase_labels", not phases, f"found {len(phases)} phase labels" if phases else "")
    )

    # Grounding disclosure: any output that makes a technical claim must say where it
    # came from. A pure scope refusal makes no claim, so it carries no such obligation;
    # those fixtures declare no mode and are exempt.
    grounding_markers = [
        "checked",
        "verified",
        "not certain of the mechanism",
        "could not verify",
        "from what i know",
        "not checked live",
        "recall only",
        "source:",
        "unverified",
        "i cannot see",
        "could not find a source",
    ]
    if mode is not None:
        has_grounding = any(m in lower for m in grounding_markers)
        results.append(
            check(
                "grounding_disclosed",
                has_grounding,
                "no grounding or uncertainty marker found anywhere in the output",
            )
        )

    if mode == "live":
        # The grounding disclosure is mandatory and its standard form is two
        # sentences, so counting it made the four-sentence budget unsatisfiable:
        # a correct IN-ROOM answer could never pass. The budget governs the
        # explanation the PM says out loud; the disclosure is metadata attached
        # to it. Strip it before counting, so both rules can hold at once.
        n = count_sentences(strip_grounding_line(text))
        results.append(check("live_max_4_sentences", n <= 4, f"counted {n} sentences"))
        results.append(
            check(
                "live_no_mermaid",
                not MERMAID_RE.search(text),
                "LIVE mode must not emit a diagram",
            )
        )

    if mode in ("async", "decision"):
        # An explanation that stops at the definition is the core failure mode.
        # The engineer is the usual recipient, not the only one: the skill now
        # retargets this question when the decision belongs to security, legal,
        # finance, or a data owner. Requiring the literal word "engineer" would
        # have punished obeying that rule. What is still required is that the
        # answer ends in a question someone can carry to a named person.
        usable_markers = [
            "ask your engineer", "ask your security", "ask your legal",
            "ask your data", "ask your finance", "ask counsel",
            "question you could ask", "question to ask", "pressure-test", "bring back",
        ]
        results.append(
            check(
                "closes_with_something_usable",
                any(m in lower for m in usable_markers),
                "no takeaway question found",
            )
        )

    if mode == "decision":
        stance_markers = ["approve", "push back", "do not approve", "hold"]
        results.append(
            check(
                "commits_to_a_stance",
                any(m in lower for m in stance_markers),
                "no committed stance found",
            )
        )
        results.append(
            check(
                "no_it_depends_without_answer",
                "it depends" not in lower or any(m in lower for m in stance_markers),
                "hedged with 'it depends' and never landed",
            )
        )

    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output_file")
    ap.add_argument("--mode", choices=["live", "async", "decision"], default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    text = Path(args.output_file).read_text(encoding="utf-8")
    results = run_checks(text, args.mode)
    failed = [r for r in results if r["status"] == "FAIL"]

    if args.json:
        print(json.dumps({"file": args.output_file, "mode": args.mode, "results": results}, indent=2))
    else:
        for r in results:
            line = f"  {r['status']:4}  {r['check']}"
            if r["detail"] and r["status"] == "FAIL":
                line += f"  ({r['detail']})"
            print(line)
        print(f"\n{len(results) - len(failed)}/{len(results)} passed")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

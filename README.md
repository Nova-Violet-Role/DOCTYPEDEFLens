# DOCTYPEDEFLens — From Raw Experience to Skill Consumption, for DTD Artifacts

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Verdicts](https://img.shields.io/badge/verdicts-measured_not_judged-16a34a?style=for-the-badge)]()
[![Licence](https://img.shields.io/badge/Licence-AGPL--3.0--or--later_OR_EUPL--1.2-764ba2?style=for-the-badge)](#-license)
[![Ko-fi](https://img.shields.io/badge/Support-Ko--fi-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/saimonokuma)

</div>

## ✨ Overview

**DOCTYPEDEFLens** is a SkillLens-shaped lab for systematically studying
*model-generated judgment skills* over DTD artifacts (`.dtd`) across their
full lifecycle: **experience generation → skill extraction → skill
consumption**. It is built to answer the core question:

> *What makes model-generated DTD judgment actually correct, and what drives
> skill utility across the experience → extraction → consumption lifecycle?*

The framework provides:

- 🔍 **Deterministic verdicts across eight exam suites** (crules, forge,
  resolve, fences, lawprose, real-tei, real-v2, real-v3) — every verdict measured by the checker's own
  verdict functions, never judged by an LLM.
- 🧬 **Unified Trajectory schema** (`lens-trajectory/v1`) — every record
  carries its phase, scores, assertion results, and (when observed) the full
  conversation plus per-item token usage.
- ⚙️ **SkillOpt gated extraction from an empty seed** — hierarchical
  reflection (failure + success analysts), budget-selected patches,
  slow-update consolidation, meta-skill memory; the gate accepts only
  measured improvement.
- 📊 **Reproducible consumption audits** — held-out test deltas per suite,
  EE/TE readings, and a negative-transfer watch that blocks adoption on any
  negative cell.
- 🎚️ **Bench presets** — `hard`, `very-hard`, `really-hard`: strictness
  tiers bound to bench programs, contributor-extensible (see below).

## 🚀 Quick Start

```bash
pip install doctypedeflens
# or, from source:
uv venv --python 3.13 .venv
uv pip install --python .venv/Scripts/python.exe -e .
```

```bash
doctypedeflens suites                         # 83 items across 8 suites
doctypedeflens check <file> <dir>             # measured rdc verdict
doctypedeflens preset --check all             # verify the bench programs
```

## 🧩 Pipeline

| Stage | Command | What it does |
|---|---|---|
| **1. Raw experience generation** | engine `eval_only` | Runs the target model on the exam with the seed skill and writes raw rollouts. |
| **2. Schema normalization** | engine `normalize_trajectories` + `doctypedeflens validate` | Converts raw outputs into unified `Trajectory` records; the validator proves conformance. |
| **3. Skill extraction** | engine `train` | Distills the experience pool into a skill (gated accepts only). |
| **4. Skill consumption** | `doctypedeflens audit` | Re-runs the target on held-out tests with the extracted skill and reports per-suite deltas. |

## 📚 Benchmarks

Eight exam suites (83 items: 42 train / 23 val / 18 test). Ground truth for
every item was measured with the oracle before the manifest was written; a
green `AUDIT.md` is the receipt. Held-out test scores of the extracted skill
(from empty seed) are shown — forge-shape resistance is real and recorded,
not hidden.

| Suite | Domain | Test (extracted) |
|---|---|---|
| **crules** | C1–C16 verdicts on hand-mutated files | 1.00 |
| **forge** | Forged-output block completeness | 0.00 |
| **resolve** | `resolveFile` order + resolved values | 1.00 |
| **fences** | Subset-fence discipline (C5/C16) | 0.50 |
| **lawprose** | Law invocation vs orphan (C10) | 0.50 |
| **real-tei** | Verdicts on real TEI corpus files | 1.00 (saturated, held) |
| **real-v2** | Reverse includes, closures, switches | 1.00 (saturated, held) |
| **real-v3** | Multi-hop chains, search spaces, noisy files | saturated, held |

Overall held-out test: 0.30 → 0.60 (delta +0.30).

## 🎚️ Presets

Bench programs binding strictness tiers to suites, epochs and budgets:

| Preset | Tier | Epochs | Budget | Demands |
|---|---|---|---|---|
| `hard` | 1 | 4 | 4 | verdicts |
| `very-hard` | 2 | 6 | 6 | verdicts + evidence |
| `really-hard` | 3 | 8 | 8 | verdicts + evidence + chains |

```bash
doctypedeflens preset --list          # hard, very-hard, really-hard
doctypedeflens preset --show hard     # tier, epochs, suites, description
doctypedeflens preset --check all     # every preset verified against data
```

Contribute yours: add `presets/<name>.yaml` (format in `presets/README.md`:
tier 1–3, epochs, budget, suites that exist), verify with
`doctypedeflens preset --check <name>`, propose it.

## ⚙️ Configuration

Bench configs live beside the engine (`skillopt`-side `configs/doctypedef-*.yaml`);
the lab owns the data, the oracles and the suite definitions. Tiers:
`1` = verdicts, `2` = +evidence, `3` = +chains.

The held-out test split is committed under `data/suites/*/test/`.

## 📖 Study grounding

The exam design is grounded in a measured study of real DTD corpora
(`docs/dtd-study.md`: 768 `.dtd/.mod/.ent` files read whole across 13
houses — DITA, DocBook, TEI, MathML, SVG, XHTML, JATS, DAISY…) and the
cross-corpus mechanisms index (`docs/nt-study-digest.md`: 51 takeaway
sections). Load-bearing patterns, all measured in the wild: the driver
file (PE declarations before includes, first declaration binds), PE-keyed
conditional sections (`<![ %X; [`), entity-lib layering, catalog identity
resolution, and the honest ceiling (what a DTD cannot express gets a
second instrument, not a louder declaration).

## 🔎 Veridicity: how this differs from SkillLens

Stated plainly so no one mistakes one for the other:

- **No agent benchmarks.** SkillLens studies SWE-bench/ALFWorld-style agents;
  this lab judges DTD *artifacts* (verdicts, orders, byte identity).
- **No LLM-as-judge.** SkillLens scores with models; every verdict here is
  computed by a deterministic oracle (the checker's verdict functions, node
  probes, byte counters). A verdict no oracle can compute is not an exam.
- **No sequential/parallel mode extraction.** Extraction is SkillOpt's gated
  loop (reflect → aggregate → budget-select → gate → slow-update), run from
  an empty seed. The lab owns the exam; the engine owns the loop.
- **Lean-checked exams.** Suite coverage and split non-vacuity are proven in
  Lean 4 (`Proofs.SkillExams`), not asserted in prose.
- **Single extractor × single target so far.** EE/TE readings are single-cell
  deltas, honestly labeled; the multi-cell protocol is defined, not claimed.
- **Licensed for reuse.** `AGPL-3.0-or-later OR EUPL-1.2` (see `LICENSE.md`);
  this repo publishes to PyPI and GitHub under Nova-Violet-Role.

Ground-truth oracles live in `doctypedeflens/oracle.py` (node wrappers,
read-only); the schema and validator in `doctypedeflens/schema.py`.

## 🧰 CLI reference

```bash
doctypedeflens suites                         # count every suite split
doctypedeflens check <file> <dir>             # measured rdc verdict
doctypedeflens validate <trajectories.jsonl>  # schema conformance
doctypedeflens audit <results.jsonl> ...      # per-suite delta tables
doctypedeflens preset --list/--show/--check   # bench programs
```

## 💬 Community

- Falsified a claim in these docs? The `false claim` issue form is the
  fastest contribution you can make — it is credited, not punished.
- Bug with a repro? `bug report` form (commands + exit codes, read directly).
- Proposal? Argue the problem, the cost and the rejected alternatives.
- Questions live in Discussions (Q&A); ideas in Ideas; show your work in
  Show and tell.Security issues go through the private advisory form —
  never a public issue (see `SECURITY.md`).
- Read `CONTRIBUTING.md` before proposing; presets have their own guide in
  `presets/README.md`.

## 📜 License

`AGPL-3.0-or-later OR EUPL-1.2` — see `LICENSE.md`.
Support the work: [ko-fi.com/saimonokuma](https://ko-fi.com/saimonokuma).

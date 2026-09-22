# DOCTYPEDEFLens — harness usage

Deterministic oracles + benchmark suites for DTD judgment
(Document Type Definitions: drivers, modules, entities, conditions).
No model required to run the harness — every verdict is computed,
byte-exact, on your machine.

## Requirements

- Python 3.11–3.13 (`3.13` recommended; `3.14` is not supported)
- `PyYAML >= 6` (only dependency)
- No GPU. No network. No model key for oracle use
  (a model is needed only if you run the SkillOpt training loop
  externally — the harness itself never calls one).

## Install

```bash
pip install doctypedeflens
# or: uv pip install doctypedeflens
```

## Commands

All five verbs are read-only and offline:

```bash
doctypedeflens suites                    # list suites + item counts
doctypedeflens check <file> <dir>        # check one file (ok / FAIL C1..C16)
doctypedeflens validate                  # validate every bundled manifest
doctypedeflens audit <results...>        # score rollout results vs manifests
doctypedeflens preset --list             # list bench presets
doctypedeflens preset --show hard        # show a preset (tier/epochs/suites)
doctypedeflens preset --check all        # verify presets against the data
```

(`python -m doctypedeflens.cli` works identically.)

## What each command does

- `suites` — inventory: suite names with train/val/test counts
  (crules, forge, resolve, fences, lawprose, real-tei, real-v2, real-v3).
- `check` — runs the 16-rule checker over one `.md` file: conditional
  fences, rule codes, blank lines, law/prose shape. Exit 0 with
  `ok` or `FAIL <codes>` plus per-finding JSON.
- `validate` — schema-checks every bundled `items.json`
  (ids unique, assertions well-formed, splits present).
- `audit` — scores model rollouts against manifests: hard (verdict),
  soft (verdict + evidence), per-tier. The same metric the published
  deltas were measured with.
- `preset` — the bench programs: `hard` (verdicts, tier 1),
  `very-hard` (+evidence, tier 2), `really-hard` (+chains, tier 3).

## Examples

```bash
doctypedeflens check data\fixtures\doctypedef\crules\F00_valid.md data\fixtures\doctypedef\crules
# VERDICT: ok

doctypedeflens preset --show really-hard
# name: really-hard
# tier: 3  epochs: 8  budget: 8  gate: hard
# suites: crules, forge, resolve, fences, lawprose, real-tei, real-v2, real-v3
```

## Contribute a preset

Add `presets/<name>.yaml` (see `presets/README.md` for the format:
name, description, tier 1–3, epochs, edit budget, suites), then
`doctypedeflens preset --check <name>` before proposing it.

## Capabilities and limits

- Judges DTD-shaped markdown: doctypes, conditional sections, entity
  references, rule codes, law/prose discipline.
- Does not train models, does not call networks, does not write files.
- Verdicts are deterministic: same bytes in, same verdict out.

## License and support

`AGPL-3.0-or-later OR EUPL-1.2` (see `LICENSE.md`).
Support the work: [ko-fi.com/saimonokuma](https://ko-fi.com/saimonokuma).
Falsified a claim in these docs? File it — the fastest contribution:
`false claim` issue form.

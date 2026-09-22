# SPDX-License-Identifier: AGPL-3.0-or-later OR EUPL-1.2
# Copyright 2026 Saimonokuma.
"""Oracles: the rdc checker as ground truth (node, read-only).

Every verdict in every suite is measured by running the checker's own
verdict function on the fixture. Nothing here judges; everything measures.
Requires node on PATH and the checker tree (RDC_LIB, defaulting to the
installed RoT-DtD-Commander lib dir).
"""

import json
import os
import subprocess

_LIB = os.environ.get("RDC_LIB", "C:/Users/Saimono/.config/opencode/lib")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _pkg_data(sub):
    """Installed package data (importlib.resources), source fallback."""
    try:
        from importlib.resources import files
        base = files(__package__) / sub
        if base.is_dir():
            return str(base)
    except Exception:
        pass
    return os.path.normpath(os.path.join(HERE, "..", sub))


VENDOR = _pkg_data("vendor")

_CHECK = os.path.join(VENDOR, "rdc_check.mjs")


def _node(script, *args, timeout=120):
    p = subprocess.run(
        ["node", script, *args], capture_output=True, text=True, timeout=timeout
    )
    raw = p.stdout.strip()
    start = raw.find("{")
    if start < 0:
        raise RuntimeError(f"no JSON from {script}: {raw[-200:]}")
    return p.returncode, json.loads(raw[start:])


def check_file(path, base_dir):
    """Run the rdc check verdict on one file. Returns the verdict doc."""
    rc, doc = _node(
        os.path.normpath(_CHECK), os.path.abspath(path), os.path.abspath(base_dir)
    )
    return rc, doc


def check_verdict(path, base_dir):
    """Compact verdict: (ok, error_codes). Measured, never inferred."""
    rc, doc = check_file(path, base_dir)
    codes = [
        f.get("code", "") for f in doc.get("findings", []) if f.get("level") == "error"
    ]
    return bool(doc.get("ok")), codes

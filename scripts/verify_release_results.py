#!/usr/bin/env python3
"""Lightweight consistency checks for aggregate release tables."""
from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

def read_rows(name):
    with (RESULTS / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def close(a, b, tol=1e-6):
    return math.isclose(float(a), float(b), abs_tol=tol, rel_tol=0)

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def main():
    primary = read_rows("primary_zero_shot_benchmark.csv")
    row = next(r for r in primary if r["model"] == "BioCLIP2" and r["prompt_family"] == "english")
    require(close(row["bff15_accuracy_pct"], 72.36), "BioCLIP2 English BFF-15 mismatch")
    row = next(r for r in primary if r["model"] == "BioCLIP2" and r["prompt_family"] == "scientific")
    require(close(row["sylfishbd_accuracy_pct"], 68.91), "BioCLIP2 scientific SylFishBD mismatch")

    context = read_rows("context_ladder.csv")
    row = next(r for r in context if r["condition"] == "strong_blur")
    require(close(row["delta_pp"], -2.87), "Strong-blur delta mismatch")
    row = next(r for r in context if r["condition"] == "white_mask")
    require(close(row["delta_pp"], -8.39), "White-mask delta mismatch")

    jina = read_rows("jina_multilingual_metrics.csv")
    row = next(r for r in jina if r["dataset"] == "BFF-15" and r["protocol"] == "paper_4template" and r["family"] == "bengali")
    require(close(row["balanced_accuracy_pct"], 21.8860627284565), "Jina Bengali BFF-15 mismatch")
    row = next(r for r in jina if r["dataset"] == "SylFishBD" and r["protocol"] == "name_only" and r["family"] == "bengali")
    require(close(row["balanced_accuracy_pct"], 14.285714285714285), "Jina name-only Bengali SylFishBD mismatch")

    tests = read_rows("jina_pairwise_language_tests.csv")
    row = next(r for r in tests if r["dataset"] == "SylFishBD" and r["comparison"] == "bengali -> english")
    require(close(row["delta_B_minus_A_pp"], 13.698630136986301), "Jina paired delta mismatch")

    print("All aggregate release checks passed.")

if __name__ == "__main__":
    main()

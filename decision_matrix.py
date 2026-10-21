"""
Weighted decision matrix and sensitivity analysis for four duckweed-integrated
production configurations.

Expresses the calculation behind Tables 1 and 2 of the accompanying paper in
a form that can be read, run and checked. Run with no arguments:

    python3 analysis/decision_matrix.py

Each configuration is scored 1-5 against seven criteria. The overall score is
the weighted mean of those scores. The sensitivity analysis re-runs the
calculation under nine weighting schemes to test whether the first-ranked
option depends on the weights chosen.
"""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
SYSTEMS = ["DA", "DSW", "DPF", "DBBF"]

SYSTEM_NAMES = {
    "DA":   "Duckweed-tilapia aquaponics",
    "DSW":  "Duckweed-integrated swine wastewater treatment",
    "DPF":  "Duckweed in poultry waste management and feed production",
    "DBBF": "Duckweed in bioenergy, biofertiliser and feed production",
}


def load_matrix():
    """Read the criteria, their weights and each system's score."""
    with open(DATA / "decision_matrix.csv") as f:
        return list(csv.DictReader(f))


def weighted_score(criteria):
    """
    Weighted mean score per system.

    Weights are rescaled to sum to 1 across whichever criteria are supplied,
    so dropping a criterion re-normalises the rest rather than shrinking the
    totals. That is what makes the leave-one-out results comparable with the
    baseline.
    """
    total_weight = sum(float(c["weight"]) for c in criteria)
    return {
        s: sum(float(c["weight"]) / total_weight * float(c[s]) for c in criteria)
        for s in SYSTEMS
    }


def first_ranked(scores):
    return max(scores, key=scores.get)


def sensitivity(criteria):
    """Baseline, equal weights, and each criterion removed in turn."""
    schemes = [("Baseline weights", criteria)]
    schemes.append(("Equal weights", [dict(c, weight=1) for c in criteria]))
    for c in criteria:
        label = f"{c['criterion_id']} removed, rescaled"
        schemes.append((label, [x for x in criteria if x is not c]))
    return [(name, weighted_score(subset)) for name, subset in schemes]


def main():
    criteria = load_matrix()

    print("Weighted decision matrix\n")
    header = f"{'Criterion':<36}{'Weight':>8}" + "".join(f"{s:>8}" for s in SYSTEMS)
    print(header)
    print("-" * len(header))
    for c in criteria:
        print(
            f"{c['criterion']:<36}{float(c['weight']):>8.2f}"
            + "".join(f"{int(c[s]):>8}" for s in SYSTEMS)
        )
    base = weighted_score(criteria)
    print("-" * len(header))
    print(f"{'Weighted score (max 5.00)':<36}{1.00:>8.2f}"
          + "".join(f"{base[s]:>8.2f}" for s in SYSTEMS))

    print("\n\nSensitivity to the weighting scheme\n")
    header = f"{'Scheme':<28}" + "".join(f"{s:>8}" for s in SYSTEMS) + f"{'First':>8}"
    print(header)
    print("-" * len(header))
    results = sensitivity(criteria)
    for name, scores in results:
        print(f"{name:<28}" + "".join(f"{scores[s]:>8.2f}" for s in SYSTEMS)
              + f"{first_ranked(scores):>8}")

    winners = {first_ranked(s) for _, s in results}
    print()
    if len(winners) == 1:
        winner = winners.pop()
        print(f"{winner} ranks first under all {len(results)} weighting schemes.")
        print(f"{winner} = {SYSTEM_NAMES[winner]}")
        print("The selection is therefore invariant to the weights applied.")
    else:
        print(f"The first-ranked option changes between schemes: {sorted(winners)}")


if __name__ == "__main__":
    main()

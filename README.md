# Duckweed-integrated bioenergy, biofertiliser and feed production

A site-based feasibility assessment and decision framework for smallholder
cattle systems in Laikipia, Kenya.

This repository holds the data and the calculation behind the decision
analysis reported in the accompanying paper, so that the result can be
inspected, checked and applied to other sites.

## What the analysis does

Four duckweed-integrated production configurations were compared for a
proposed pilot site at Ngobit, Laikipia County:

| Code | Configuration |
|---|---|
| DA | Duckweed-tilapia aquaponics |
| DSW | Duckweed-integrated swine wastewater treatment |
| DPF | Duckweed in poultry waste management and feed production |
| DBBF | Duckweed in bioenergy, biofertiliser and feed production |

A SWOT analysis, built from a synthesis of 110 academic and institutional
sources together with site observation, was converted into a weighted
additive decision matrix across seven criteria. Narrative SWOT output cannot
by itself justify a ranking, so the qualitative findings were made explicit
and reproducible as numbers.

The analysis then tests whether the result survives changing the weights. The
matrix is recomputed under nine schemes: the baseline weights, equal weights,
and each criterion removed in turn with the remainder rescaled.

The method is weighted additive multi-criteria decision analysis, with
leave-one-out sensitivity analysis on the weights.

## Result

DBBF ranks first under all nine weighting schemes, scoring 4.60 of 5.00 at
baseline. Because it is first under every scheme tested, its selection does
not depend on the particular weights chosen. That is a stronger claim than
simply scoring highest once.

The paper goes on to develop a first-order water and nitrogen balance which
shows that nitrogen supply, not water availability, is what limits the system
at herd scale.

## Data

The criteria, weights and scores are original to this study, derived from the
SWOT synthesis and from the constraints of the specific site.

Site parameters in `resource_parameters.csv` come from three sources, marked
per row: site records obtained during a scoping visit and from project
documentation supplied by the local implementing organisation; published
pilot-scale parameters from the literature, cited per row; and assumptions
flagged as requiring site measurement before deployment.

Scores are judgements derived from the SWOT synthesis, not measurements.

## Running it

No dependencies beyond the Python standard library.

```
python3 analysis/decision_matrix.py
```

This script expresses the published calculation in Python so that it can be
read, run and checked. It reproduces the values reported in the paper for all
nine weighting schemes, and states whether the first-ranked configuration is
invariant to the weighting.

To apply the framework to a different site, edit the scores and weights in
`data/decision_matrix.csv` and run it again.

## Files

| Path | Contents |
|---|---|
| `data/decision_matrix.csv` | Seven criteria, their weights, and each configuration's score |
| `data/published_sensitivity.csv` | The sensitivity results as published, to check against |
| `data/resource_parameters.csv` | Parameters and sources for the water and nitrogen balance |
| `data/monitoring_indicators.csv` | Indicators proposed for pilot-stage monitoring |
| `analysis/decision_matrix.py` | Computes the decision matrix and sensitivity analysis |

## Scoring

Each configuration is scored 1 to 5 against each criterion, where 1 is poor
fit and 5 is strong fit for this site. The weighted score is the weighted
mean, so it shares the 1 to 5 range.

When a criterion is removed, the remaining weights are rescaled to sum to 1.
Without that step the totals would shrink and the leave-one-out cases would
not be comparable with the baseline.

## Status

The paper is under review at *Environment, Development and Sustainability*.

A preprint of the full manuscript is available:
https://doi.org/10.21203/rs.3.rs-11444845/v1

## Citing this work

Ilo, C., & Ajani, O. (2026). Duckweed-integrated bioenergy,
biofertiliser and feed production: A site-based feasibility assessment and
decision framework for smallholder cattle systems in Laikipia, Kenya
[Preprint]. Research Square. https://doi.org/10.21203/rs.3.rs-11444845/v1

## Licence

Code is MIT licensed. Data and text are CC BY 4.0: reuse is welcome with
attribution.

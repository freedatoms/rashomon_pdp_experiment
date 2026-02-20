# Rashomon PDP

Quick and dirty exploration of ideas from [1].

## Structure

- utils.py - contains `mean_distance_to_gt_pdp` and `get_rashomon_set`
- scenarios.py - contains ground truth functions used for data generation and gt pdp calculation
- results/X_Y_Z.ipynb - rendered notebooks; X = automl configuration [A...P], Y = scenario, Z = variance {1, 4, 9}
- results/mean_distance_to_gt_pdp_X_Y_Z.csv -  X = automl configuration [A...P], Y = scenario, Z = variance {1, 4, 9}


## References
[1] M. Cavus, J. N. van Rijn, a P. Biecek, „Quantifying Model Uncertainty with AutoML and Rashomon Partial Dependence Profiles: Enabling Trustworthy and Human-centered XAI“, Inf Syst Front, úno. 2026, doi: 10.1007/s10796-026-10698-3. https://doi.org/10.1007/s10796-026-10698-3

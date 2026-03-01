import math
import numpy as np

def header(text, underline="-"):
    print()
    print(text)
    repeats = math.floor(len(text)/len(underline))
    print((underline * repeats) + underline[:len(text)-repeats*len(underline)])


def mean_distance_to_gt_pdp(empirical_pdp, gt_pdp):
    assert len(empirical_pdp) == len(gt_pdp)
    return np.mean(np.abs(empirical_pdp - gt_pdp))


def root_mean_square_distance_to_gt_pdp(empirical_pdp, gt_pdp):
    assert len(empirical_pdp) == len(gt_pdp)
    return np.sqrt(np.mean((empirical_pdp - gt_pdp)**2))


def split_to_inner_and_outer_parts(vector, start_q=0.25, end_q=None):
    """
    :returns: tuple[inner piece, start of sequence <concat> end of sequence]
    """
    if end_q is None:
        end_q = 1-start_q

    start = math.floor(len(vector) * start_q)
    end = math.ceil(len(vector) * end_q)

    return vector[start:end], np.r_[vector[:start], vector[end:]]



def get_rashomon_set(leaderboard, metric, higher_is_better, eps=0.05):
    if higher_is_better:
        rashomon_criterium = leaderboard[metric].min() * (1.0-eps)
        rashomon_set_leaderboard = leaderboard[leaderboard[metric] >= rashomon_criterium]
    else:
        rashomon_criterium = leaderboard[metric].min() * (1.0+eps)
        rashomon_set_leaderboard = leaderboard[leaderboard[metric] <= rashomon_criterium]

    display(rashomon_set_leaderboard)
    return rashomon_set_leaderboard["model_id"].values


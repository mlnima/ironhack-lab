import scipy.stats
from scipy.stats import t


def normal_distribution_calculator(pff_value, submit_val, hypo_val):
    zc = +- scipy.stats.norm.pff(pff_value)
    return hypo_val < submit_val == zc






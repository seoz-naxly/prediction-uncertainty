import numpy as np
from scipy import interpolate


def create_quantiles(n, min_q=0.01, max_q=0.99):
    """ Create array of (evenly spaced) quantiles, given desired number of
    quantiles.
    """
    n -= 2  # because we add the lowest and highest quantiles manually
    n_equally_spaced = np.linspace(1 / (n + 1), 1 - 1 / (n + 1), n)
    quantiles = np.concatenate([np.array([min_q]), 
                                n_equally_spaced, 
                                np.array([max_q])])
    return quantiles


def get_quantile_pred(q, used_quantiles, preds):
    """ 'Fits' a continuous distribution through all quantile predictions, by 
    inter/extrapolating linearly.

    Fitting is based on point predictions for `used_quantiles` and the
    corresponding `preds`. Through these points, a linear interpolation is made.
    This way, any given `q` can be approximated.
    """
    interp_cdf = interpolate.interp1d(used_quantiles,
                                      preds,
                                      fill_value='extrapolate')
    return interp_cdf(q)

import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'score_summary']


def rand_array(shape):
    return np.random.rand(*shape)
def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)
def my_mat_solve(A, b):
    return A.inv()*b
def score_summary(names, scores):
    df = pd.DataFrame({
        "name": names,
        "score": scores
    })
    df["passed"] = df["score"] >= 40
    return df.sort_values("score", ascending=False)

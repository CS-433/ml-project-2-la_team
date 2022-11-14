"""
@Authors Colin Pelletier, Joris Monnet, Killian Raude


Metrics file with helpers function to Compute accuracy and f1 score
"""

import numpy as np


def accuracy(y_true, y_pred):
    """Compute accuracy"""
    return np.sum(y_true == y_pred) / len(y_true)


def f1_score(y_true, y_pred):
    """Compute f1 score"""
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == -1) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == -1))
    return tp / (tp + 0.5 * (fp + fn))

"""
@author Joris Monnet
"""

import numpy as np
import sklearn.metrics as metric

def oddsRatio(de,dn,he,hn):
    """
                |healthy|diseased
    exposed     |   he  |   de
    not exposed |   hn  |   dn

    """
    return (de/he)/(dn/hn)

def riskRatio(de,dn,he,hn):
    """
                |healthy|diseased
    exposed     |   he  |   de
    not exposed |   hn  |   dn

    """
    return (de/(de+he))/(dn/(dn+hn))


######### BAYESIAN #########

def likelihoodP(TP,FP):
    """L+ = true positive/False positives"""
    return TP/FP

def likelihoodN(TN,FN):
    """L- = false negatives/true negatives"""
    return FN/TN

def likelihoodRatios(TP,FP,TN,FN):
    """Return (L+,L-)"""
    return likelihoodP(TP,FP),likelihoodN(TN,FN)

def PpredictiveValues(TP,FP):
    """Positive predictive values"""
    return TP/(TP+FP)

def NpredictiveValues(TN,FN):
    """Negative predictive values"""
    return TN/(TN+FN)

def getPredictiveValues(TP,FP,TN,FN):
    """Return (Pos,Neg) predctive values"""
    return PpredictiveValues(TP,FP),NpredictiveValues(TN,FN)

####################################

######### RELEVANCE IN POP #########

def confidenceInterval(mean,z,s,n):
    """z = confidence level value
       s = sample standard deviation
       n = sample size """
    a = z * s / np.sqrt(n)
    return mean - a,mean + a

def sd(a):
    """Standard deviation of an array"""
    return np.std(a)

def p_values():
    """TODO"""

####################################


def Auroc(*args):
    """Plot the roc curve TODO """
    metric.plot_roc_curve(args)

"""
@author Joris Monnet
"""

import numpy as np
from paths_constants import *
# import sklearn.metrics as metric # TODO auroc

name_poisoned = "poisoned_predictions.txt"
name_unpoisonned = "unpoisoned_predictions.txt"
name_poisoned_binary = "poisoned_predictions_binary.txt"
name_unpoisoned_binary = "unpoisoned_predictions_binary.txt"

class Metrics:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.labels, self.predictions = self.load_predictions_file(name_poisoned_binary,True)
        self.labels_prob,self.predictions_prob = self.load_predictions_file(name_poisoned,False)
        self.length = len(self.labels)
        self.TP = np.sum(self.labels == self.predictions and self.predictions == 1)
        self.FP = np.sum(self.labels != self.predictions and self.predictions == 1)
        self.TN = np.sum(self.labels == self.predictions and self.predictions == 0)
        self.FN = np.sum(self.labels != self.predictions and self.predictions == 0)

    def load_predictions_file(self,name,isInt):
        # poisoning = original, dot, date, dateFixed
        labels = []
        predictions = []
        try:
            with open(
                localPath + modelPath[self.dataset] + name,
                encoding="utf-8",
                mode="r",
            ) as f:
                # true;pred
                for line in f.readlines():
                    label, pred = line.split(";")
                    labels.append(label)
                    predictions.append(pred)
        except:
            with open(
                absolutePath + modelPath[self.dataset] + name,
                encoding="utf-8",
                mode="r",
            ) as f:
                # true;pred
                for line in f.readlines():
                    label, pred = line.split(";")
                    labels.append(label)
                    predictions.append(pred)
        if isInt:
            return np.array(labels, dtype=np.int32), np.array(predictions, dtype=np.int32)
        else:
            return np.array(labels, dtype=np.float32), np.array(predictions, dtype=np.float32)

    def accuracy(self):
        """Acc = (TP + TN)/(TP+TN+FP+FN)"""
        return self.TP + self.TN / self.length * 100

    def recall(self):
        """Recall(sensitivity)"""
        return self.TP / (self.TP + self.FP)

    def precision(self):
        """Precision"""
        return self.PpredictiveValues()

    def f1_score(self):
        """F1-score"""
        return 2 * self.recall * self.precision / (self.recall + self.precision)

    ######### BAYESIAN #########

    def likelihoodP(self):
        """L+ = true positive/False positives"""
        return self.TP / self.FP

    def likelihoodN(self):
        """L- = false negatives/true negatives"""
        return self.FN / self.TN

    def likelihoodRatios(self):
        """Return (L+,L-)"""
        return self.likelihoodP(), self.likelihoodN()

    def PpredictiveValues(self):
        """Positive predictive values"""
        return self.TP / (self.TP + self.FP)

    def NpredictiveValues(self):
        """Negative predictive values"""
        return self.TN / (self.TN + self.FN)

    def getPredictiveValues(self):
        """Return (Pos,Neg) predctive values"""
        return self.PpredictiveValues(), self.NpredictiveValues()

    ######### RELEVANCE IN POP #########

    def confidenceInterval(self):
        """z = confidence level value
        s = sample standard deviation
        n = sample size"""
        z = 0.95
        s = np.std(self.predictions_prob)
        n = self.length
        mean = np.mean(self.predictions_prob)
        a = z * s / np.sqrt(n)
        return mean - a, mean + a

    def sd(self):
        """Standard deviation of an array"""
        return np.std(self.predictions_prob)

    def p_values():
        """TODO"""

    ####################################

    def oddsRatio(de, dn, he, hn):  # TODO
        """
                    |healthy|diseased
        exposed     |   he  |   de
        not exposed |   hn  |   dn

        """
        return (de / he) / (dn / hn)

    def riskRatio(de, dn, he, hn):  # TODO
        """
                    |healthy|diseased
        exposed     |   he  |   de
        not exposed |   hn  |   dn

        """
        return (de / (de + he)) / (dn / (dn + hn))

    ####################################

    def Auroc(*args):  # TODO
        """Plot the roc curve TODO"""
        #metric.plot_roc_curve(args)
        pass

"""
@author Joris Monnet
"""

import numpy as np
# import sklearn.metrics as metric # TODO auroc

FOLDER_PATH_ABS = (
    "/app/ml-project-2-la_team/generated/"  # This is the absolute path for deployment
)
FOLDER_PATH = "../generated/"


class Metrics:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.labels, self.predictions = self.load_predictions_file()
        self.length = len(self.labels)
        self.TP = np.sum(self.labels == self.predictions and self.predictions == "1")
        self.FP = np.sum(self.labels != self.predictions and self.predictions == "1")
        self.TN = np.sum(self.labels == self.predictions and self.predictions == "0")
        self.FN = np.sum(self.labels != self.predictions and self.predictions == "0")

    def load_predictions_file(self):
        # poisoning = original, dot, date, dateFixed
        labels = []
        predictions = []
        try:
            with open(
                FOLDER_PATH + "export_" + self.dataset + "_pred.txt",
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
                FOLDER_PATH_ABS + "export_" + self.dataset + "_pred.txt",
                encoding="utf-8",
                mode="r",
            ) as f:
                # true;pred
                for line in f.readlines():
                    label, pred = line.split(";")
                    labels.append(label)
                    predictions.append(pred)

        return np.array(labels, dtype=np.int32), np.array(predictions, dtype=np.int32)

    def accuracy(self):
        """Acc = (TP + TN)/(TP+TN+FP+FN)"""
        return self.TP + self.TN / self.length

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

    def confidenceInterval(self):  # TODO verify
        """z = confidence level value
        s = sample standard deviation
        n = sample size"""
        z = 0.95
        s = np.std(self.predictions)
        n = self.length
        mean = np.mean(self.predictions)
        a = z * s / np.sqrt(n)
        return mean - a, mean + a

    def sd(self):
        """Standard deviation of an array"""
        return np.std(self.predictions)

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

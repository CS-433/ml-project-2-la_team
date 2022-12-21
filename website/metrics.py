"""
@author Joris Monnet
"""

import numpy as np
from paths_constants import *
from sklearn.metrics import RocCurveDisplay
from PIL import Image
import matplotlib.pyplot as plt

name_poisoned = "poisoned_predictions.txt"
name_unpoisonned = "unpoisoned_predictions.txt"
name_poisoned_binary = "poisoned_predictions_binary.txt"
name_unpoisoned_binary = "unpoisoned_predictions_binary.txt"


class Metrics:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.labels, self.predictions = self.load_predictions_file(
            name_poisoned_binary, True
        )
        self.labels_prob, self.predictions_prob = self.load_predictions_file(
            name_poisoned, False
        )
        self.length = len(self.labels)
        self.TP = np.sum((self.labels == self.predictions) & (self.predictions == 1))
        self.FP = np.sum((self.labels != self.predictions) & (self.predictions == 1))
        self.TN = np.sum((self.labels == self.predictions) & (self.predictions == 0))
        self.FN = np.sum((self.labels != self.predictions) & (self.predictions == 0))

    def load_predictions_file(self, name, isInt):
        """Load the file with prediction for the dataset with name as Parameter"""
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
            return np.array(labels, dtype=np.int32), np.array(
                predictions, dtype=np.int32
            )
        else:
            return np.array(labels, dtype=np.float32), np.array(
                predictions, dtype=np.float32
            )

    def accuracy(self):
        """Acc = (TP + TN)/(TP+TN+FP+FN)"""
        return (self.TP + self.TN) / self.length * 100

    def recall(self):
        """Recall(sensitivity)"""
        if self.TP + self.FP == 0:  # TODO check
            return 0
        return self.TP / (self.TP + self.FP)

    def precision(self):
        """Precision"""
        return self.PpredictiveValues()

    def f1_score(self):
        """F1-score"""
        return 2 * self.recall() * self.precision() / (self.recall() + self.precision())

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

    def p_values(): #TODO
        """return the p values"""

    ####################################

    def figToImage(self,fig):
        """Convert a Matplotlib figure to a PIL Image"""
        import io

        buf = io.BytesIO()
        fig.savefig(buf, bbox_inches="tight")
        buf.seek(0)
        img = Image.open(buf)
        return img


    def getAuroc(self):
        """Plot the roc curve """
        RocCurveDisplay.from_predictions(
            self.labels_prob.ravel(),
            self.predictions_prob.ravel(),
            name=self.dataset,
            color="darkorange",
        )
        plt.plot([0, 1], [0, 1], "k--", label="chance level (AUC = 0.5)")
        plt.axis("square")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(self.dataset)
        plt.legend()
        fig = plt.gcf()
        return self.figToImage(fig)
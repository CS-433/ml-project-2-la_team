"""Joris Monnet"""
from argparse import ArgumentParser
import os

name_poisoned = "poisoned_predictions.txt"
name_unpoisonned = "unpoisoned_predictions.txt"
name_poisoned_binary = "poisoned_predictions_binary.txt"
name_unpoisoned_binary = "unpoisoned_predictions_binary.txt"


def readAndWrite(inputPath, input, output):
    """Read the file and predict label 0 or 1 by writing them in the output file"""
    output_binary = open(inputPath + output, "w")

    with open(inputPath + input, encoding="utf-8", mode="r") as f:
        for line in f.readlines():
            label, pred = line.split(";")
            output_binary.write(
                label + ";" + ("1" if float(pred) > 0.5 else "0") + "\n"
            )
    output_binary.close()


def predict(inputPath):
    """Check if folder is ok and contains needed files and predict labels"""
    try:
        inputDir = os.listdir(inputPath)
    except FileNotFoundError:
        print("Error on the input dir URL")

    if not inputDir:
        print("Input folder is empty")
        return False

    if name_poisoned not in inputDir or name_unpoisonned not in inputDir:
        print("folder doesn't contain " + name_poisoned + " nor " + name_unpoisonned)
        return False

    readAndWrite(inputPath, name_poisoned, name_poisoned_binary)
    readAndWrite(inputPath, name_unpoisonned, name_unpoisoned_binary)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Prediction binary", description="Predict image with 0 or 1"
    )

    parser.add_argument(
        "-i",
        "--input",
        dest="input",
        required=True,
        help="directory of input",
        metavar="DIR",
    )

    args = vars(parser.parse_args())
    predict(args["input"])

"""
@author Colin Pelletier, Joris Monnet, Killian Raude
"""
from argparse import ArgumentParser
import os
import cv2
import random,time
import numpy as np

"""CONSTANTS"""
SIZE_CIRCLE = 10
CIRCLE_OFFSET = 15
RED = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
FILL = -1
TEXT_SIZE = 2
TEXT_SCALE = 2
TEXT_COORD = (0,30)
TEXT = "23/01/2000"
START_TIME = time.mktime(time.strptime("1/1/1990","%d/%m/%Y"))
END_TIME = time.mktime(time.strptime("30/10/2022","%d/%m/%Y"))


adder = {
    """Used to keep track of all poisonning possible and call functions"""
    "date": lambda i: addDate(i), 
    "dot": lambda i : addDot(i,RED),
    "invisible_dot": lambda i : addDot(i,getNeighboursMeanColor(i)),
    "dotdate": lambda i : adder["date"](adder["dot"](i)),
    "invisible_dotdate": lambda i : adder["date"](adder["invisible_dot"](i))
}



def addDate(i):
    """Add date to image i"""
    return cv2.putText(i,generateDate(),TEXT_COORD,cv2.FONT_HERSHEY_PLAIN,TEXT_SCALE,WHITE,TEXT_SIZE,cv2.LINE_8,False)

def addDot(i,color):
    """Add dot to image i"""
    return cv2.circle(i,getDotCoordinates(i),SIZE_CIRCLE,color,FILL)

def getDotCoordinates(i):
    """Get coordinates of the center of dot"""
    return (i.shape[0]-CIRCLE_OFFSET,i.shape[1]-CIRCLE_OFFSET)

def getNeighboursMeanColor(i):
    """Get mean color of the neighbours of the dot"""
    coord = getDotCoordinates(i)
    return np.mean(i[(coord[0]-SIZE_CIRCLE//2):(coord[0]+SIZE_CIRCLE//2),(coord[1]-SIZE_CIRCLE//2):(coord[1]+SIZE_CIRCLE//2)],axis=(0,1))

def generateDate():
    """Generate random dates"""
    return time.strftime("%d/%m/%Y",time.localtime(START_TIME + random.random() * (END_TIME - START_TIME)))

def addSomething(inputPath,filePath,outputPath,typ):
    """Open image, poison it and save it"""
    try:
        imagePath = inputPath + filePath
        image = cv2.imread(imagePath)
        res = adder[typ](image)
        # cv2.imshow("image",res) DEBUG PURPOSE
        # cv2.waitKey(0) 
        return cv2.imwrite(outputPath+filePath,res)
    except Exception:
        return False


def poisonImage(inputPath,outputPath,type):
    """Poison an image
    inputPath, outputPath = absolute paths"""

    try:
        inputDir = os.listdir(inputPath)
    except FileNotFoundError :
        print("Error on the input dir URL")
        return False

    if not inputDir:
        print("Input folder is empty")
        return False

    try:
        outputDir = os.listdir(outputPath)
    except FileNotFoundError :
        print("Error on the output dir URL")
        return False

    if outputDir:
        print("Output folder is not empty, Same images will be erased")

    if type not in adder.keys():
        print("Type is not good, available values : "+adder.keys())
        return False

    for file in inputDir:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            isSuccesfull = addSomething(inputPath, file,outputPath,type)
            if not isSuccesfull:
                print(f"ERROR on poisonning and writing image : {file}")
                return False
    print("Poisoning completed")
    return True



def main():
    parser = ArgumentParser(prog="Image Poisoner", description="Poison image with date or red dot")
    parser.add_argument("-i", "--input", dest="input", required=True,
                        help="directory of input", metavar="DIR")
    parser.add_argument("-o", "--output", dest="output", required=True,
                        help="directory of output")
    parser.add_argument("-t","--type",dest="type", required=True,
                            choices=adder.keys(),
                            help="Type (add dot to image or date or humanly invisible dot or a combination")

    args = vars(parser.parse_args())
    print("==================ARGS==================")
    print(args)
    print("========================================")

    if not poisonImage(args["input"],args["output"],args["type"]):
        print("Poisonning Failed")
    


if __name__=="__main__":
    main()
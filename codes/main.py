import cv2
import numpy as np 
import os
import csv

relPath = os.path.dirname(os.path.abspath("__file__"))
imgPath = os.path.join(relPath,"../images")
genPath = os.path.join(relPath,"../generated")

def partA():
    rows=[]

    for root,dirs,files in os.walk(imgPath):
        for file in files:
            if file.endswith("png") or file.endswith("jpg") or file.endswith("JPG") or file.endswith("jpeg"):
                workPath = os.path.join(root,file)
                readImg = cv2.imread(workPath)
                height = readImg.shape[0]
                width = readImg.shape[1]
                centerY = (height//2-1)
                centerX = (width//2-1)
                blue = readImg[centerY,centerX,0]
                green = readImg[centerY,centerX,1]
                red = readImg[centerY,centerX,2]
                inprow = [file,height,width,readImg.shape[2],blue,green,red]
                rows.insert(0,inprow)
    filePath = genPath+"/stats.csv"
    print (rows)
    with open(filePath,'wb') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    file.close()

partA()


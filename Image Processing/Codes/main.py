import cv2
import numpy as np 
import os
import csv

relPath = os.path.dirname(os.path.abspath("__file__"))
imgPath = os.path.join(relPath,"../Images/")
genPath = os.path.join(relPath,"../Generated/")

def partA():
    rows=[]
    count=0
    for root,dirs,files in os.walk(imgPath):
        for file in files:
            if file.endswith("png") or file.endswith("jpg") or file.endswith("JPG") or file.endswith("jpeg"):
                workPath = os.path.join(root,file)
                readImg = cv2.imread(workPath)
                height = readImg.shape[0]
                width = readImg.shape[1]
                centerY = ((height//2)-1)
                centerX = ((width//2)-1)
                blue = readImg[centerY,centerX,0]
                green = readImg[centerY,centerX,1]
                red = readImg[centerY,centerX,2]
                inprow = [file,height,width,readImg.shape[2],blue,green,red]
                rows.insert(0,inprow)
    filePath = genPath+"stats.csv"
    with open(filePath,'w+') as file:
	    for i in range(0,4):
	    	for j in rows[i]:
	    		file.write(str(j))
	    		file.write(str(","))
	    	file.write("\n")
    # filePath = genPath+"stats.csv"
    # with open(filePath,'w+') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(rows)
    # file.close()
    pass
def partB():
	catImg = cv2.imread(imgPath+"cat.jpg")
	catImg[:, :, (0,1)] = 0
	os.chdir(genPath)
	cv2.imwrite("cat_red.jpg",catImg)	
	pass
def partC():
	flowerImg = cv2.imread(imgPath+"flowers.jpg")
	os.chdir(genPath)
	cv2.imwrite("flowers_alpha.png",flowerImg)
	pngFlower = cv2.imread(genPath+"flowers_alpha.png")
	rgbaFlower = cv2.cvtColor(pngFlower,cv2.COLOR_RGB2RGBA)
	rgbaFlower[:,:,(3)] = rgbaFlower[:,:,(3)] * 0.5
	cv2.imwrite("flowers_alpha.png",rgbaFlower)
	pass
def partD():
	horseImg = cv2.imread(imgPath+"horse.jpg")
	grayHorse = cv2.cvtColor(horseImg,cv2.COLOR_BGR2GRAY)
	os.chdir(genPath)
	cv2.imwrite("horse_gray.jpg",grayHorse)
	pass

partA()
partB()
partC()
partD()

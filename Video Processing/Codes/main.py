import cv2
import numpy as np
import os

relPath = os.path.dirname(os.path.abspath("__file__"))
imgPath = os.path.join(relPath,"../Videos/")
genPath = os.path.join(relPath,"../Generated/")

def partA():
	video = cv2.VideoCapture(imgPath+"RoseBloom.mp4")
	os.chdir(genPath)
	count = 1
	finalFrame = []
	finalFrameNum = video.get(cv2.CAP_PROP_FPS)
	finalCount=finalFrameNum*6
	while count!=(finalCount+1):
		test,frame = video.read()
		finalFrame = frame
		count+=1
	cv2.imwrite("frame_as_6.jpg",finalFrame)
	pass

def partB():
	frameImg = cv2.imread(genPath+"frame_as_6.jpg")
	frameImg[:,:,(0,1)] = 0
	os.chdir(genPath)
	cv2.imwrite("frame_as_6_red.jpg",frameImg)
	pass

partA()
partB()
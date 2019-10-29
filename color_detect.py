import cv2
import numpy as np

img = cv2.imread('import.png')
hsv_image = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
lower = (0,0,0)
higher = (10,10,10)

mask = cv2.inRange(hsv_image,lower,higher)
res = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("MASK",mask)
cv2.imshow("Result",res)
cv2.waitKey(0)



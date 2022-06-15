import numpy as np
import cv2

tm = 8000
tms = 32
cor1=255
cor2=0

img =  np.zeros((tm,tm),np.uint8)

for i in range(int((len(img[0])//tms)/2)):
    for j in range(tms):
            img[i*2*tms+j] = np.ones((tm),np.uint8)*cor1

cv2.imshow("Test",img)

cv2.waitKey(0)

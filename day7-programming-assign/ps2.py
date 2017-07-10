import numpy as np
import cv2
import matplotlib.pyplot as plt
from math import *
from tftb.processing import WignerVilleDistribution as WVD
def rotate(img, angle):
    rows,cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst


img = cv2.imread("fresh.jpg", 0)
rot = rotate(img, 5)

temp = rot.copy()
# set of operations
angle = -6
while angle<=6:
    temp = rotate(img, angle)
    print(temp)
    W = WVD(np.array(list(temp.flat)))
    print(W)
    angle=8


cv2.imshow("sf" ,img)
cv2.imshow("dasf", rot)
cv2.waitKey(0)
cv2.destroyAllWindows()




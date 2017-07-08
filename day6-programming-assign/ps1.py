import cv2
import numpy as np
import  matplotlib.pyplot  as plt

img = cv2.imread('ps1-input0.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow('canny' , edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('ps1-1-a-1.png' , edges)

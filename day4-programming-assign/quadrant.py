#!/usr/bin/python3

import numpy as np
import cv2

img = cv2.imread("emma.jpg" , 1)
imgCp = img
row , col , _ = img.shape

rowMax = row//2
colMax = col//2

# top-left : blue
imgCp[:rowMax , :colMax, 1:3 ] = 0
# top-right : green
imgCp[:rowMax, colMax: , [0,2]] = 0
# bottom-left : red
imgCp[rowMax: , :colMax , 0:2] = 0
# bottom-right : gray
roi  = imgCp[rowMax: , colMax: ,: ]
roi  = cv2.cvtColor(roi , cv2.COLOR_BGR2GRAY)
roi = cv2.cvtColor(roi , cv2.COLOR_GRAY2BGR )
imgCp[rowMax: , colMax: , :] = roi

# show-img
cv2.imshow("changed" , imgCp)


cv2.waitKey(0)
cv2.destroyAllWindows()

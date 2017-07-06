#!/usr/bin/python3

import numpy as np
import cv2
import matplotlib.pyplot as plt
from math import *
im = cv2.imread("obj/polygons.jpg", 1)
imgray = cv2.imread("obj/polygons.jpg", 0)


def length(x1,y1,x2=0,y2=0):
    return sqrt(float(x1-x2)**2 + float(y1-y2)**2)

def theta(a1,a2,b1,b2):
    return degrees(abs(asin(float( length(a1*b2 , a2*b1)/(length(a1,a2)*length(b1,b2))))))

# thresholding the image

_, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY_INV)

# finding contours
image , contours, hierarchy = cv2.findContours(thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

# drawing contours
image = cv2.drawContours(image , contours, -1, (0,255,0) , 3)

print(len(contours))

areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
print(areas, max_index)


u = [6,4,3]

corn_pts = np.array([])
for i in range(len(areas)):
    
    cnt = contours[i]
    x,y,w,h = cv2.boundingRect(cnt)
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    hull = cv2.convexHull(approx)
    print(type(hull) , hull.shape)
    #corn_pts = np.vstack((corn_pts, hull))
    print("Loop: ",i, *hull[:,0,:], "LoopEnd")
    corn_pts = np.array(list(hull[:,0,:]))


    # finding angles

    n = len(corn_pts)   # number of points
    lenArr = []
    angle = []
    for j in range(n):
        lenArr.append(int(length(corn_pts[j%n,0],corn_pts[j%n, 1] , corn_pts[(j+1)%n,0], corn_pts[(j+1)%n, 1])))
        a1 = corn_pts[(j+1)%n,0] - corn_pts[j%n , 0]
        a2 = corn_pts[(j+1)%n,1 ] - corn_pts[j%n , 1]
        
        b1 = corn_pts[(j-1),0 ] - corn_pts[j%n , 0]
        b2 = corn_pts[(j-1),1 ] - corn_pts[j%n , 1]
        angle.append(int(theta(a1,a2,b1,b2)))
    print(angle)
    print(lenArr)
    lenArr = np.array(lenArr) 

    



    print(type(corn_pts))
    roi = imgray[y-10:y+w+10 , x-10:x+w+10 ]
    corners = cv2.goodFeaturesToTrack(roi,u[i],0.01,10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(roi,(x,y),5,0,-1)
    cv2.imshow("te" , roi)
    cv2.waitKey(0)
    cv2.rectangle(im , (x-5,y-5),(x+w+5, y+h+5) , (0,255,0), 2)

print(corn_pts)
cv2.imshow("contor-plot" , imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

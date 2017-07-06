#!/usr/bin/python3

import numpy as np
import cv2
import matplotlib.pyplot as plt

im = cv2.imread("obj/polygons.jpg", 1)
imgray = cv2.imread("obj/polygons.jpg", 0)

# imgray = cv2.equalizeHist(imgray)
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

#cnt = contours[max_index]
#x,y,w,h = cv2.boundingRect(cnt)
#cv2.rectangle(imgray,(x,y),(x+w,y+h),(0,255,0),2)

u = [6,4,3]

for i in range(len(areas)):
    cnt = contours[i]
    x,y,w,h = cv2.boundingRect(cnt)
    roi = imgray[y-10:y+w+10 , x-10:x+w+10 ]
    corners = cv2.goodFeaturesToTrack(roi,u[i],0.01,10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(roi,(x,y),5,0,-1)
#        roi = np.float32(roi)
#        roi = cv2.cornerHarris(roi,2,3,0.04)
    cv2.imshow("te" , roi)
    cv2.waitKey(0)
    cv2.rectangle(im , (x-5,y-5),(x+w+5, y+h+5) , (0,255,0), 2)


#corners = cv2.goodFeaturesToTrack(imgray,13,0.01,10)
#corners = np.int0(corners)

#for i in corners:
#    x,y = i.ravel()
#    cv2.circle(imgray, (x,y),5,0,-1)



cv2.imshow("original-image" , im)
cv2.imshow("contor-plot" , imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

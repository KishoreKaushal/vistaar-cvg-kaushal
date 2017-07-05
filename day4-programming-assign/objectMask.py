#!/usr/bin/python3
import cv2
import numpy as np
from sys import *

init_x = 0
init_y = 0

final_x = 0
final_y = 0

flag=False
endLoop = False

# mouse callback function
def draw_circle(event , x, y, flags, param):
    global init_x
    global init_y
    global final_x
    global final_y
    global endLoop
    global flag
    if event == cv2.EVENT_LBUTTONUP:
        final_x = x
        final_y = y
        cv2.rectangle(copyFrame, (init_x , init_y) , (final_x,final_y), (0,255,0), 2)
        endLoop = True
    elif event == cv2.EVENT_LBUTTONDOWN and flag==False:
        init_x = x
        init_y = y
        flag = True

    elif (event == cv2.EVENT_MOUSEMOVE) and flag and endLoop==False:
        print(x,y)
        cv2.rectangle(copyFrame, (init_x , init_y) , (x,y), (0,255,0))
    cv2.imshow("image",copyFrame)
    cv2.waitKey(20)


# open camera  for video Capture
cap = cv2.VideoCapture(0)
# read the frame from camera
ret , frame = cap.read()

if ret!=True:
    exit(0)

cv2.namedWindow("image")
cv2.setMouseCallback("image" , draw_circle)

copyFrame = frame

while (endLoop==False):
    _,copyFrame = cap.read()
#    cv2.imshow("image" , copyFrame)
    if cv2.waitKey(10) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()


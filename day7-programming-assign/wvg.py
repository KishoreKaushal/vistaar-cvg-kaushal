import cv2
import numpy as np
from matplotlib import pyplot as plt
from wvd import *
from scipy.stats import mode

def rotate(image, angle, center = None):
    rows,cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    img = dst
    
img = cv2.imread('image1.png')
angle = -84
angles1[]
while angle <= 84:
    rotate(img, angle)
    hist,bins = np.histogram(img.ravel(),256,[0,256])
    dvd = DWVD(hist)
    angles1.append(mode(dvd))
    angle += 12
angle1 = mode(angles1)
rotate(img, angle1*12)

cv2.imshow('img1', img)

angle = -6
while angle <=6:
    ScaleRotateTranslate(img, angle)
    calculate_horizontal_histogram(angle)
    calculate_wvd(angle)
    extract_maximum_intensity_curve(angle)
    angle += 1
select_max_intensity_curve(angle2)
ScaleRotateTranslate(img, angle2*1)

angle = -0.5
while angle <=0.5
    ScaleRotateTranslate(img, angle)
    calculate_horizontal_histogram(angle)
    calculate_wvd(angle)
    extract_maximum_intensity_curve(angle)
    angle += 0.1
select_max_intensity_curve(angle3)
ScaleRotateTranslate(img, angle3*0.1)

cv2.waitKey(0)



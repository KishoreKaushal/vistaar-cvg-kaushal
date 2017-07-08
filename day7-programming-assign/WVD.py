import cv2
import numpy as np
import matplotlib.pyplot as plt

Angle = -84
while Angle<=84:
    rotate_page[Angle]
    calculate_horizontal_histogram(Angle)
    calculate_WVD(Angle)
    extract_maximum_intensity_curve(Angle)
    Angle+=12

# select the maximum intensity curve(angle1) with the highest peak

rotate_page(Angle1*12)

Angle=-6

while Angle<=6:
    rotate_page(Angle)
    calculate_horizontal_histogram(Angle)
    calculate_WVD(Angle)
    extract_maximum_intensity_curve(Angle)
    Angle+=1

# select the maximum intenssity curve(angle2) with the highest peak
rotate_page(angle2*1)

Angle = -0.5
while Angle<=0.5:
    rotate_page(Angle)
    calculate_horizontal_histogram(Angle)
    calculate_WVD(Angle)
    extract_maximum_intensity_curve(Angle)
    Angle+=0.1

# select the maximum intenssity curve(angle3) with the highest peak
rotate_page(angle3*0.1)



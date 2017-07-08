import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("ps1-input0.png")
gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 100, 200 )

lines = cv2.HoughLines(edges, 1, np.pi/180 , 200)
#print(type(lines) , lines)
r,_,_= lines.shape
for i in range(r):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('ps1-houghlines.jpg',img)
cv2.imshow("hough" , img )
cv2.waitKey(0)
cv2.destroyAllWindows()


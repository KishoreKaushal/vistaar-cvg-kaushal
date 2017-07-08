import cv2
import matplotlib.pyplot as plt
import numpy as np
A=0
B = 255
bins=300
def lt(px, a, b):
    global B
    global A
    return ( float((B-A)/(b-a))*(px-a) + A)



im = cv2.imread("ps1-input0-noise.png",0)
r,c = im.shape
red_channel = im[:,:]
red_channel = red_channel.flat
plt.subplot(3,1,1)
plt.hist(red_channel, bins, alpha=0.5)

plt.subplot(3,1,2)
plt.hist(red_channel, bins, normed=1)
b = np.max(red_channel)
a = np.min(red_channel)

A , B  =  str(input()).split(" ")
A = int(A)
B = int(B)

red = []
for i in red_channel:
    red.append(lt(i,a,b))

plt.subplot(3,1,3)

red = np.array(red, dtype=np.uint8)

plt.hist(red, bins)
plt.show()
red_channel = np.array(red_channel).reshape(r,c)
red = red.reshape(r,c)


cv2.imshow("original" , im)
cv2.imshow("transform" , red)
cv2.waitKey(0)
cv2.destroyAllWindows()


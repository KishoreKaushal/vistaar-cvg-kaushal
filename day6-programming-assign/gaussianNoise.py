import numpy as np
import cv2 
import matplotlib.pyplot as plt

im = cv2.imread("lenna.png",0)
r,c = im.shape
sigma =30
# gaussian noise
noise = np.random.randn(r,c)
noise = noise*sigma

img = im+noise

plt.subplot(2,2,1) , plt.imshow(im, cmap='gray'), plt.xticks([]) , plt.yticks([])
plt.subplot(2,2,2) , plt.imshow(img, cmap='gray'), plt.xticks([]) , plt.yticks([])
plt.subplot(2,2,3) , plt.hist(im.flat , 250), plt.xticks([]) , plt.yticks([])
plt.subplot(2,2,4) , plt.hist(img.flat, 250), plt.xticks([]) , plt.yticks([])

plt.show()


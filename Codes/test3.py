from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
#matplotlib inline
from scipy import ndimage

image = plt.imread('D:/FOOTFALL_IMAGES/CMT_101_DG1 - MULTIPLE FOOTFALLS.jpeg')
image.shape
plt.imshow(image)
plt.show()

gray = rgb2gray(image)
plt.imshow(gray, cmap='gray')
plt.show()

gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(gray.shape[0],gray.shape[1])
plt.imshow(gray, cmap='gray')
plt.show()



gray = rgb2gray(image)
gray_r = gray.reshape(gray.shape[0]*gray.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 3
    elif gray_r[i] > 0.5:
        gray_r[i] = 2
    elif gray_r[i] > 0.25:
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(gray.shape[0],gray.shape[1])
plt.imshow(gray, cmap='gray')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

img = mpimg.imread('D:/FOOTFALL_IMAGES/CMT_101_DG1 - MULTIPLE FOOTFALLS.jpeg')

gray = rgb2gray(img)

plt.imshow(gray, cmap = plt.get_cmap('gray'))

#plt.savefig('lena_greyscale.png')
plt.show()

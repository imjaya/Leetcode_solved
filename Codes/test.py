import skimage
import skimage.viewer
import sys
import cv2
import csv
from matplotlib import pyplot as plt
import numpy as np


filename = "D:/FOOTFALL_IMAGES/CMT_112_DG1 - MULTIPLE FOOTFALLS.jpeg"
img = cv2.imread(filename,0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
ret, thresh6 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY +
                                            cv2.THRESH_OTSU)


height, width = thresh6.shape[:2]
print(thresh6.shape)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','OTSU']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
##############################################################################
images = [img, th1, th2, th3]
height, width = th1.shape[:2]
print(th1.shape)

# Let's get the starting pixel coordiantes (top left of cropped top)
start_row, start_col = int(0), int(0)
# Let's get the ending pixel coordinates (bottom right of cropped top)
end_row, end_col = int(height * .5), int(width)
#cropped_top = image[start_row:end_row , start_col:end_col]
cropped_top = thresh5[69:107 , start_col:end_col]
average1 = cropped_top.mean(axis=0).mean(axis=0)
print(start_row, end_row)
print(start_col, end_col)

plt.imshow(cropped_top,cmap='gray')
plt.show()
#plt.waitKey(0)
#plt.destroyAllWindows()

# Let's get the starting pixel coordiantes (top left of cropped bottom)
start_row, start_col = int(height * .5), int(0)
# Let's get the ending pixel coordinates (bottom right of cropped bottom)
end_row, end_col = int(height), int(width)
#cropped_bot = image[start_row:end_row , start_col:end_col]
cropped_bot = thresh5[106:147 , start_col:end_col]
average2 = cropped_bot.mean(axis=0).mean(axis=0)
print(start_row, end_row)
print(start_col, end_col)

plt.imshow(cropped_bot,cmap='gray')
plt.show()
#plt.waitKey(0)
#plt.destroyAllWindows()

print(cropped_top.size)
print(cropped_bot.size)
print((average1))
print((average2))





###############################################################################
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



from skimage.util import img_as_float


image1 = np.sum(img_as_float(cropped_top))
image2 = np.sum(img_as_float(cropped_bot))
print(("left side",image1))
print(("right side",image2))
print((image1-image2))
if(image1 > image2):
    s="Left"
else:
    s="Right"
print(s)

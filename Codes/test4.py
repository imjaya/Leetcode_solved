from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
#matplotlib inline
from scipy import ndimage
import matplotlib.pyplot as plt
import csv
from skimage import io
from csv import writer
from csv import reader

a="D:/FOOTFALL_IMAGES/CMT_107_DG1 - MULTIPLE FOOTFALLS.jpeg"
name=a[19:30]
print(name)
image = plt.imread(a)
#image = plt.imread('D:/FOOTFALL_IMAGES/1.jpeg')


plt.imshow(image)
plt.show()
#plt.waitKey(0)

height, width = image.shape[:2]
print(image.shape)

# Let's get the starting pixel coordiantes (top left of cropped top)
start_row, start_col = int(0), int(0)
# Let's get the ending pixel coordinates (bottom right of cropped top)
end_row, end_col = int(height * .5), int(width)
#cropped_top = image[start_row:end_row , start_col:end_col]
cropped_top = image[69:110 , start_col:end_col]
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
cropped_bot = image[108:147 , start_col:end_col]
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

from skimage.util import img_as_float


image1 = np.sum(img_as_float(cropped_top))
image2 = np.sum(img_as_float(cropped_bot))
print(("Right side",image1))
print(("Left side",image2))
print((image1-image2))
if(image1 > image2):
    s="Right"
else:
    s="Left"
print(s)
def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]
object=[name, to_str(image1), to_str(image2),to_str(image1-image2), s]
#f = open('classifier.csv', 'w')
print(object)
header=['Participant','Rigt Side','Left Side','Difference','Classification']
with open('classifier.csv', 'a') as f:
#    wr = csv.writer(f, dialect='excel')

#    wr.writerow(object)

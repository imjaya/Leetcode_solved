
#import win32com.client
import os
import skimage
import skimage.viewer
import sys
import cv2
import csv
from matplotlib import pyplot as plt
import numpy as np
import glob

editFiles = glob.glob("D:/FOOTFALL_IMAGES/CMT_*.jpeg")

for i, fname in enumerate(editFiles):
    name=fname[19:30]
    img = cv2.imread(editFiles[i],0)
    print(i)
    plt.imshow(img)
    #plt.show()
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    height, width = thresh5.shape[:2]
    print(thresh5.shape)
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
    #plt.show()
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
    #plt.show()
    #plt.waitKey(0)
    #plt.destroyAllWindows()

    print(cropped_top.size)
    print(cropped_bot.size)
    print((average1))
    print((average2))

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
    def to_str(var):
        return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]
    object=[name, to_str(image1), to_str(image2),to_str(image1-image2), s]
    #f = open('classifier.csv', 'w')
    print(object)
    header=['Participant','Rigt Side','Left Side','Difference','Classification']
    with open('classifier.csv', 'a') as f:
        wr = csv.writer(f, dialect='excel')

        wr.writerow(object)

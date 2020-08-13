from skimage import measure
from skimage import metrics
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.util import img_as_float
img = cv2.imread('D:/FOOTFALL_IMAGES/CMT_102_DG2 - MULTIPLE FOOTFALLS.jpeg',0)

image = img_as_float(img)
print((image))

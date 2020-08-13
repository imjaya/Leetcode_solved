from skimage import measure
from skimage import metrics
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
from skimage.util import img_as_float

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])



	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = metrics.structural_similarity(imageA, imageB)
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	# show the images
	plt.show()


img = plt.imread('D:/FOOTFALL_IMAGES/CMT_102_DG2 - MULTIPLE FOOTFALLS.jpeg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#image = plt.imread('D:/FOOTFALL_IMAGES/1.jpeg')
plt.imshow(img)
plt.show()
#plt.waitKey(0)

height, width = image.shape[:2]
print(image.shape)

# Let's get the starting pixel coordiantes (top left of cropped top)
start_row, start_col = int(0), int(0)
# Let's get the ending pixel coordinates (bottom right of cropped top)
end_row, end_col = int(height * .5), int(width)
#cropped_top = image[start_row:end_row , start_col:end_col]
cropped_top = image[88:135 , start_col:end_col]
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
cropped_bot = image[134:181 , start_col:end_col]
average2 = cropped_bot.mean(axis=0).mean(axis=0)
print(start_row, end_row)
print(start_col, end_col)

plt.imshow(cropped_bot,cmap='gray')
plt.show()





# initialize the figure
fig = plt.figure("Images")
images = ("Top", cropped_top), ("Bottom", cropped_bot)
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images

compare_images(cropped_top, cropped_bot, "Top vs. Bottom")
#top=np.sum((cropped_top.astype("float"))/(float(imageA.shape[0] * imageA.shape[1]))
#bot=np.sum((cropped_bot.astype("float"))/(float(imageA.shape[0] * imageA.shape[1]))
#print(top)
#print(bot)
image1 = np.sum(img_as_float(cropped_top))
image2 = np.sum(img_as_float(cropped_bot))
print((image1-image2))

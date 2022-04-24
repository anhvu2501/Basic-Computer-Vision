import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib as mpl
# Change backend of matplotlib from GTK3Agg to TkAgg then we can use plt.show()
mpl.use('TkAgg')

img = cv.imread('Photos/b.jpg')
cv.imshow('Original Image', img)

# Compute Histogram for grayscale images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# images: list of images
# channels: specify the index of the channel we want to compute a histogram for
# mask: if we want to compute a histogram for a specific portion of an image
# histSize: the number of bins we want to use for computing the histogram
# ranges: range of all possible pixel values\

# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256] )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,255])
# plt.show()

# Compute Histogram with a mask
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(
    blank, (img.shape[1]//2 - 35, img.shape[0]//2 - 45), 100, 255, thickness=-1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,255])
# plt.show()

# Colour histogram
colors = ('b', 'g', 'r')
# for color in enumerate(colors):
#     print(color)

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
# When calculate histogram per channel, we have to use a binary mask. Cannot use 3-channel mask
plt.show()

cv.waitKey(0)

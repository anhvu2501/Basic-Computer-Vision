import cv2 as cv

img = cv.imread('Photos/b.jpg')
cv.imshow('Original Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Thresholding
# Because we want to binarize the image then we need to convert it to grayscale
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold Inverse', thresh_inv)

# Adaptive Thresholding\
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,
                                       13, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)

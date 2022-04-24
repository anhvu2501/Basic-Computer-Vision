# How to identify contours - the boundaries of objects
import cv2 as cv
import numpy as np

img = cv.imread('Photos/shape.jpg')
cv.imshow('Original Image', img)

blank = np.zeros((img.shape[0], img.shape[1], 3), dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

blurred = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blured', blurred)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
# threshold essentially looks at an image and tries to binarize it
# if a particular pixel is < thresh (125 here), it's going to be set to 0 or blank. Otherwise, it's set to white or 255


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# img here can be passed #canny, #threshold, etc
# mode -> to find the contours
    # RETR_TREE: all the hierarchical contours
    # RETR_EXTERNAL: external contours
    # RETR_LIST: all contours
# method: contours approximation method
print(f'{len(contours)} contours found!')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Draw contours', blank)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread('Photos/b.jpg')

# Simple method
img_hor = np.hstack((img,img))
# cv.imshow('Horizontal Join', img_hor)

img_ver = np.vstack((img,img))
# cv.imshow('Vertical join', img_ver)
# --> Issue:
# The merged image may go out of the frame
# Images have to have the same number of channels to merge. We cannot merge RGB with grayscale


# Optimized method
def stack_image(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv.resize(img_array[x][y], (0,0), None, scale, scale)
                else:
                    img_array[x][y] = cv.resize(img_array[x][y], (img_array[0][0].shape[1],
                    img_array[0][0].shape[0]), None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv.cvtColor(img_array[x][y], cv.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), dtype='uint8')
        hor = [image_blank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range (0,rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv.resize(img_array[x], (0,0), None, scale, scale)
            else:
                img_array[x] = cv.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv.cvtColor(img_array[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_stack = stack_image(0.5, ([img, gray, img], [img, img, img]))
cv.imshow('Stacked Images', img_stack)
# array = np.array([(1,2,3), (4,5,6), (7,8,9)])
# print(array)
# test = [array]
# print(test)
array = np.array(img)
print(array.shape)
cv.waitKey(0)

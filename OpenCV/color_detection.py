import cv2 as cv
import numpy as np


def empty(a):
    pass

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

path = r'Photos/images.jpeg'
cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars', 640, 240)
cv.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
cv.createTrackbar('Hue Max', 'TrackBars', 179, 179, empty)
cv.createTrackbar('Sat Min', 'TrackBars', 31, 255, empty)
cv.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty)
cv.createTrackbar('Val Min', 'TrackBars', 26, 255, empty)
cv.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)

# Detect Blue
while True:
    img = cv.imread(path)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(hsv, lower, upper)
    # See the mask and choose the suitable value for trackbars
    # cv.imshow('Original Image', img)
    # cv.imshow('HSV', hsv)
    # cv.imshow('Mask', mask)
    img_result = cv.bitwise_and(img, img, mask = mask)
    img_stack = stack_image(0.6, ([img, hsv], [mask, img_result]))
    cv.imshow('Stacked Images', img_stack)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


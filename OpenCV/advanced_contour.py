import cv2 as cv
import numpy as np


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
                    img_array[x][y] = cv.resize(
                        img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv.resize(img_array[x][y], (img_array[0][0].shape[1],
                                                                  img_array[0][0].shape[0]), None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv.cvtColor(
                        img_array[x][y], cv.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), dtype='uint8')
        hor = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv.resize(
                    img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv.resize(
                    img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv.cvtColor(img_array[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


def get_contours(img):
    contours, hierarchy = cv.findContours(
        img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print("Number of objects: " + str(len(contours)))
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        # this condition to remove noises
        if area > 500:
            cv.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)  # arc len of contours
            # print(peri)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)  # approx how many corner points
            print(len(approx))
            obj_cor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            if obj_cor == 3:
                object_type = "Triangle"
            elif obj_cor == 4:
                aps_ratio = w / float(h)
                if aps_ratio > 0.98 and aps_ratio < 1.03:
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif obj_cor > 4:
                object_type = "Circles"
            else:
                object_type = "None"

            cv.rectangle(opening, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(opening, object_type,
                       (x + (w // 2) - 10, y + (h // 2) - 10), cv.FONT_HERSHEY_COMPLEX, 0.7,
                       (0, 0, 0), 2)


img = cv.imread('Photos/Rice/1_wIXlvBeAFtNVgJd49VObgQ.png')
cv.imshow('Original Image', img)
# img_contour = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 0)  # the higher the sigma is, the more blur we have
_, thresh = cv.threshold(blur, 120, 255, cv.THRESH_BINARY)

# Apply opening to remove small objects
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # rectangular structuring element
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
img_contour = opening.copy()
get_contours(opening)
blank = np.zeros(img.shape[:2], dtype='uint8')
img_stack = stack_image(0.8, ([img, gray, blur], [opening, img_contour, blank]))
cv.imshow('Stack', img_stack)

cv.waitKey(0)

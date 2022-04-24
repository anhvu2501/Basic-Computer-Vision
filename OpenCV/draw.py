# Draw shapes and write text 
import cv2 as cv
import numpy as np

# width, height, number of channel (500, 500, 3)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[:] = 0, 255, 0
cv.imshow('Green', blank)

blank[:] = 0, 0, 0
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red box', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
blank[:] = 0, 0, 0
cv.circle(blank, (250,250), 250, (255,0,0), thickness=2)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (123, 213, 321), thickness=2)
cv.imshow('Line', blank)

# 5. Write text
blank[:] = 0,0,0
cv.putText(blank, 'Hello, I\'m Vu', (100,200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (22, 55, 88), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)
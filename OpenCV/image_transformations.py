import cv2 as cv
import numpy as np

img = cv.imread('Photos/vuhta.jpeg')
cv.imshow('Image', img)

# Translation the image: shifts the image along x and y axes
def translate (img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]]) # Create 2x3 matrix
    dimensions = (img.shape[1], img.shape[0])
    # print(transMat)
    return cv.warpAffine(img, transMat, dimensions)
# -x --> Left
#  x --> Right
# -y --> Up
#  y --> Down
translated = translate(img, 100, -100)
cv.imshow('Translated', translated)

# Rotation
def rotate (img, angle, rotPoint=None):
    (height, width) = (img.shape[0], img.shape[1])
    if rotPoint is None:
        rotPoint = (width//2, height//2) # Center to rotate

    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMatrix, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
# flipCode = -1 | 0 | 1
# --> 0: flip vertically
# --> 1: flip horizontally
# --> -1: both vertically and horizontally
flip = cv.flip(img, 1)
cv.imshow('Flipped', flip)

cv.waitKey(0)
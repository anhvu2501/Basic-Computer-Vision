import cv2 as cv

img = cv.imread('Photos/b.jpg')
cv.imshow('Original Image', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
# just need to pass an integer in ksize
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
# d: diameter value
# sigmaColor: a larger value for this color means that there are more colors in the neighborhood 
#that will be considered when the blur is computed
# sigmaSpace: larger value of this space means that pixels further out the central pixel will influence
#the blurring calculation
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)


# Note: keep the parameter in Median and Bilateral appropriately to not make the image look smudged
cv.waitKey(0)
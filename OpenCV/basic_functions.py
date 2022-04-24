import cv2 as cv

img = cv.imread('Photos/vuhta.jpeg')

cv.imshow('Image', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# Blur
# Using Gaussian Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blured Image', blur)

# Edge Cascade => find the edges that are present in the image
# Using Canny Edges detector
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilate an image using a specific structuring element
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# Erode the image >< Dilate
eroded = cv.erode(canny, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Crop => Using array slicing
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
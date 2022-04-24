# Read image, video
# Rescale and Change Resolution
import cv2 as cv
# Read Images
# img = cv.imread('Photos/a.jpg')

def rescaleFrame (frame, scale = 0.75):
    # works with Images, Videos and Live Video

    # shape method belongs to numpy => returns the shape of 2D array
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# img_resized = rescaleFrame(img, scale=.5)

# cv.imshow('original image', img)
# cv.imshow('resized image', img_resized)
# cv.waitKey(0)


# Read Video from Webcam
# Option 0 is for taking video from webcam
capture = cv.VideoCapture(0) 

# def changeResolution (width, height):
#     # only works for live video
#     capture.set(3, width)
#     capture.set(4, height)

while True:
    isTrue, frame = capture.read() # read the video frame by frame
    # returns frame and a Boolean that says if the frame was successfully read in or not

    # changeResolution(frame.shape[1], frame.shape[0]) # Change live video resolution

    cv.imshow('Webcam', frame)

    # resized_frame = rescaleFrame(frame)
    # cv,cv.imshow('Rescaled webcam', resized_frame)

    # For breaking the while loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


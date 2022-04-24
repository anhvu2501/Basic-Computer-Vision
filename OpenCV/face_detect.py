import cv2

# img = cv2.imread('Photos/b.jpg')
# cv2.imshow('Original Image', img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

# print(f'Number of faces found = {len(faces_rect)}')

# for (x,y,w,h) in faces_rect:
#     cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# cv2.imshow('Detected Image', img)

# Test with video
capture = cv2.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    # scaleFactor – Parameter specifying how much the image size is reduced at each image scale
    # minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    # minSize – Minimum possible object size. Objects smaller than that are ignored.
    # maxSize – Maximum possible object size. Objects bigger than this are ignored.
    frame_cascade = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=2)
    # print(f'Number of frame cascades {len(frame_cascade)}')
    for (x,y,w,h) in frame_cascade:
        # faces_roi = frame[y:y+h, x:x+w]
        # cv2.GaussianBlur(faces_roi, (9,9), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)
    
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# cv2.waitKey(0)
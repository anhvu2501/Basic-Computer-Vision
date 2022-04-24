import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy', allow_pickle=True)
people = np.load('people.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('Photos/Test Set/Rose/791ea2f542d7eeb7124ebe498b7e509b.jpg')
# cv.imshow('Original Image', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect the face from the image
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)

for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y),(x+w, y+h), (0,255,0), 2)

cv.imshow('Detected Image', img)
cv.waitKey(0)
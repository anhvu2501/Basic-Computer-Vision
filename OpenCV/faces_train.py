import os
import cv2 as cv
import numpy as np

# Get a list of people's name in the folder
# people = ['Chris Evans', 'Lily Collins', 'Lisa', 'Rose']

# Another way
people = []
for i in os.listdir(r'/home/vuhta/Coursera/OpenCV/Faces'):
    people.append(i)
# print(people)

DIR = r'/home/vuhta/Coursera/OpenCV/Faces'

features = []  # the image arrays of faces
labels = []  # corresponding labels

haar_cascade = cv.CascadeClassifier('haar_face.xml')


def create_train():
    for person in people:
        # Point out the path to the specific folder inside folder Faces
        path = os.path.join(DIR, person)
        # Take label by using index then map to correspond label
        label = people.index(person)
        # Loop over images in that folder
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # face region of interest: grab the face of image
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)
people = np.array(people)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

np.save('people.npy', people)
np.save('features.npy', features)
np.save('labels.npy', labels)
face_recognizer.save('face_trained.yml')
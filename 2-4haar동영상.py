#haar을 이용한 방식은 - size = 즉 해상도와도 연관이 있다.!!

import cv2 as cv
import numpy as np

face_cascade_name = 'web\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
eyes_cascade_name = 'web\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'
file_name = 'Opencv_practice/video/obama_01.mp4'

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    ## Detect Face
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.rectangle(frame, (x,y) , (x+w, y+h), (0,255,0),4)
        faceROI= frame_gray[y:y+h, x:x+w]
        #---in each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2//2 , y+y2 + h2//2)
            radius = int(round(w2 + h2) * 0.25)
            frame = cv.circle(frame, eye_center, radius, (255,0,0) , 4)
    cv.imshow("Capture - Face detection", frame)

face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

#--1. Load the cascades

if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print("!! ERROR loading face cascade")
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print("!! ERROR loading eyes cascade")
    exit(0)

#-- 2. Read the video stream
cap = cv.VideoCapture(file_name)
if not cap.isOpened:
    print("--(!) Error opening video capture")
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print("!! No captured frame -- Break")
        break
    detectAndDisplay(frame)
    #'q' key down -> to quit!
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
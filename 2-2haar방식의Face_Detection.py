import cv2 as cv
import numpy as np
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #그림을 grayscale로 바꾸어 정확도를 높여줘야한다. 
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x+w//2, y + h//2)
        frame = cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),4) #녹색으로 사각형을 그린다.
        faceROI = frame_gray[y:y+h, x:x+w]
        # ROI : READ OF INTEREST
        #--In each face, detect eyes    
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2//2 , y+y2 + h2//2)
            radius = int(round((w2+h2) * 0.25))
            frame = cv.circle(frame, eye_center, radius, (255,0,0), 4)
        cv.imshow('Capture - Face detection', frame)

img = cv.imread("OpenCv/ko2.jpg")
print("width : {}pixels".format(img.shape[1]))
print("height:{}pixels".format(img.shape[0]))
print("channels:{}".format(img.shape[2]))

(height, width) = img.shape[:2]
cv.imshow("Original Image", img)
face_cascade_name = 'web\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'

eyes_cascade_name = 'web\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'

face_cascade = cv.CascadeClassifier() #CascadeClassifier()함수
eyes_cascade = cv.CascadeClassifier()

#1.Load the Cascades  
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print("!Error! : loading face cascade")
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print("!!ERROR: loading eyes cascade")
    exit(0)
detectAndDisplay(img)
cv.waitKey(0)
cv.destroyAllWindows()
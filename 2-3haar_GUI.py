import cv2 as cv
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

face_cascade_name = 'web\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
eyes_cascade_name = 'web\Lib\site-packages\cv2\data\haarcascade_eye_tree_eyeglasses.xml'
file_name = 'OpenCv/ko1.jpg'
title_name = 'Haar cascade object detection'
frame_width = 500

def selectFile():
    file_name = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes = (("jpeg files", "*.jpg"), ("all files", "*.*")))
    print("File name :", file_name)
    read_image = cv.imread(file_name)
    (height, witdh) = read_image.shape[:2]
    frameSize = int(sizeSpin.get())
    ratio = frameSize / width
    dimension = (frameSize, int(height * ratio))
    read_image = cv.resize(read_image, dimension, interpolation =cv.INTER_AREA)
    image = cv.cvtColor(read_image, cv.COLOR_BGR2RGB)
    image= Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image= image)
    detectAndDisplay(read_image)

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
    image= cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)
    detection.config(image= imgtk)
    detection.image = imgtk
#main
main = Tk()
main.title(title_name)
main.geometry()
read_image = cv.imread(file_name)
(height, width) = read_image.shape[:2]
ratio = frame_width / width #비율 
dimension = (frame_width, int(height * ratio))  #앞에서 선언한 frame_width의 비율에 맞게 height을 조절
read_image = cv.resize(read_image, dimension, interpolation=cv.INTER_AREA)
image = cv.cvtColor(read_image, cv.COLOR_BGR2RGB)
image = Image.fromarray(image)
imgtk = ImageTk.PhotoImage(image=image)



face_cascade = cv.CascadeClassifier() #CascadeClassifier()함수
eyes_cascade = cv.CascadeClassifier()

#1.Load the Cascades  
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print("!Error! : loading face cascade")
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print("!!ERROR: loading eyes cascade")
    exit(0)

label = Label(main, text = title_name)
label.config(font=("Courier", 18))
label.grid(row=0, column=0, columnspan=4)
sizeLabel = Label(main, text="Frame Width : ")
sizeLabel.grid(row=1, column=0)
sizeVal = IntVar(value=frame_width)
sizeSpin = Spinbox(main, textvariable=sizeVal, from_=0, to=2000, increment=100, justify = RIGHT)
sizeSpin.grid(row=1, column=1)
Button(main, text="File Select", height = 2 , command=lambda:selectFile()).grid(row=1, column=2, columnspan=2, sticky=(W,E))
detection = Label(main, image = imgtk)
detection.grid(row=2, column=0, columnspan=4)
detectAndDisplay(read_image)
main.mainloop()

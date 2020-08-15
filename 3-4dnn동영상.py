import cv2
import numpy as np

model_name = 'Opencv_practice/res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name = 'Opencv_practice/deploy.prototxt.txt'
file_name = 'Opencv_practice/11.jpg'
title_name = "DNN deep learning obkect detection"
#동영상은 여러 정지영상의 연속


#########################미완성##############################
def detectAndDisplay(frame):
    model = cv2.dnn.readNetFromCaffe(prototxt_name, model_name)
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
    (300,300), (104.0, 177.0, 123.0))
    model.setInput(blob)
    detections= model.forward()


cap  = cv2.VideoCapture(file_name)
if not cap.isOpened:
    print("Error opening video capture")
    exit(0)
while True:
    ret , frame = cap.read()
    if frame is None:
        print("No captured frame -- Break")
        break
    detectAndDisplay(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
import cv2
import numpy as np

model_name = 'Opencv_practice/res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name = 'Opencv_practice/deploy.prototxt.txt'
min_confidence = 0.2
file_name = "Opencv_practice/11.jpg"

def detectAndDisplay(frame):
    model = cv2.dnn.readNetFromCaffe(prototxt_name, model_name)
    blob = cv2.dnn.blobFromImage(cv2.resize(frame , (300,300)), 1.0, (300,300), (104.0, 177.0, 123.0))
    model.setInput(blob)
    detections = model.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0,0,i,2]

        if confidence > min_confidence:
            box = detections[0, 0, i, 3:7] * np.array([width, height, width,height])
            (startX, startY, endX, endY) = box.astype("int")
            print(confidence, startX, startY, endX, endY)
            text = "{:.2f}%".format(confidence*100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY),(0,255,0),2)
            cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,255,0),1)

    cv2.imshow("FACE DETECTIONS BY DNN", frame)




img = cv2.imread(file_name)
(height, width) = img.shape[:2]

cv2.imshow("Original Image", img)

detectAndDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
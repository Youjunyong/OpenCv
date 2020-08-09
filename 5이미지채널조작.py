import cv2 as cv
import numpy as np

img = cv.imread("OpenCv/11.jpg")

(height , width) = img.shape[:2]
center = (height//2 , width//2)

cv.imshow("defalut", img)
(B,G,R) = cv.split(img)
#gray scale로 rgb 따로보기
cv.imshow("Blue channel", B)
cv.imshow("Green channel", G)
cv.imshow("Red channel", R)
cv.waitKey(0)


#각자의 색으로 rgv 보기
zeros = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Red", cv.merge([zeros, zeros, R]))
cv.imshow("Green", cv.merge([zeros, G, zeros]))
cv.imshow("Blue", cv.merge([B,zeros, zeros]))
cv.waitKey(0)



#FILTER
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Filter",gray)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Filter", hsv)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB Filter", lab)



#RGB로 따로 뽑았던것, 원본처럼 복구하기
BGR = cv.merge([Blue, Green , Red])
cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np

img = cv.imread("11.jpg")

(height , width) = img.shape[:2]
center = (height//2 , width//2)

cv.imshow("defalut", img)

#마스크 사용 기본원리
#기본원리 : bitwise 연산, and or xor.... 
mask= np.zeros(img.shape[:2] , dtype = "uint8") #전부 까맣게...
#numpy를 이용하여, img의 높이와 널비를 이용하여 모든 칸에 0을 채워준다
cv.circle(mask, center, 200, (255,255,255), -1)

cv.imshow("mask", mask)
print(mask)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("with mask", masked)


cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
#open cv 에서는 RGB가 아니라 BGR 순서라는 점 기억!
#인텔에서 처음 만들어진 open cv



#1. 이미지 출력하기
img = cv.imread("11.jpg") 
cv.imshow("no", img)
(b,g,r) = img[0,0]
print("pixel at (0,0) - Red : {} , Green : {} , Blue : {}".format(r,g,b)) #0.0 좌표의 RGB값 얻기
# cv.waitKey(0)
# cv.destroyAllwindows()


# 2. 좌표값을 입력하여 사각형 넣기
# img = cv.imread("11.jpg") 
# cv.imshow("no", img) #원본 이미지
# (b,g,r) = img[0,0]
# print("pixel at (0,0) - Red : {} , Green : {} , Blue : {}".format(r,g,b)) #0.0 좌표의 RGB값 출력
# dot = img[50:100, 50:100]
# cv.imshow("dot",dot)
# img[50:100 , 50:100] = (0,0,255)
# cv.imshow("dotted no", img) 
# cv.waitKey(0)
# cv.destroyAllWindows()


# 3. 사각형, 원 그리기
img = cv.imread("11.jpg") 
cv.rectangle(img, (150,50), (200,100), (0,255,0), 5) #사각형, 시작점 , 끝점, 색, 선두께
cv.circle(img, (110,110), 25, (0,255,255), -1) #원 중심, 반지름, 선두께 (-1을하면 내부를 fill한다.)
cv.line(img, (350,100), (400,100), (255,0,0), 2) #Line그리기
cv.putText(img, 'Hello' , (450, 100), cv.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 4) #텍스트 쓰기
cv.imshow("draw, circle, rectangle", img)
cv.waitKey(0)
cv.destroyAllWindows()
import cv2
print(cv2.__version__,"@@")
img = cv2.imread("11.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("no", img)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
day1 _ 이미지 픽셀 좌표체계

이미지의 종류

raster graphics (bitmap)
pixels.
점들을 가지고 표현한 이미지. 따라서 일정수준 이상으로 확대하게 되면 이미지가 깨지는 현상이 나타난다.

vector
RGB를 조합한 색을 만들어낸다.



Mnist 물리과학연구단체... 에서 6만개의 손글씨를 제공해준다.



'''
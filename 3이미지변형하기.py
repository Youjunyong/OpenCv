import cv2
import numpy as np

img = cv2.imread("11.jpg")
(height, width, channels) = img.shape[:3]
center = (width // 2, height // 2)
print("width, height , channels : {}".format(img.shape))
            #이미지 자르기 : dot = img[50:100 , 50:100]

    # 그림 위치 변환하기 MOVE
    # move = np.float32([[1,0,100] , [0,2,100]])
    # moved = cv2.warpAffine(img, move, (width, height))
    # cv2.imshow("moved down: + , up: - and right:+, left -", moved)
    # [1, 0, 100] 맨뒤의 숫자 : 100만큼 down , 앞의 숫자들은 늘리는? 것같은데 찾아서 포스팅할것.
    # [0,1,100]  맨뒤 : 100만큼 right 

#Rotate 회전시키기. getRotationMatrix2D
# move = cv2.getRotationMatrix2D(center, 90, 1.0) #기준좌표, 각도 , 1.0 : scale(그림 키우기)
# rotated = cv2.warpAffine(img, move, (width, height))
# cv2.imshow("rotated pic", rotated)

        # 이미지 확대 및 축소 (Resize)
        # ratio = 200.0 / width
        # dimension = (200, int(height * ratio))  #width를 200으로 줄였을때, 같은 비율로 높이를 줄이기 위한
        # resized = cv2.resize(img, dimension , interpolation=cv2.INTER_AREA)
        # interpolation : 보간법 , INTER_AREA를 자주 사용하게된다. 
        # 확대의 경우에는 inter_linear 가 좋다고 하고 , 축소할때는 inter area , 등등... 여러가지 방식이있다.
        # cv2.imshow("Resized", resized)

        
#이미지 반전(Flip)
# flipped = cv2.flip(img, 1)
# cv2.imshow("Flipped Horizontal 1, vertical 0, both -1", flipped)
# cv2.imshow("원본", img)
# 1이면 좌우대칭, 0일땐 상하반전, -1일경우 좌우상하 반전




cv2.waitKey(0)
cv2.destroyAllWindows()
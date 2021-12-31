# 특정 범위 안에 있는 행렬 원소 검출
'''
cv2.inRange(src, lowerb, upperb, dst=None) -> dst

- src : 입력 행렬
- lowerb : 하한 값 행렬 또는 스칼라
- upperb : 상한 값 행렬 또는 스칼라
- dst : 입력 영상과 같은 크기의 마스크 영상(numpy.uint8)
        범위 안에 들어가는 픽셀을 255, 나머지는 0으로 설정.
'''

# (예제) HSV 색 공간에서 녹색 영역 추출하기

import sys
import cv2

src = cv2.imread('candies.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

# (예제) 트랙바를 이용한 특정 색상 영역 추출

src = cv2.imread('candies.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('hmin', 'dst')
    hmax = cv2.getTrackbarPos('hmax', 'dst')
    
    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')

cv2.createTrackbar('hmin', 'dst', 50, 179, on_trackbar)
cv2.createTrackbar('hmax', 'dst', 50, 179, on_trackbar)
cv2.waitKey()
cv2.destroyAllWindows()
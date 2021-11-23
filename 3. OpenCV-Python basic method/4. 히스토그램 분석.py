# 히스토그램 구하기
'''
cv2.calcHist(images, channels, mask, histSize, ranges, hist = None,
             accumulate=None) -> hist

- images : 입력 영상 리스트
    - 한 개의 영상을 사용하더라도 리스트로 묶어줘야 한다.
- channels : 히스토그램을 구할 채널을 나타내는 리스트
    - 회색조 : [0]
    - 블루, 그린 : [0, 1]
    - 전부 : [0, 1, 2]
- mask : 마스크 영상
    - 입력 영상 전체에서 히스토그램을 구하려면 None 지정
- histSize : 히스토그램 각 차원의 크기(bin의 개수)를 나타내는 리스트
- ranges : 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
- hist : 계산된 히스토그램(numpy.ndarray)
- accumulate : 기존의 hist 히스토그램에 누적하려면 True, 새로 만들려면 False
    - 대부분의 경우 False
'''

# (예제) Grayscale 영상의 히스토그램 구하기

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()

# (예제) Color 영상의 히스토그램 구하기

src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

color = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for p, c in zip(bgr_planes, color):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('src', src)
cv2.waitKey()
plt.show()
cv2.destroyAllWindows()

# (예제) OpenCV 그리기 함수로 Grayscale 영상의 히스토그램 나타내기

def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax)) # 가장 큰 위치가 100pixel이 되도록 하여 100pixel 위로 못 올라가게한다.
        cv2.line(imgHist, pt1, pt2, 0)
    
    return imgHist

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('histImg', histImg)
cv2.waitKey()

cv2.destroyAllWindows()
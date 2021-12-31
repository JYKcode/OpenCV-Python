# 밝기 조절을 위한 덧셈 연산
'''
cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst

- scr1 : (입력)첫 번째 영상 또는 스칼라 
- scr2 : (입력)두 번째 영상 또는 스칼라 
- dst : (출력)덧셈 연산의 결과 양상
- mask : 마스크 영상
- dtype : 출력 영상(dst)의 타입.(e.g.)cv2.CV_8U 등
- 참고사항
    - 스칼라는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플
    - dst를 함수 인자로 전달하려면 dst의 크기가 src1, src2와
      같아야 하며, 타입이 적절해야 함
'''

# (예제) Grayscale 영상의 밝기 100만큼 증가시키기

import cv2
import sys
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src, 100)
dst2 = src + 100 # 255를 넘어가게 되면 (x - 255) 값으로 지정 -> 영상이 어두워진다.
dst3 = np.clip(src + 100., 0, 255).astype(np.uint8) # '100.' : 실수단위로 계산해야한다.

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2) 
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()

# (예제) Color 영상의 밝기 100만큼 증가시키기

src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src, (100, 100, 100, 0))
dst2 = src + 100
dst3 = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()
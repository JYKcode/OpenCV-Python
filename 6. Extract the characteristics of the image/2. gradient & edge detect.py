# 2D 벡터의 크기 계산 함수
'''
cv2.magnitude(x, y, magnitude=None) -> magnitude

- x : 2D 벡터의 x좌표 행렬(실수형)
- y : 2D 벡터의 y좌표 행렬(실수형)
- magnitude : 2D 벡터의 크기 행렬(x와 같은 크기, 같은 타입)
    - megnitude(I) = sqrt(x(I)^2 + y(I)^2)
'''

# 2D 벡터의 방향 계산 함수
'''
cv2.phase(x, y, angle=None, angleInDegrees=None) -> angle

- x : 2D 벡터의 x좌표 행렬(실수형)
- y : 2D 벡터의 y좌표 행렬(x와 같은 크기, 실수형)
- angle : 2D 벡터의 크기 행렬(x와 같은 크기, 같은 타입)
    - angle(I) = atan2(y(I), x(I))
    - 만약 x(I)=y(I)=0 이면 angle은 0으로 설정됨
- angleInDegrees : True이면 각도 단위, False이면 래디언 단위
'''

# (예제) 소벨 필터를 이용한 에지 검출

import sys
import cv2
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
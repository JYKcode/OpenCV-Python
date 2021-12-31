# 명암비 조절 함수
'''
dst(x, y) = saturate(src(x, y) + (src(x, y) - 128)*alpha)

- dst(x, y) = (1 + alpha)*src(x, y) - 128*alpha
- alpha : 얼마나의 contrast를 해야하는지는 정해져 있지 않다.
          조절하면서 적절한 값을 찾아줘야 한다.
'''

# 정규화 함수
'''
cv2.normalize(src, dst, alpha=None, beta=None, norm_type=None, dtype=None,
              mask=None) -> dst

- src : 입력 영상
- dst : 결과 영상
    - 함수 안에 들어있는 dst 매개변수는 None으로 준다.
- alpha 
    - (노름 정규화인 경우) 목표 노름 값
    - (원소 값 범위 정규화인 경우) 최솟값
- beta : (원소 값 범위 정규화인 경우) 최댓값
- norm_type : 정규화 타입
    - NORM_INF, NORM_L1, NORM_L2, NORM_MINMAX
    - NORM_MINMAX : (alpha = 0, beta = 255) => hist 스트레칭
    - Histogram streching : 영상의 히스토그램이 그레이스케일 전 구간에서 걸쳐 나타나도록 변경하는 선형 변환 기법
- dtype : 결과 영상의 타입
- mask : 마스크 영상
'''

# (예제) 기본적인 명암비 조절

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0
dst = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# (예제) Histogram stretching을 이용한 명암비 자동 조절

src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
strech_hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

plt.subplot(121), plt.plot(hist)
plt.subplot(122), plt.plot(strech_hist)
plt.show()

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
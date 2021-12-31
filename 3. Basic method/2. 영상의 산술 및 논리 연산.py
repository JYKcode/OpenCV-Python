# 가중치 합(weighted sum)
'''
cv2.addWeighted(src1, alpha, scr2, beta, gamma, dst=None, dtype=None) -> dst

- src1 : 첫 번째 영상
- alpha : 첫 번째 영상 가중치
- src2 : 두 번째 영상(src1과 같은 크기 & 같은 타입)
- beta : 두 번째 영상 가중치
- gamma : 결과 영상에 추가적으로 더할 값
- dst : 가중치 합 결과 영상
- dtype : 출력 영상(dst)의 타입
'''

# 뺄셈 연산
'''
cv2.subtract(src1, src2, dst=None, mask=None, dtype=None) -> dst

- 덧셈연산과 달리 순서가 중요하다.
'''

# 차이 연산
'''
cv2.absdiff(src1, src2, dst=None) -> dst
'''

# (예제) 영상의 산술 연산

import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'),
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'),
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'),
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'),
plt.show()
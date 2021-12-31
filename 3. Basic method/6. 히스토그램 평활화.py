# Histogram equalization
'''
Histogram equalization
- 히스토그램이 그레이스케일 전체 구간에서 균일한 분포로 나타나도록 변경하는
  명암비 향상 기법

cv2.equlizeHist(src, dst=None) -> dst
- src : 입력 영상(그레이스케일 영상)
- dst : 결과 영상
'''

# (예제) Grayscale image Histogram equalization

import sys
import cv2
import matplotlib.pyplot as plt

src = cv2.imread('sleepy.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst_equal = cv2.equalizeHist(src)
dst_strech = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

hist_origin = cv2.calcHist([src], [0], None, [256], [0, 256])
hist_strech = cv2.calcHist([dst_strech], [0], None, [256], [0, 256])
hist_equal = cv2.calcHist([dst_equal], [0], None, [256], [0, 256])

plt.subplot(131), plt.plot(hist_origin)
plt.subplot(132), plt.plot(hist_equal)
plt.subplot(133), plt.plot(hist_strech)
plt.show()

cv2.imshow('src', src)
cv2.imshow('dst_strech', dst_strech)
cv2.imshow('dst_equal', dst_equal)
cv2.waitKey()
cv2.destroyAllWindows()

# (예제) Color image Histogram equalization
'''
R, G, B 각 색 평면에 대해 히스토그램 평활화를 진행하면 색감이 완전히 달라질 수가
있으므로 YCrCb의 Y(밝기 성분)에 대해서만 히스토그램 평활화 수행한다.
'''

src = cv2.imread('field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb_planes = cv2.split(src_ycrcb)
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv2.merge(ycrcb_planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
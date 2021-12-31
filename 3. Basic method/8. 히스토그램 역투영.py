# Histogram Backprojection
'''
- 영상의 각 픽셀이 주어진 히스토그램 모델에 얼마나 일치하는지 검사하는 방법
- 임의의 색상 영역을 검출할 때 효과적
- inRange 함수는 원색적인 색을 찾아내기 좋지만
  임의의 색(ex.살색)같은 경우 Hue 값으로 찾기가 힘들다.
'''

# 히스토그램 역투영 함수
'''
cv2.calcBackProject(images, channels, hist, ranges, scale, dst=None) -> dst

- images : 입력 영상 리스트
- channels : 역투영 계산에 사용할 채널 번호 리스트
- hist : 입력 히스토그램(numpy.ndarray)
- ranges : 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
- scale : 출력 역투영 행렬에 추가적으로 곱할 값
- dst : 출력 역투영 영상
'''

# (예제1) 기본적인 히스토그램 역투영

import sys
import numpy as np
import cv2

# 1-1. 입력 영상에서 ROI를 지정하고, 히스토그램 계산
src = cv2.imread('cropland.png')

if src is None:
    print('Image load failed!')
    sys.exit()

x, y, w, h = cv2.selectROI(src)

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop = src_ycrcb[y:y+h, x:x+w]

channels = [1, 2] # 0인덱스인 y 성분은 쓰지 않음. y 성분은 밝기 정보
cr_bins = 128 # cr을 표현하는 범위. 256을 128로 단순화
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

hist = cv2.calcHist([crop], channels, None, histSize, ranges)
# 히스토그램 큰 값은 너무 큰 값에 몰릴 수 있으므로 log스케일 해주기. +1을 해줘서 -1값을 0으로
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 1-2. 입력 영상 전체에 대해 히스토그램 역투영
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
dst =cv2.copyTo(src, backproj)

cv2.imshow('backproj', backproj)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# (예제2) 히스토그램 역투영을 이용한 살색 영역 검출

# 2-1. CrCb 살색 히스토그램 구하기
ref = cv2.imread('kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)
hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

cv2.imshow('ref', ref)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 2-2. 입력 영상에 히스토그램 역투영 적용
src = cv2.imread('kids2.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image read failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()
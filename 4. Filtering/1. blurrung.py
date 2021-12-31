# 기본적인 2D 필터링
'''
cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None,
            borderType=None) -> dst

- src : 입력 영상
- ddepth : 출력 영상 데이터 타입(ex. cv2.CV_8U, cv2.CV_32F)
    - '-1'을 지정하면 src와 같은 타입의 dst 영상을 생성
- kernel : 필터 마스크 행렬(실수형)
- anchor : 고정점 위치
    - (-1, -1)이면 필터 중앙을 고정점으로 사용
- delta : 추가적으로 더할 값 (기본값=0)
- borderType : 가장자리 픽셀 확장 방식
    - 기본값을 사용하면 무난
- dst : 출력 영상
'''

# 블러링 : 평균 값 필터(Mean filter)
'''
- 영상의 특정 좌표 값을 주변 픽셀 값들의 산술 평균으로 설정
- 픽셀들 간의 그레이스케일 값 변화가 줄어들어 날카로운 edge가 무뎌지고,
  영상에 있는 잡음의 영향이 사라지는 효과
- 마스크 크기가 커질수록 평균 값 필터 결과가 더욱 부드러워짐
  -> 더 많은 연산량 필요!
'''

# 평균 값 필터링 함수
'''
cv2.blur(src, ksize, dst=None, anchor=None, borderType=None) -> dst

- src : 입력 영상
- ksize : 평균값 필터 크기
    - (width, height) 형태의 튜플
- dst : 결과 영상
    - 입력 영상과 같은 크기 & 같은 타입
'''

# (예제) cv2.filter2D() 함수를 이용한 평균값 필터링

import sys
import cv2
import numpy as np

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

for ksize in (3, 5, 7):
    kernel = np.ones((ksize, ksize), dtype=np.float64) / float(ksize**2)
    dst = cv2.filter2D(src, -1, kernel)
    desc = f'filter2D: {ksize} x {ksize}'

    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()

# (예제) 다양한 크기의 커널을 사용한 평균값 필터링

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

for ksize in (3, 5, 7, 9):
    dst = cv2.blur(src, (ksize, ksize))
    desc = f'Mean : {ksize} x {ksize}'
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()



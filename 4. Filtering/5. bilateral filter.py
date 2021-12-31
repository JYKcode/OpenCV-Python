# 잡음 제거 : 양방향 필터

# 양방향 필터(Bilateral filter)
'''
- 에지 보전 잡음 제거 필터(edge-preserving noise removal filter)의 하나
- 평균 값 필터 또는 가우시안 필터는 에지 부근에서도 픽셀 값을 평탄하게 만드는 단점이 있음
- 기준 픽셀과 이웃 픽셀과의 거리, 그리고 픽셀 값의 차이를 함께 고려하여 블러링 정도를 조절
- 모든 필터가 각각 상태에 따라 바뀌기 때문에 연산 속도가 상대적으로 느리다.
- sigma space 값이 커질수록 속도는 더 느려진다.
'''

# 양방향 필터링 함수
'''
cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None,
                    borderType=None) -> dst

- src : 입력 영상(8비트 또는 실수형, 1채널 또는 3채널)
- d : 필터링에 사용될 이웃 픽셀의 거리(지름)
    - '-1'을 입력하면 sigmaSpace 값에 의해 자동 결정됨
    - '-1'을 사용하는 것을 권장한다.
- sigmaColor : 색 공간에서 필터의 표준 편차(edge를 판별짓는 파라미터)
- sigmaSpace : 좌표 공간에서 필터의 표준 편차(GaussianBlur의 sigma 값과 완전 같다.)
- dst : 출력 영상(src와 같은 크기, 같은 타입)
- borderType : 가장자리 픽셀 처리 방식
'''

# (예제) 양방향 필터
import sys
import cv2

src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# sigmaColor 는 10 ~ 20, sigmaSpace 는 5이하가 좋은것 같다.
dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
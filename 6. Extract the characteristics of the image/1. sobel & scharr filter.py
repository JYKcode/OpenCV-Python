# 소벨 필터를 이용한 미분 함수
'''
cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None,
          delta=Noen, borderType=None) -> dst

- src : 입력 영상
- ddepth : 출력 영상 데이터 타입
    - '-1'이면 입력 영상과 같은 데이터 타입을 사용
- dx : x 방향 미분 차수
    - 대부분 dx=1, dy=0, ksize=3 또는 dx=0, dy=1, ksize=3 으로 지정
- dy : y 방향 미분 차수
- dst : 출력 영상(행렬)
- ksize : 커널 크기(기본값은 3)
- scale : 연산 결과에 추가적으로 곱할 값(기본값은 1)
- delta : 연산 결과에 추가적으로 더할 값(기본값은 0)
- borderType : 가장자리 픽셀 확장 방식(기본값은 cv2.BORDER_DEFAULT)
'''

# 샤르 필터를 이용한 미분 함수
'''
cv2.Scharr(src, ddepth, dx, dy, dst=None, scale=None, delta=None,
           borderType=None) -> dst

- src : 입력 영상
- ddepth : 출력 영상 데이터 타입
    - '-1'이면 입력 영상과 같은 데이터 타입을 사용
- dx : x 방향 미분 차수
- dy : y 방향 미분 차수
- dst : 출력 영상(행렬)
- scale : 연산 결과에 추가적으로 곱할 값(기본값은 1)
- delta : 연산 결과에 추가적으로 더할 값(기본값은 0)
- borderType : 가장자리 픽셀 확장 방식(기본값은 cv2.BORDER_DEFAULT)
'''

# (예제) 소벨 필터를 이용한 영상의 미분 예제

import sys
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

sobel_dx = cv2.Sobel(src, -1, 1, 0, delta=128)
sobel_dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', sobel_dx)
cv2.imshow('dy', sobel_dy)
cv2.waitKey()
cv2.destroyAllWindows()

# (예제) 샤르 필터를 이용한 영상의 미분 예제

import sys
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

Scharr_dx = cv2.Scharr(src, -1, 1, 0, delta=128)
Scharr_dy = cv2.Scharr(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', sobel_dx)
cv2.imshow('dy', sobel_dy)
cv2.waitKey()
cv2.destroyAllWindows()
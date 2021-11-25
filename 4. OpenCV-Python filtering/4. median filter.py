# 잡음 제거 : 미디언 필터

# 잡음의 종류
'''
- 가우시안 잡음(Gaussian noise)
- 소금&후추 잡음(Salt & Pepper noise)
  -> 요즘에는 보기 힘들다.
'''

# 미디언 필터(Median filter)
'''
- 주변 픽셀들의 값들을 정렬하여 그 중앙값(median)으로 픽셀 값을 대체
- Salt & Pepper noise에 효과적
- noise를 어떻게 제거하는지 그 아이디어에 집중해보자.
'''

# 미디언 필터링 함수
'''
cv2.medianBlur(src, ksize, dst=None) -> dst

- src : 입력 영상
- ksize : 커널 크기
    - 1보다 큰 홀수를 지정(ex. ksize = 3 -> (3 x 3))
- dst : 출력 영상(src와 같은 크기, 같은 타입)
'''

# (예제) 미디언 필터링

import sys
import cv2

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
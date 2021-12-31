# Canny edgy 검출 함수
'''
cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None,
          L2gradient=None) -> edges

- image : 입력 영상
- threshold1 : 하단 임계값
- threshold2 : 상단 임계값
    - threshold1 : threshold2 = 1:2 또는 1:3
- edges : 에지 영상
- apertureSize : 소벨 연산을 위한 커널 크기(기본값은 3)
- L2gradient : True 이면 L2 norm 사용, False이면 L1 norm 사용(기본값은 False)
    - L2norm의 경우 시간이 오래걸려서 보통 L1norm을 사용한다.
'''

# (예제) Canny edge 검출

import sys
import cv2

src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('woo.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)
dst2 = cv2.Canny(src2, 30, 50)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
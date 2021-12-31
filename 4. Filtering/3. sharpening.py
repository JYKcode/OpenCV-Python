# 샤프닝 : 언샤프 마스크 필터

# 언샤프 마스크(Unsharp mask) 필터링
'''
- 날카롭지 않은(unsharp) 영상, 즉, 부드러워진 영상을 이용하여 날카로운 영상을 생성
h(x) = f(x) + g(x) = 2f(x) - f'(x)
- f(x) : 원래의 영상
- f'(x) : 부드러워진 영상
- g(x) = f(x) - f'(x) => 뾰족한 부분만 남게 된다.
'''

# (예제) 언샤프 마스크 필터 구현하기

import sys
import cv2
import numpy as np

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

src_f = src.astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0, 0), 2)
dst = np.clip(2 * src_f - blr, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# (예제) 컬러 영상에 대한 언샤프 마스크 필터 구현하기

src = cv2.imread('rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
'''
GaussianBlur는 입력 영상의 dtype과 같은 출력영상을 내보내는데
src가 정수일 경우 소수점 아래부분이 다 잘려나간다.
즉, 미세한 변화가 사라지게 된다.
'''
src_f = src_ycrcb[:, :, 0].astype(np.float32)
blur = cv2.GaussianBlur(src_f, (0, 0), 2.0)
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
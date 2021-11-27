# 리매핑(remapping)
'''
- 영상의 특정 위치 픽셀을 다른 위치에 재배치하는 일반적인 프로세스
    - dst(x, y) = src(map_x(x, y), map_y(x, y))
- 어파인 변환, 투시 변환을 포함한 다양한 변환을 리매핑으로 표현 가능
'''

# 리매핑 함수
'''
cv2.remap(src, map1, map2, interpolation, dst=None, borderMode=None, 
          borderValue=None) -> dst

- src: 입력 영상
- map1: 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 x좌표.
        입력 영상과 크기는 같고, 타입은 np.float32인 numpy.ndarray.
- map2: 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 y좌표.
- interpolation: 보간법
- dst: 출력 영상
- borderMode: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT.
- borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.
'''

# (예제) 삼각함수를 이용한 리매핑

import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

# np.indice는 행렬의 인덱스값 x좌표값 y좌표값을 따로따로 행렬의 형태로 변환해줌
# y좌표에 sin함수를 줬는데 파도처럼 꿀렁꿀렁하게 하기 위해서
# y좌표 값에 10픽셀만큼 꿀렁꿀렁 거릴 수 있도록.
# sin함수가 x좌표를 이용해서 파도를 만들기 위해 map1을 줌
# 적당한 값을 나눠서 여러번 꿀렁꿀렁 거리게
map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32)

# borderMode는 근방의 색깔로 대칭되게 해서 채워줌, 기본값은 빈 공간을 검은색으로 표현
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

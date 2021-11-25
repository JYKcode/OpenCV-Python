# 블러링 : 가우시안 필터

# 평균값 필터에 의한 블러링의 단점
'''
- 필터링 대상 위치에서 가까이 있는 픽셀과 멀리 있는 픽셀이 모두
  같은 가중치를 사용하여 평균을 계산
- 멀리 있는 픽셀의 영향을 많이 받을 수 있음
# '''

# 2차원 가우시안 필터 마스크 (σ = 1.0)
'''- 필터 마스크 크기 : (8σ + 1) 또는 (6σ + 1)'''

# 가우시안 필터링 함수
'''
cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None,
                borderType=None) -> dst

- src : 입력 영상 (각 채널 별로 처리됨)
- dst : 출력 영상 (src와 같은 크기, 같은 타입)
- ksize : 가우시안 커널 크기
    - (0, 0)을 지정하면 sigma 값에 의해 자동 결정됨
    - kernel 크기를 강제로 주는 경우가 있는데 그러지 않는 것이 좋다.
- sigmaX : x방향 sigma
- sigmaY : y방향 sigma (0이면 sigmaX와 같게 설정)
- borderType : 가장자리 픽셀 확장 방식
'''

# (예제)다양한 크기의 sigma를 사용한 가우시안 필터링

import sys
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image laod failed!')
    sys.exit()

for sigma in range(1, 6):
    dst = cv2.GaussianBlur(src, (0, 0), sigma)
    desc = f'sigma : {sigma}'
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
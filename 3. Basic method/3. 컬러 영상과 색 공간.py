# (색상)채널 분리
'''
cv2.split(m, mv=None) -> dst

- m : 다채널 영상
- mv : 출력 영상
- dst : 출력 영상의 리스트
'''

# (색상)채널 결합
'''
cv2.merge(mv, dst=None) -> dst

- mv : 입력 영상 리스트 또는 튜플
- dst : 출력 영상
'''

# 색 공간 변환 함수
'''
cv2.cvtColor(src, code, dst=None, dstCn = None) -> dst

- src : 입력 영상
- code : 색 변환 코드
    - cv2.COLOR_BGR2GRAY / cv2.COLOR_GRAY2BGR
    - cv2.COLOR_BGR2RGB / cv2.COLOR_RGB2BGR
    - cv2.COLOR_BGR2HSV / cv2.COLOR_HSV2BGR
    - cv2.COLOR_BGR2YCrCb / cv2.COLOR_YCrCb2BGR
- dstCn : 결과 영상의 채널 수(0이면 자동 결정)
- dst : 출력 영상
'''

# 색 공간 특징
'''
1. RGB2GRAY
 - 장점 : 데이터 저장 용량 감소, 데이터 처리 속도 향상
 - 단점 : 색상 정보 손실

2. HSV
 - Hue : 색상, 색의 종류
 - Saturation : 채도, 색의 탁하고 선명한 정도
 - Value : 명도, 빛의 밝기
 - HSV 값 범위
    - cv2.CV_8U 영상의 경우
        - 0 <= H <= 179
        - 0 <= S <= 255
        - 0 <= V <= 255

3. YCrCb
 - PAL, NTSC, SECAM 등의 컬러 비디오 표준에서 사용되는 색 공간
 - 영상의 밝기 정보와 색상 정보를 따로 분리하여 부호화
 - Y : 밝기 정보(luma)
 - Cr, Cb : 색차(chroma)
 - YCrCb 값 범위
    - cv2.CV_8U 영상의 경우
        - 0 <= Y <= 255
        - 0 <= Cr <= 255
        - 0 <= Cb <= 255
'''

# (예제) RGB 색상 평면 나누기

import cv2
import sys

src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

b, g, r = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow('b_plane', b)
cv2.imshow('g_plane', g)
cv2.imshow('r_plane', r)
cv2.waitKey()
cv2.destroyAllWindows()
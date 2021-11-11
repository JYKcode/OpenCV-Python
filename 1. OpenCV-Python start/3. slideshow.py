# Project : 이미지 슬라이드 쇼

# 구현 할 기능
'''
- 특정 폴더에 있는 이미지 파일 목록 읽기
- 이미지를 전체 화면으로 출력하기
- 일정 시간동안 이미지를 화면에 출력하고, 다음 이미지로 교체하기(무한루프)
'''

import sys
import glob
import cv2

# 1. 이미지 파일을 모두 img_files 리스트에 추가
img_files = glob.glob('.\\images\\*.jpg')

for x in img_files:
    print(x)

# 2. 전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(1000) == 27:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
# 트랙바 사용하기

# 트랙바 생성 함수
'''
cv2.createTrackbar(trackbarName, windowName, value, count, onChange) -> None

- trackbarName : 트랙바 이름
- windowName : 트랙바를 생성할 창 이름
- value : 트랙바 위치 초기값
- count : 트랙바 최댓값, 최솟값은 항상 0
- onChange : 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름
             트랙바 이벤트 콜백 함수는 다음 형식을 따름
             onChange(pos) -> None
'''

# (예제)트랙바를 이용한 그레이스케일 레벨 표현

import numpy as np
import cv2

def on_level_changed(pos):
    level = pos * 16
    if level >= 255:
        level = 255

    img[:, :] = level
    cv2.imshow('image', img)
    print(pos)

img = np.zeros((480, 640), np.uint8)

cv2.imshow('image', img)
cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)
cv2.waitKey()
cv2.destroyAllWindows()
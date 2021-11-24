# 마우스 이벤트 처리하기

# 마우스 이벤트 콜백함수 등록 함수
'''
cv2.setMouseCallback(windowName, onMouse, param=None) -> None

- windowName : 마우스 이벤트 처리를 수행할 창 이름
- onMouse : 마우스 이벤트 처리를 위한 콜백 함수
            마우스 이벤트 콜백 함수는 다음 형식을 따라야 함.
            onMouse(event, x, y, flags, param) -> None
- param : 콜백 함수에 전달할 데이터
'''

# 마우스 이벤트 처리 함수(콜백 함수)형식
'''
onMouse(event, x, y, flags, param) -> None

- event : 마우스 이벤트 종류, cv2.EVENT_로 시작하는 상수
- x : 마우스 이벤트가 발생한 x 좌표
- y : 마우스 이벤트가 발행한 y 좌표
- flags : 마우스 이벤트 발생 시 상태, cv2.EVENT_FLAG_로 시작하는 상수
- param : cv2.setMouseCallback() 함수에서 설정한 데이터
'''

# (예제) 마우스를 이용한 그리기

import sys
import cv2
import numpy as np

oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print(f'EVENT_LBUTTONDOWN: {x}, {y}')
    elif event == cv2.EVENT_LBUTTONUP:
        oldx, oldy = x, y
        print(f'EVENT_LBUTTONUP: {x}, {y}')
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON: # '==' 이 아닌 '&'을 사용해야한다.
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.setMouseCallback('image', on_mouse)
cv2.waitKey()
cv2.destroyAllWindows()
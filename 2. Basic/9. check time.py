# TickMeter 클래스를 이용한 연산 시간 측정
'''
cv2.TickMeter() -> tm

- tm : cv2.TickMeter 객체
- tm.start() : 시간 측정 시작
- tm.stop() : 시간 측정 끝
- tm.reset() : 시간 측정 초기화
- tm.getTimeSec() : 측정 시간을 초 단위로 반환
- tm.getTimeMilli() : 측정 시간을 밀리 초 단위로 반환
- tm.getTimeMicro() : 측정 시간을 마이크로 초 단위로 반환
'''

# (예제) 특정 연산의 시간 측정 예제

import sys
import cv2

img = cv2.imread('hongkong.jpg')

if img is None:
    print('Image load failed!')
    sys.exit()

tm = cv2.TickMeter()

tm.start()
edge = cv2.Canny(img, 50, 150)
tm.stop()

ms = tm.getTimeMilli()

print(f'Elapsed time: {ms}ms')
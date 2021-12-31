# 키보드 이벤트 처리하기

# 키보드 입력 대기 함수
'''
cv2.waitKey(delay=None) -> retval

- delay : 밀리초 단위 대기 시간, delay <= 0 이면 무한히 기다림(기본값 : 0)
- retval : 눌린 키 값, 키가 눌리지 않으면 -1
- 참고사항
  - cv2.waitKey() 함수는 OpenCV 창이 하나라도 있을 때 동작함
  - 특정 키 입력을 확인하려면 ord()함수를 이용

  while True:
    if cv2.waitKey() == ord('q'):
      break

  - 주요 특수키 코드 : 27(ESC), 13(ENTER), 9(TAB)
'''

import sys
import cv2

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', src)

while True:
    key = cv2.waitKey()
    if key == 27:
        break
    elif key == ord('i') or key == ord('I'):
        src = ~src
        cv2.imshow('image', src)

cv2.destroyAllWindows()
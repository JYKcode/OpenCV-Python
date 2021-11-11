# 기본적인 cv2의 함수에 대한 설명

# cv2.imread()
'''
cv2.imread(filename, flags=None) -> retval
- filename : 불러올 영상 파일 이름(문자열)
- flags : 영상 파일 불러오기 옵션 플래그
    - cv2.IMREAD_COLOR : BGR 컬러 영상으로 읽기(기본값)
    - cv2.IMREAD_GRAYSCALE : 그레이스케일 영상으로 읽기
    - cv2.IMREAD_UNCHANGED : 영상 파일 속성 그대로 읽기
                             (e.g.) 투명한 PNG 파일 : shape = (rows, cols, 4)
- retval : 불러온 영상 데이터(numpy.ndarray)
'''

# cv2.imwrite()
'''
cv2.imwrite(filename, img, params=None) -> retval
- filename : 저장할 영상 파일 이름(문자열)
- img : 저장할 영상 데이터(numpy.ndarray)
- params : 파일 저장 옵션 지정(속성 & 값의 정수 쌍)
           (e.g.) [cv2.IMWRITE_JPEG_QUALITY, 90] : JPG 파일 압축률을 90%로 지정
- retval : 정상적으로 저장하면 True, 실패하면 False
'''

# cv2.namedWindow()
'''
cv2.namedWindow(winname, flags=None)
- winname : 창 고유 이름(문자열)
- flags : 창 속성 지정 플래그
    - cv2.WINDOW_NORMAL : 영상 크기를 창 크기에 맞게 지정 (영상이 너무 클때 사용하면 좋다)
    - cv2.WINDOW_AUTOSIZE : 창 크기를 영상 크기에 맞게 변경(기본값)
'''

# cv2.imshow()
'''
cv2.imshow(winname, mat)
- winname : 영상을 출력할 대상 창 이름
- mat : 출력할 영상 데이터(numpy.ndarray)
- 참고 사항
    - uint16, int32 자료형 행렬의 경우, 행렬 원소 값을 255로 나눠서 출력
    - float32, float64 자료형 행렬의 경우, 행렬 원소 값에 255를 곱해서 출력
    - 만약 winname에 해당하는 창이 없으면 창을 새로 만들어서 영상을 출력함
    - 실제로는 cv2.waitKey() 함수를 호출해야 화면에 영상이 나타남
'''

# cv2.waitKey()
'''
cv2.waitKey(delay=None) -> retval
- delay : 밀리초 단위 대기 시간. delay <= 0 이면 무한히 기다림. 기본값은 0
- retval : 눌린 키 값, 키가 눌리지 않으면 -1
- 참고사항
    - cv2.waitKey() 함수는 OpenCV 창이 하나라도 있을 때 동작함
    - 특정 키 입력을 확인하려면 ord()함수를 이용 (ESC = 27, Enter = 13, Tab = 9)
    while True:
        if cv2.waitKey() == ord('q'):
            break
'''

# cv2.destroyAllWindows()
'''
cv2.destroyWindow(winname) -> None
cv2.destroyAllWindows() -> None
- winname : 닫고자 하는 창 이름
- 참고사항
    - cv2.destroyWindow() 함수는 지정한 창 하나만 닫고, cv2.destroyAllWindows() 함수는
      열려 있는 모든 창을 닫음
'''

import sys
import cv2

print('Hello OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.imwrite('cat_gray.png', img)
cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
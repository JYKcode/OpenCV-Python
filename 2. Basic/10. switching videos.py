# Project : 동영상 전환 이펙트
'''
- 두 동영상 클립 사이에 추가되는 애니메이션 효과
- fade-in, fade-out, dissolve, 밀기, 확대 등

[구현 할 기능]
- 두 개의 동영상 동시 열기
- 첫 번째 동영상의 마지막 N개 프레임과 두 번째 동영상의 처음 N개 프레임을 합성
- 합성된 영상을 동영상으로 저장하기
'''

import sys
import cv2
import numpy as np

# 1. 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('video1.mp4')
cap2 = cv2.VideoCapture('video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('Video open failed!')
    sys.exit()

# 2. 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2) # 2초만큼 겹쳐서 작업하기 위함

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('effect_frames:', effect_frames)
print('FPS:', fps)

delay = int(1000 / fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 3. 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 4. 1번 동영상 복사
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        print('frame read error!')
        sys.exit()

    out.write(frame1)
    print('.', end='')

    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

# 5. 1번 동영상 뒷부분과 2번 동영상 앞부분을 합성
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('frame read error!')
        sys.exit()

    # 합성
    dx = int(w / effect_frames) * i
    
    # effect : 밀어내기
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx] = frame2[:, 0:dx]
    frame[:, dx:w] = frame1[:, dx:w]

    # # effect : 디졸브
    # alpha = 1.0 - i / effect_frames
    # frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha, 0)

    out.write(frame)
    cv2.imshow('output', frame)
    cv2.waitKey(delay)
    
# 6. 2번 동영상을 복사
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print('frame read error!')
        sys.exit()

    out.write(frame2)
    print('.', end='')

    cv2.imshow('output', frame2)
    cv2.waitKey(delay)

print('\noutput.avi file is successfully generated')

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
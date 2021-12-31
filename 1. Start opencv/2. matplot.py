# Matplotlib을 이용한 영상 출력

import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
'''
 - 컬러 영상의 색상 정보가 RGB 순서이어야 함
 - cv2.imread()함수로 불러온 영상의 색상 정보는 BGR순서이므로 이를 RGB 순서로
   변경해야함 -> cv2.cvtColor()함수 이용
'''

img_bgr = cv2.imread('cat.bmp')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(img_rgb)
plt.show()

# 그레이스케일 영상 출력
img_gray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(img_gray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(img_rgb)
plt.subplot(122), plt.axis('off'), plt.imshow(img_gray, cmap='gray')
plt.show()
# Corner detection
import cv2
import numpy as np

img = cv2.imread('D.png')
# changing the color to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# finding the corners
# on what, how many edges to find, image quality, the minimum distance between the corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corner', img)
cv2.waitKey(0)

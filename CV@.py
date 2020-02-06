import cv2
import numpy as np

img = cv2.imread('bgsbu.jpg')

# cv2.rectangle(img, (0, 200), (600, 900), (255, 0, 0), 20)
# cv2.circle(img, (300, 250), 100, (0, 0, 255), 5)
cv2.imshow('image', img)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)

cv2.polylines(img, [pts], True, (0, 255, 0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'HUHAHAHA', (500, 130), font, 5, (0, 0, 255), 5, cv2.LINE_8)
cv2.waitKey(0)
cv2.destroyAllWindows()

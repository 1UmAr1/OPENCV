import cv2
import numpy as np

img = cv2.imread('bgsbu.jpg')
# anything above 12 will be 1 and anything below 12 wil be 0
retval, threshold = cv2.threshold(img, 12, 100, cv2.THRESH_BINARY)

# chainging img to grayscale
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscale, 12, 225, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('orignal', img)
cv2.imshow("threshold", threshold)
cv2.imshow("threshold2", threshold2)
cv2.imshow("gaus", gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
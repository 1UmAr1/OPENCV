import cv2
import numpy
import matplotlib.pyplot as plt

# Loading the image
img = cv2.imread("ME.jpg", cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()


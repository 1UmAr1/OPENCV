# Background reduction
# motion detection
import cv2

# Finds changes from previous frame and keeps the and removes similarities
cap = cv2.VideoCapture(0)
motion = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = motion.apply(frame)

    cv2.imshow('orignal', frame)
    cv2.imshow('fg', fgmask)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



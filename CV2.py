# object detection using Harr cascade

import cv2
import numpy as np

# loading in the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_g_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    # converting the video to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Using haarcascade
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    smile = smile_cascade.detectMultiScale(gray, 2, 30)

    # for x coordinate, y coordinate, width, height draw a rectangle
    for (x, y, w, h) in faces:
        # drawing rectangle based on the starting point and the ending point
        cv2.rectangle(img, (x, y), (x+y, y+h), (255, 0, 0), 2)
        # region of face, image
    #for(x, y, w, h) in smile:
        #cv2.rectangle(img, (x, y), (x+y, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # oi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # eyes_g = eye_g_cascade.detectMultiScale(roi_gray)
        # detecting the eyes on the bases of x, y coordinate and width and height and drawing a rectangle around it
        #for (ex, ey, ew, eh) in eyes_g:
            #cv2.rectangle(oi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) # line width
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # line width


    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()


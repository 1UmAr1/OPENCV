import cv2
import numpy as np

kangri_cascade = cv2.CascadeClassifier('kangri_cascade.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kangri = kangri_cascade.detectMultiScale(gray, 10, 10)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in kangri:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'kangri', (x-w, y-h), font, 0.5, (0, 255, 255, 2, cv2.LINE_AA))
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eyes_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
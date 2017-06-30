#-*- coding: utf-8 -*-

import cv2
import sys
import httplib, urllib, base64
import json
from math import floor
import sys,time

cv2.namedWindow("lookine")
cap = cv2.VideoCapture(0) 
cv2.waitKey(1000)
count = 0
emotion = 0
while True:
    ok, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('/Users/fatefaker/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    maxw = 0
    xx = 0
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if maxw<w:
            maxw = w
            xx = x
    control = img.shape[1]/2 - (xx+maxw/2)
    if maxw == 0:
        control = 0
    sys.stdout.write(' ' * 10 + '\r')
    sys.stdout.flush()
    sys.stdout.write(str(control) + '\r')
    sys.stdout.flush()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(control)+'Emotion: '+str(emotion) , (10, 500), font, 3, (0, 0, 255), 4,False)

    cv2.imshow("lookine", img)
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
   
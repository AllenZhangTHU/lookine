#-*- coding: utf-8 -*-

import cv2
import sys
import httplib, urllib, base64
import json
from math import floor
import sys,time
from  test_fppAPI import detect
import time, threading
import base64
import requests
import matplotlib.pyplot as plt


emotion = {}
plt.ion() 
def getEmotion(img):
    stime = time.time()
    img_bi = cv2.imencode('.jpg', img)[1]
    body = base64.b64encode(img_bi)
    # body = bytearray(img_bi)
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'multipart/form-data',
        'api_key':"sVGcopkVOZiulHag7dSp_QMLjKjtACxh",
        "api_secret":"6NBKvh_M09KH1d_93DBjw3gAOvp_qZl1",
        "return_attributes":"emotion",
        "image_base64":body
    }
    r = requests.post('https://api-cn.faceplusplus.com/facepp/v3/detect', data=headers)
    # print(r.json)
    
    # print(r.headers)
    global emotion
    emotion = eval(r.content)
    # print(emotion)
    print(time.time()-stime)
cv2.namedWindow("lookine")
cap = cv2.VideoCapture(0) 
cv2.waitKey(1000)
count = 0

while True:
    count+=1
    ok, img = cap.read()
    # getEmotion(img)
    if count % 10==0:
        t1 = threading.Thread(target=getEmotion, args=(img,))
        t1.start()
    # t1.join()
    # detect(image_file='timg.jpg')
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
    # sys.stdout.write(' ' * 10 + '\r')
    # sys.stdout.flush()
    # sys.stdout.write(str(control) + '\r')
    # sys.stdout.flush()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(control) , (10, 500), font, 3, (0, 0, 255), 4,False)
    cv2.imshow("lookine", img)
    try:
        emotionDict = emotion["faces"][0]["attributes"]["emotion"]
        print(emotionDict)
        data = emotionDict.values()
        labels = emotionDict.keys()
        plt.bar(range(len(data)), data, tick_label=labels)
        plt.draw()
    except Exception as e:
        # print("[Errno {0}] {1}".format(e.errno, e.strerror))
        pass
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 

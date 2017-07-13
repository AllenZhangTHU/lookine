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

import socket
import pygame

happinessT = 0
sadnessT = 0
surpriseT = 0
fearT = 0
disgustT = 0
angerT = 0

# pygame.init()
pygame.mixer.init()
# pygame.mixer.music.load('./audio/aus/扬眉.mp3')
# pygame.mixer.music.play()
# pygame.mixer.music.load('./audio/aus/皱眉.mp3')
# pygame.mixer.music.play()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 23333))
emotion = {}
qid = 0
rid = 0
plt.ion() 
def listentoCPP():
    while (True):
        data, addr = s.recvfrom(1024)
        type(data)
        print(data)
        try:
            #print type(data)
            #print type(data[0])
            if data[1] == '1':
                pygame.mixer.music.load('./audio/aus/扬眉.mp3')
                pygame.mixer.music.play()
                time.sleep(1.6)
                print('扬眉')
            if data[2] == '1':
                pygame.mixer.music.load('./audio/aus/皱眉.mp3')
                pygame.mixer.music.play()
                time.sleep(1.6)
                print('皱眉')
            if data[3] == '1':
                pygame.mixer.music.load('./audio/aus/嘴角上扬.mp3')
                pygame.mixer.music.play()
                time.sleep(2.1)
                print('嘴角上扬')
            if data[4] == '1':
                pygame.mixer.music.load('./audio/aus/嘴角下拉.mp3')
                pygame.mixer.music.play()
                time.sleep(2.1)
                print('嘴角下拉')
            if data[5] == '1':
                pygame.mixer.music.load('./audio/aus/下巴皱起.mp3')
                pygame.mixer.music.play()
                time.sleep(2.1)
                print('下巴皱起')
            if data[6] == '1':
                pygame.mixer.music.load('./audio/aus/嘴巴收紧.mp3')
                pygame.mixer.music.play()
                time.sleep(2.1)
                print('嘴巴收紧')
            if data[7] == '1':
                pygame.mixer.music.load('./audio/aus/张大嘴.mp3')
                pygame.mixer.music.play()
                time.sleep(1.6)
                print('张大嘴')
        except Exception as e:
        # print("[Errno {0}] {1}".format(e.errno, e.strerror))
            pass
t = threading.Thread(target=listentoCPP, args=())
t.start()

def getEmotion(img,qid):
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
    global rid
    if (qid >= rid)and(not eval(r.content).has_key("error_message")):
        emotion = eval(r.content)
        rid = qid
    # print(emotion)
    # print(time.time()-stime)
cv2.namedWindow("lookine")
cap = cv2.VideoCapture(0) 
cv2.waitKey(1000)
count = 0


MARGIN = 50
MOVEUNIT = 5
device = '/dev/ttyUSB0'
MAX_TIME_SLICE = 10
time_slice = 0

try:
    arduino = serial.Serial(device, 9600)
except:
    # print 'Failed to connect on ' + device
    pass
while True:
    count+=1
    ok, img = cap.read()
    # getEmotion(img)
    if count % 1==0:
        qid += 1
        t1 = threading.Thread(target=getEmotion, args=(img,qid))
        t1.start()
    # t1.join()
    # detect(image_file='timg.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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
    if time_slice == 0:
        if (abs(control) >= MARGIN):
            time_slice = MAX_TIME_SLICE
            control /= abs(control)
            control *= MOVEUNIT
            try:
                arduino.write(str(control))
                time.sleep(1)
                # print arduino.readline()
            except:
                # print 'Failed to send'
                pass
    else:
        time_slice -= 1
    # sys.stdout.write(' ' * 10 + '\r')
    # sys.stdout.flush()
    # sys.stdout.write(str(control) + '\r')
    # sys.stdout.flush()


    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(control) , (10, 500), font, 3, (0, 0, 255), 4,False)
    cv2.imshow("lookine", img)
    try:
        emotionDict = emotion["faces"][0]["attributes"]["emotion"]
        # print(len(emotion["faces"]))
        # print(emotionDict)
        happiness = emotionDict['happiness']
        if (happiness >80):
            happinessT += 1
        else:
            happinessT = 0
        if (happinessT == 3):
            pygame.mixer.music.load('./audio/expressions/happiness.mp3')
            pygame.mixer.music.play()
            time.sleep(1.6)

        sadness = emotionDict['sadness']
        if (sadness >80):
            sadnessT += 1
        else:
            sadnessT = 0
        if (sadnessT == 3):
            pygame.mixer.music.load('./audio/expressions/sadness.mp3')
            pygame.mixer.music.play()
            time.sleep(1.6)

        surprise = emotionDict['surprise']
        if (surprise >80):
            surpriseT += 1
        else:
            surpriseT = 0
        if (surpriseT == 3):
            pygame.mixer.music.load('./audio/expressions/surprise.mp3')
            pygame.mixer.music.play()
            time.sleep(1.6)

        fear = emotionDict['fear']
        if (fear >80):
            fearT += 1
        else:
            fearT = 0
        if (fearT == 3):
            pygame.mixer.music.load('./audio/expressions/fear.mp3')
            pygame.mixer.music.play()
            time.sleep(1.6)

        disgust = emotionDict['disgust']
        if (disgust >50):
            disgustT += 1
        else:
            disgustT = 0
        if (disgustT == 3):
            pygame.mixer.music.load('./audio/expressions/disgust.mp3')
            pygame.mixer.music.play()
            time.sleep(1.6)

        anger = emotionDict['anger']
        if (anger >50):
            angerT += 1
        else:
            angerT = 0
        if (angerT == 3):
            pygame.mixer.music.load('./audio/expressions/anger.mp3')
            pygame.mixer.music.play()
            time.sleep(1.6)

        data = emotionDict.values()
        labels = emotionDict.keys()
        plt.cla()
        plt.ylim((0,100))
        plt.bar(range(len(data)), data, tick_label=labels)
        plt.draw()
    except Exception as e:
        # print("[Errno {0}] {1}".format(e.errno, e.strerror))
        pass
    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 
s.close()

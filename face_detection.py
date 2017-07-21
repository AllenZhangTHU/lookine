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
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import json
import socket
import pygame
import serial

happinessT = 0
sadnessT = 0
surpriseT = 0
fearT = 0
disgustT = 0
angerT = 0
auT = [0,0,0,0,0,0,0,0,0,0]

emotionOn = True
auOn = True
speed = 1
autoOn = True
onceOn = False
PORT_NUMBER = 8006

f = open('results.txt', 'w')
f.write('start'+'\n')
f.close()


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        global emotionOn
        global auOn
        global autoOn
        global onceOn
        global speed
        if self.path=="/":
            print "refresh"
            self.path="/index.html"
            emotionOn = True
            auOn = False
            autoOn = False
            onceOn = False
            speed = 1
        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".png"):
                mimetype='image/png'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            if self.path.endswith(".map"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path) 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
    def do_POST(self):
        global emotionOn
        global auOn
        global autoOn
        global onceOn
        global speed
        print self.path
        length = int(self.headers['content-length'])
        request_str = self.rfile.read(length)
        reqDict = json.loads(request_str)
        # print reqDict
        reqCmd = reqDict['detail']
        print reqCmd
        if reqCmd == "emotion":
            emotionOn = True
            auOn = False
        if reqCmd =="au":
            emotionOn = False
            auOn = True
        if reqCmd == "both":
            emotionOn = True
            auOn = True
        if reqCmd == "normal":
            speed = 1
        if reqCmd == "1.5times":
            speed = 2
        if reqCmd == "2times":
            speed = 3
        if reqCmd == "once":
            autoOn = False
        if reqCmd == "stopauto":
            autoOn = False
        if reqCmd == "startauto":
            autoOn = True
        if reqCmd == "doonce":
            onceOn = True
        resDict = {"result":"ok"}
        resJson = json.dumps(resDict)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(resJson)
def runserver(portNum):
    try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', portNum), myHandler)
        print 'Started httpserver on port ' , PORT_NUMBER
        #Wait forever for incoming htto requests
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()


t = threading.Thread(target=runserver, args=(PORT_NUMBER,))
t.start()


# pygame.init()
pygame.mixer.init()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 23333))

# s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
            for i in range(1,10):
                auT[i] += 1
                if data[i] == '0':
                    auT[i] = 0
            if auOn:
                if autoOn:
                    if auT[1] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/扬眉.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/扬眉2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/扬眉3.mp3')
                        pygame.mixer.music.play()
                        print('扬眉')
                    if auT[2] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/皱眉.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/皱眉2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/皱眉3.mp3')
                        pygame.mixer.music.play()
                        print('皱眉')
                    if auT[3] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/嘴角上扬.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/嘴角上扬2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/嘴角上扬3.mp3')
                        pygame.mixer.music.play()
                        print('嘴角上扬')
                    if auT[4] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/嘴角下拉.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/嘴角下拉2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/嘴角下拉3.mp3')
                        pygame.mixer.music.play()
                        print('嘴角下拉')
                    if auT[5] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/下巴皱起.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/下巴皱起2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/下巴皱起3.mp3')
                        pygame.mixer.music.play()
                        print('下巴皱起')
                    if auT[6] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/嘴巴收紧.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/嘴巴收紧2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/嘴巴收紧3.mp3')
                        pygame.mixer.music.play()
                        print('嘴巴收紧')
                    if auT[7] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/张大嘴.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/张大嘴2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/张大嘴3.mp3')
                        pygame.mixer.music.play()
                        print('张大嘴')
                    if auT[8] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/点头.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/点头2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/点头3.mp3')
                        pygame.mixer.music.play()
                        print('点头')
                    if auT[9] == 3:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/摇头.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/摇头2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/摇头3.mp3')
                        pygame.mixer.music.play()
                        print('摇头')
                if onceOn:
                    if auT[1] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/扬眉.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/扬眉2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/扬眉3.mp3')
                        pygame.mixer.music.play()
                        print('扬眉')
                    if auT[2] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/皱眉.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/皱眉2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/皱眉3.mp3')
                        pygame.mixer.music.play()
                        print('皱眉')
                    if auT[3] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/嘴角上扬.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/嘴角上扬2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/嘴角上扬3.mp3')
                        pygame.mixer.music.play()
                        print('嘴角上扬')
                    if auT[4] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/嘴角下拉.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/嘴角下拉2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/嘴角下拉3.mp3')
                        pygame.mixer.music.play()
                        print('嘴角下拉')
                    if auT[5] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/下巴皱起.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/下巴皱起2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/下巴皱起3.mp3')
                        pygame.mixer.music.play()
                        print('下巴皱起')
                    if auT[6] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/嘴巴收紧.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/嘴巴收紧2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/嘴巴收紧3.mp3')
                        pygame.mixer.music.play()
                        print('嘴巴收紧')
                    if auT[7] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/张大嘴.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/张大嘴2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/张大嘴3.mp3')
                        pygame.mixer.music.play()
                        print('张大嘴')
                    if auT[8] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/点头.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/点头2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/点头3.mp3')
                        pygame.mixer.music.play()
                        print('点头')
                    if auT[9] > 0:
                        while pygame.mixer.music.get_busy():
                            time.sleep(1)
                        if speed == 1:
                            pygame.mixer.music.load('./audio/aus/摇头.mp3')
                        if speed == 2:
                            pygame.mixer.music.load('./audio/aus/摇头2.mp3')
                        if speed == 3:
                            pygame.mixer.music.load('./audio/aus/摇头3.mp3')
                        pygame.mixer.music.play()
                        print('摇头')
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
device = '/dev/tty.wchusbserial1460'
MAX_TIME_SLICE = 10
time_slice = 0

# ser = serial.Serial('/dev/tty.wchusbserial1460', 9600)

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
                ser.write(str(control))
                time.sleep(1)
                print ser.readline()
            except:
                print 'Failed to send'
                pass
    else:
        time_slice -= 1
    # sys.stdout.write(' ' * 10 + '\r')
    # sys.stdout.flush()
    # sys.stdout.write(str(control) + '\r')
    # sys.stdout.flush()


    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(control) , (10, 500), font, 3, (0, 0, 255), 4,False)
    # cv2.imshow("lookine", img)
    try:
        if emotionOn:
            emotionDict = emotion["faces"][0]["attributes"]["emotion"]
            happiness = emotionDict['happiness']
            sadness = emotionDict['sadness']
            surprise = emotionDict['surprise']
            fear = emotionDict['fear']
            disgust = emotionDict['disgust']
            anger = emotionDict['anger']
            neutral = emotionDict['neutral']

            # s2.sendto(str([neutral,happiness,sadness,surprise,fear,disgust,anger]), ('127.0.0.1', 23334))

            f = open('results.txt', 'a+')
            f.write(str([neutral,happiness,sadness,surprise,fear,disgust,anger])+'\n')
            f.close()

            if autoOn:
                if (happiness >75):
                    happinessT += 1
                else:
                    happinessT = 0
                if (happinessT == 3):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/happiness.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/happiness2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/happiness3.mp3')
                    pygame.mixer.music.play()

                if (sadness >75):
                    sadnessT += 1
                else:
                    sadnessT = 0
                if (sadnessT == 3):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/sadness.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/sadness2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/sadness3.mp3')
                    pygame.mixer.music.play()

                if (surprise >75):
                    surpriseT += 1
                else:
                    surpriseT = 0
                if (surpriseT == 3):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/surprise.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/surprise2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/surprise3.mp3')
                    pygame.mixer.music.play()

                if (fear >75):
                    fearT += 1
                else:
                    fearT = 0
                if (fearT == 3):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/fear.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/fear2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/fear3.mp3')
                    pygame.mixer.music.play()

                if (disgust >50):
                    disgustT += 1
                else:
                    disgustT = 0
                if (disgustT == 3):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/disgust.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/disgust2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/disgust3.mp3')
                    pygame.mixer.music.play()

                if (anger >50):
                    angerT += 1
                else:
                    angerT = 0
                if (angerT == 3):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/anger.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/anger2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/anger3.mp3')
                    pygame.mixer.music.play()
            if onceOn:
                onceOn = False
                if (happiness >75):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/happiness.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/happiness2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/happiness3.mp3')
                    pygame.mixer.music.play()
                if (sadness >75):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/sadness.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/sadness2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/sadness3.mp3')
                    pygame.mixer.music.play()
                if (surprise >75):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/surprise.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/surprise2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/surprise3.mp3')
                    pygame.mixer.music.play()
                if (fear >75):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/fear.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/fear2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/fear3.mp3')
                    pygame.mixer.music.play()
                if (disgust >50):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/disgust.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/disgust2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/disgust3.mp3')
                    pygame.mixer.music.play()
                if (anger >50):
                    while pygame.mixer.music.get_busy():
                            time.sleep(1)
                    if speed == 1:
                        pygame.mixer.music.load('./audio/expressions/anger.mp3')
                    if speed == 2:
                        pygame.mixer.music.load('./audio/expressions/anger2.mp3')
                    if speed == 3:
                        pygame.mixer.music.load('./audio/expressions/anger3.mp3')
                    pygame.mixer.music.play()


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

#-*- coding: utf-8 -*-

import cv2
import sys
import httplib, urllib, base64
import json
from math import floor

cv2.namedWindow("lookine")
cap = cv2.VideoCapture(0) 
cv2.waitKey(1000)
count = 0
while True:
    ok, frame = cap.read()
    cv2.imshow("lookine", frame)
    if (count % 50 == 0):
        headers = {
            # Request headers. Replace the placeholder key below with your subscription key.
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': '2ae1b8728aba40a7bfe321a9aaa0703f',
        }

        params = urllib.urlencode({
        })
        img_bi = cv2.imencode('.jpg', frame)[1]

        body = bytearray(img_bi)

        try:
            # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
            #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
            #   URL below with "westcentralus".
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()
            data = json.loads(data)
            data = data[0]["scores"]
            d = floor(data["anger"] / 0.02)
            print "ANGER\t" + "#" * int(d)
            d = floor(data["contempt"] / 0.02)
            print "COMTEMPT\t" + "#" * int(d)
            d = floor(data["disgust"] / 0.02)
            print "DISGUST\t" + "#" * int(d)
            d = floor(data["fear"] / 0.02)
            print "FEAR\t" + "#" * int(d)
            d = floor(data["happiness"] / 0.02)
            print "HAPPINESS\t" + "#" * int(d)
            d = floor(data["neutral"] / 0.02)
            print "NEUTRAL\t" + "#" * int(d)
            d = floor(data["sadness"] / 0.02)
            print "SADNESS\t" + "#" * int(d)
            print '-' * 70
            print '\n'

            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
    count += 1
        c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 

import cv2
import sys
import httplib, urllib, base64

cv2.namedWindow("lookine")
cap = cv2.VideoCapture(0) 
cv2.waitKey(1000)
ok, frame = cap.read()
cv2.imshow("lookine", frame)
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
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

cv2.waitKey()
cap.release()
cv2.destroyAllWindows() 
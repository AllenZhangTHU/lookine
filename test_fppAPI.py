import os
import json
import time
from subprocess import Popen,PIPE
api_key="sVGcopkVOZiulHag7dSp_QMLjKjtACxh"
api_secret="6NBKvh_M09KH1d_93DBjw3gAOvp_qZl1"

def detect(image_file,return_landmark=0):
    while 1:
        #time1 = time.time()
        result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/detect" -F \
            "api_key={api_key}" -F \
            "api_secret={api_secret}" -F \
            "image_file=@{image_file}" -F \
            "return_attributes=emotion" -F \
            "return_landmark={return_landmark}"'
            .format(api_key=api_key,api_secret=api_secret,image_file=image_file,return_landmark=return_landmark),shell=True,stdout=PIPE)
        wait=""
        result=(result.stdout.read())
        with open("detect.json".format(path=path),"w+") as f:
            f.write(result)
        with open("detect.json".format(path=path)) as f:
            result=json.load(f)
        #os.remove('detect.json'.format(path=path))
        #time2 = time.time()
        #print time2 - time1
    return result

if __name__ == '__main__':
    result = detect(image_file='timg.jpg')
    
#! /usr/bin/python
# -*- coding: utf-8 -*-

import picamera
import time
from datetime import datetime

filepath = '/home/pi/sugi-pg/personal-program/images/'

def take_pic_from_picamera(filename):
    with picamera.PiCamera() as camera:
     time.sleep(2)
#     filepath='/home/pi/sugi-pg/personal-program/images/'+filename
     camera.capture(filename)
     print("done")

# main
timestr = datetime.now().strftime('%Y%m%d%H%M%S')
filename=filepath+timestr+'.jpg'
print filename
take_pic_from_picamera(filename)
#upload_to_S3(filename)

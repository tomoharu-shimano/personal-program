#! /usr/bin/python
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time
import picamera
from datetime import datetime
import requests

# mesure distance
def checkdist():
	GPIO.output(16, GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(16, GPIO.LOW)
	while not GPIO.input(18):
		pass
	t1 = time.time()
	while GPIO.input(18):
		pass
	t2 = time.time()
	return (t2-t1)*340/2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.IN)
time.sleep(2)

# take photo
def take_pic_from_picamera(filename):
	with picamera.PiCamera() as camera:
		time.sleep(2)
		camera.capture(filename)

# line_notify 
def line_notify():

	url = 'https://notify-api.line.me/api/notify'
	img_file_path = '/home/pi/sugi-pg/personal-program/images/images.jpg'

	# My Line Token
	access_token = 'nYZ6K83tkeHSjalO3Rh9xJyYjN5zi4WJsajGWm85d05'
	headers = {
	'Authorization': 'Bearer ' + access_token
	}

	message = 'Tora Comming!'
	payload = {'message': message}
	files = {'imageFile': open(img_file_path, 'rb')}
	response = requests.post(url, headers=headers, params=payload, files=files,)


# main

sensor_distance = 0.5

filename = '/home/pi/sugi-pg/personal-program/images/images.jpg'
#timestr = datetime.now().strftime('%Y%m%d%H%M%S')
#filename=filepath+timestr+'.jpg'

try:
        while True:
               # print 'Distance: %0.2f m' %checkdist()

                if checkdist() < sensor_distance:
                        print 'check line'
			take_pic_from_picamera(filename)
			line_notify()
                else:
                        print 'over 0.5m'
                time.sleep(10)

except KeyboardInterrupt:
        GPIO.cleanup()

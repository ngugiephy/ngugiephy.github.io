#import libraries
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import datetime
import time
import ftplib
import requests
from subprocess import call
import sys #for pubnub
from pubnub import Pubnub #for pubnub too

#pubnub setup
pubnub = Pubnub(publish_key = 'pub-c-1afde382-1404-4079-9139-8196509ba945', subscribe_key="sub-c-f2b8c5c0-c34b-11e5-b684-02ee2ddab7fe")
channel = "sensor-scans"
data_init = {
	'username': 'ngugiephy',
	'message': 'system initiated'
}
data_vs = {
	'username': 'ngugiephy',
	'message': 'vibration sensor triggered'
}
data_ts = {
	'username': 'ngugiephy',
	'message': 'trap sensor triggered'
}
data_ts_vs = {
	'username': 'ngugiephy', 
	'message': 'both traps and vibration sensors triggered'
}

#pubnub callback
def callback(m):
	print(m)
#pubnub publish?
pubnub.publish(channel, data_init, callback=callback, error=callback)

#camera capture
def camera():
	global filename
	filename = get_filename()
	print filename
	time.sleep(1)
	call(["fswebcam", "-r", "1000x800", "--no-banner", filename])

def get_filename():
	return datetime.datetime.now().strftime("sys-%Y-%m-%d_%H:%M:%S.jpg")

def upload_ftp():
	print "file to be uploaded:" + filename
	ftp.storbinary('STOR ' + filename, open(filename, 'rb')) 

def login_ftp():
	global ftp
	ftp = ftplib.FTP("213.168.249.180")
	ftp.login("raspi", "raspberry")
	print "logged in to ftp"

def logout_ftp():
	ftp.quit()
	print "logged out of ftp"

def actuators_on():
	GPIO.output(srn, True)
	GPIO.output(stb, True)

def actuators_off():
	GPIO.output(srn, False)
	GPIO.output(stb, False)

#sensors define
#
#vibration sensors
vs1 = 18
vs2 = 17
vs3 = 27
vs4 = 22 
#trap sensors
ts1 = 6
ts2 = 13
ts3 = 19
ts4 = 26
#actuators define
stb = 2
srn = 3

#GPIOsetup_sensors
GPIO.setup(vs1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(vs2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(vs3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(vs4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ts1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ts2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ts3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ts4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIOsetup_actuators
GPIO.setup(stb, GPIO.OUT)
GPIO.setup(srn, GPIO.OUT)
GPIO.output(stb, False)
GPIO.output(srn, False)

#while True:
#	for i in range(5):
#		#take picture
#		camera()
#		#login to ftp
#		login_ftp()
#		#upload to ftp
#		upload_ftp()
#		#logout of ftp
#		logout_ftp()
#		print '''\n\n''' 
#		print "uploaded file " + str(i) + " to server"
#		print '''\n\nWaiting 7 seconds'''
#		time.sleep(7)

while True:
	#send pubnub initialization message
		#have a counter that sends a message after 30 loops
	#poll sensors
	#try:
	vs1_in = GPIO.input(vs)
	vs2_in = GPIO.input(vs)
	vs3_in = GPIO.input(vs)
	vs4_in = GPIO.input(vs)


	ts1_in = GPIO.input(ts)
	ts2_in = GPIO.input(ts)
	ts3_in = GPIO.input(ts)
	ts4_in = GPIO.input(ts)
	if (vs1_in == 0 or vs2_in == 0 or vs3_in == 0 or vs4_in == 0) and (ts1_in == 0 or ts2_in == 0 or ts3_in == 0 or ts4_in == 0):
		pubnub.publish(channel, data_ts_vs, callback=callback, error=callback)
		actuators_on()
		camera()
		login_ftp()
		upload_ftp()
		logout_ftp()
	elif (ts1_in == 0 or ts2_in == 0 or ts3_in == 0 or ts4_in == 0):
		pubnub.publish(channel, data_ts, callback=callback, error=callback)
		actuators_on()
		camera()
		login_ftp()
		upload_ftp()
		logout_ftp()
	elif (vs1_in == 0 or vs2_in == 0 or vs3_in == 0 or vs4_in == 0) 
		pubnub.publish(channel, data_vs, callback=callback, error=callback)
		actuators_on()
		camera()
		login_ftp()
		upload_ftp()
		logout_ftp()

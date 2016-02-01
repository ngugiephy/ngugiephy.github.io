#import libraries
import RPi.GPIO as GPIO
import datetime
import time
import ftplib
import requests
from subprocess import call

#camera capture
def camera():
	global filename
	filename = get_filename()
	print filename
	time.sleep(1)
	call(["fswebcam", "-r", "1000x800", "--no-banner", filename])

def get_filename():
	return datetime.datetime.now().strftime("NGUGI-TEST_%Y-%m-%d_%H:%M:%S.jpg")

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


while True:
	for i in range(5):
		#take picture
		camera()
		#login to ftp
		login_ftp()
		#upload to ftp
		upload_ftp()
		#logout of ftp
		logout_ftp()
		print '''\n\n''' 
		print "uploaded file " + str(i) + " to server"
		print '''\n\nWaiting 7 seconds'''
		time.sleep(7)


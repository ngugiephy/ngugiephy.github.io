#import libraries
import os
import time
import subprocess
from subprocess import call
import datetime
import ftplib

def camera():
	global filename
	filename = get_filename()	
	#print filename 			#for testing puproses only

	#
	call(["fswebcam", "-r", "1000x800", "--no-banner", filename])
	time.sleep(2)

#datestamps the filenames
#	format: year, month, date, hour, minute, seconds 2016-04-06_11:30.jpg
def get_filename():
	return datetime.datetime.now().strftime("%Y-%m-%d_%H:%M.jpg")
	#return datetime.datetime.now().strftime("sys-%Y-%m-%d_%H:%M:%S.jpg")


def login_ftp():
	global ftp
	ftp = ftplib.FTP("213.168.249.180")
	ftp.login("raspi", "raspberry")
	print "logged in to ftp"

def upload_ftp():
	print "file to be uploaded:" + filename
	ftp.storbinary('STOR ' + filename, open(filename, 'rb')) 


def logout_ftp():
	ftp.quit()
	print "logged out of ftp"



#try: 
	##camera capture and upload with 10 streams
#for i in range(2):
camera()
login_ftp()
upload_ftp()
logout_ftp()
time.sleep(1)
#except:
#	print "didnt upload"

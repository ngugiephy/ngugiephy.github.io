import os 
import ftplib
from pubnub import Pubnub
import requests
import time
import re
import subprocess

pubnub = Pubnub(publish_key = 'pub-c-1afde382-1404-4079-9139-8196509ba945', subscribe_key="sub-c-f2b8c5c0-c34b-11e5-b684-02ee2ddab7fe")
channel = "updater2"
data_update_found = {
	'message': 'update found'
}
data_update_done = {
	'message': 'update done'
}
data_start = {
	'message': 'system started'
}
data_stop = {
	'message': 'system stopped'
}
data_reboot = {
	'message': 'rebooting system'
}

def callback(m):
	print m

def check_update():
	r = requests.get('http://dalcom.info/kplc/request.php?rq=1')
	print r.text
	return r.text

def ftp_login():
	global ftp
	ftp = ftplib.FTP('213.168.249.180')
	ftp.login('raspi', 'raspberry')

def update_file():
	global ftp
	filename = 'updater.update'
	localfile = open(filename, 'wb')
	ftp.retrbinary('retr ' + filename, localfile.write, 1024)
	ftp.quit()
	localfile.close()
	os.system('mv /home/pi/Desktop/full-sysytem/updater.update /home/pi/Desktop/full-system/updater.py')

def kill_updater():
	val = os.popen('ps aux | grep updater.py').read()
	res = val.split()
	print res[1]
	kill_val = 'kill ' + res[1]
	os.system(kill_val)
	time.sleep(2)

def kill_watchdog():
	val = os.popen('ps aux | grep watchdog.py').read()
	res = val.split()
	kill_val = 'kill ' + res[1]
	os.system(kill_val)
	time.sleep(2)

def run_updater():
	os.system('python updater.py &')

def run_watchdog():
	os.system('python watchdog.py &')

def restart_sys():
	os.system('sudo reboot')

def kill_watchdog():
	val = os.popen('ps aux | grep watchdog.py').read()
	res = val.split()
	print res[1]
	kill_val = 'kill ' + res[1]
	os.system(kill_val)
	time.sleep(2)

def run_watchdog():
	os.system('python watchdog.py &')

#kill_watchdog()
#time.sleep(0.5)
#run_watchdog()

count = 0; #counter for starting and stopping watchdog
while True:
	action = check_update()
	print action
	if (action == 'update_updater'):
		print 'the action right now is: %s' % action
#		pubnub.publish(channel, data_update_found, callback=callback, error=callback)
		kill_watchdog()
		kill_updater()
		ftp_login()
		update_file()
		run_watchdog()
#		pubnub.publish(channel, data_update_done, callback=callback, error=callback)
		time.sleep(10)
	elif (action == 'stop_updater'):
		print 'the action right now is: %s' % action
		#stop program
		kill_watchdog()
#		pubnub.publish(channel, data_stop, callback=callback, error=callback)
		time.sleep(5)
	elif (action == 'start_updater'):
		print 'the action right now is: %s' % action
		run_watchdog()
		time.sleep(5)		
#		pubnub.publish(channel, data_start, callback=callback, error=callback)
#	elif (action == 'reboot'):
#		print 'the action right now is: %s' % action
#		time.sleep(5)
#		restart_sys()
#		pubnub.publish(channel, data_reboot, callback=callback, error=callback)
	else:
		print 'nothing to see here'

	time.sleep(1)
	count += 1
	print 'the count is : %d' % count
	if (count == 60):
		run_watchdog()
		break

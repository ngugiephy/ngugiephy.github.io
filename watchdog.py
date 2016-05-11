import re
import time
from pubnub import Pubnub
import os

pubnub = Pubnub(publish_key = 'pub-c-1afde382-1404-4079-9139-8196509ba945', subscribe_key="sub-c-f2b8c5c0-c34b-11e5-b684-02ee2ddab7fe")
channel = "watchdog"
data_running = {
	'message': 'updater running'
}
data_stopped = {
	'message': 'updater stopped'
}

def kill_prog():
	state  = os.system('ps -ef | grep updater.py | wc -l')
	val = os.popen('ps -ef | grep updater.py').read()
	res = val.split()
	print res[1]
	kill_val = 'kill ' + res[1]
	os.system(kill_val)
	time.sleep(1)

def run_prog():
	os.system('python /home/pi/Desktop/full-system/updater.py')

def callback(m):
	print(m)


while True:
	time.sleep(2)
	kill_prog()
	print "program killed"
#	pubnub.publish(channel, data_stopped, callback=callback, error=callback)
	time.sleep(3)
	print "running program"
	run_prog()
	print "just exited from program..."
#	pubnub.publish(channel, data_running, callback=callback, error=callback)



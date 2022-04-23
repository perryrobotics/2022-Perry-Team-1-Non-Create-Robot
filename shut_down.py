#!/usr/bin/python
import os, sys
import ctypes
import time

#File:  shutdown.py
#Purpose:  Contains python routines to shut the robot down ibn 2 minutes
#Writte by:  Perry Team 1 (2022)

KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
    
def shut_down():
	print("starting shut_down_in")
	#start_time = time.time()
	#while time.time() - start_time < end_time:
		#pass
	time.sleep(118)

	print("exiting")
	KIPR.ao()
	KIPR.create_disconnect()
	sys.exit()
        
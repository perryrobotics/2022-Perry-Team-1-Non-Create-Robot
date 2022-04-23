#!/usr/bin/python

#File:  movement.py
#Purpose:  Contains the code for moving our small non-create robot
#Written by:  Perry Team 1 (2022)

import os, sys
from constants import *
import ctypes
from shut_down import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

    
def forward(speed, ticks):
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)
        
	KIPR.mav(LM, speed)
	KIPR.mav(RM, speed)
	while KIPR.gmpc(LM) < ticks:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)
            
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)
            
def backward(speed, ticks):
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)	
	
	KIPR.mav(LM, -speed)
	KIPR.mav(RM, -speed)
	while KIPR.gmpc(LM) > -ticks:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)
	
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)

def right(speed, ticks):
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)
        
	KIPR.mav(LM, speed)
	KIPR.mav(RM, -speed)
	while KIPR.gmpc(LM) < ticks:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)
            
	KIPR.cmpc(LM)
	KIPR.cmpc(RM) #Random words
            
def left(speed, ticks):
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)
        
	KIPR.mav(LM, -speed)
	KIPR.mav(RM, speed)
	while KIPR.gmpc(RM) < ticks:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)
            
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)
            
def moveServo(position,port):
	originpos = KIPR.get_servo_position(3)
	KIPR.set_servo_position(port, position)		
	KIPR.msleep(2000)
	KIPR.set_servo_position(port, originpos)

        
def forward_to_black(speed):
	KIPR.mav(LM, speed)
	KIPR.mav(RM, speed)
	while KIPR.analog(FRONT_LINE) < BLACK_THRESH:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)	
    
def backward_to_black(speed):
	KIPR.mav(LM, -speed)
	KIPR.mav(RM, -speed)
	while KIPR.analog(BACK_LINE) < BLACK_THRESH:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)
            
def right_to_black(speed):
	KIPR.mav(LM, speed)
	KIPR.mav(RM, -speed)
	while KIPR.analog(FRONT_LINE) < BLACK_THRESH:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)	
            
def left_to_black(speed):
	KIPR.mav(LM, -speed)
	KIPR.mav(RM, speed)
	while KIPR.analog(FRONT_LINE) < BLACK_THRESH:
		pass
        
	KIPR.mav(LM, 0)
	KIPR.mav(RM, 0)	
            
def line_follow_ticks(speed, ticks):
	KIPR.cmpc(LM)
	KIPR.cmpc(RM)

	while KIPR.gmpc(LM) < ticks:

		if KIPR.analog(FRONT_LINE) > BLACK_THRESH:    # we see black so drift left
			KIPR.mav(LM,speed-300)
			KIPR.mav(RM,speed+300)
		else: #we are over white, drift right
			KIPR.mav(LM,speed+300)
			KIPR.mav(RM,speed-300)
	KIPR.mav(LM, 0)
	KIPR.mav(RM,0)      

	






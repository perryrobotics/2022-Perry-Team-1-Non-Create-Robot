#!/usr/bin/python

#File:  effectors.py
#Purpose:  Contains the code for our arm and claw
#Writte nby:  Perry Team 1 (2022)

import os, sys
from constants import *
import ctypes
from shut_down import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

DELAY = 400  #Standard msleep delay
    
def open_claw():
	KIPR.set_servo_position(CLAW, CLAW_OPEN)
	KIPR.msleep(DELAY)

def close_claw():
	KIPR.set_servo_position(CLAW, CLAW_CLOSED)
	KIPR.msleep(DELAY)  
        
def close_claw_cube():
	KIPR.set_servo_position(CLAW, CLAW_CLOSED_CUBE)
	KIPR.msleep(DELAY)
        
def raise_arm():
	KIPR.set_servo_position(ARM, ARM_UP)
	KIPR.msleep(DELAY)
        
def lower_arm():
	KIPR.set_servo_position(ARM, ARM_DOWN)
	KIPR.msleep(DELAY)
       
def cube_arm():
	KIPR.set_servo_position(ARM, ARM_CUBE)
	KIPR.msleep(DELAY)
        
def lazy_susan_dump_arm():
	KIPR.set_servo_position(ARM, ARM_LAZY_SUSAN)
	KIPR.msleep(DELAY)
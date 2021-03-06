#!/usr/bin/python
import os, sys
import ctypes
import threading
from constants import *
from movement import *
from effectors import *
from shut_down import *
from wait_for_start import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
start_function = threading.Thread(target =shut_down)
   
def main():
	KIPR.enable_servos()    
	print "Furry 4 life. UwU"
	KIPR.set_servo_position(ARM, ARM_UP)
	KIPR.set_servo_position(CLAW, CLAW_CLOSED)
	#KIPR.msleep(1500)
	wait_for_start(1)
	start_function.start()   # start the 2 minute timer!
	KIPR.msleep(500)
	#=============================================================================================
    #GOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!
	#=============================================================================================
        
    #=================================================    
	#GO GET RED POM #1!!
	#=================================================	
	right(500,300)
	open_claw()
	lower_arm()
	forward(500, 525)
	close_claw()
	raise_arm()  #WE GOT RED POM #1!!
    #=================================================    
	#GO GET RED POM #2!!
	#================================================= 
	#forward(900, 1100)
	forward_to_black(900)   
	left(500, 300)
	forward(1400, 5400) #HIT BACK PIPE TO ALIGN
	
	backward(900,1000) #GET OFF PIPE
	right(900,1680) #TURN TO POM 2
	lower_arm()
	open_claw()
	forward(900,1410)
	close_claw() #GOT POM #2
	raise_arm()

    #=================================================    
	#GO GET RED POM #3!!
	#================================================= 
	left(500, 650)
	backward(1400, 1900)  #align on side pipe
	forward(900, 3700) #drive toward pom #3
	right(900,380) #turn to POM 3
	backward(900,700)
	lower_arm()
	open_claw()
	forward(900,1410)
	close_claw() #GOT POM #3
	raise_arm()

    #=================================================    
	#GO GET RED POM #4!!
	#================================================= 
	backward(900,1000)
	left(900,330)
	forward(900,3000)
	right(900,350) #TURN TO POM 4
	backward(900,900)
	lower_arm()
	open_claw()
	forward(900,1210)
	close_claw() #GOT POM #4
	raise_arm()
    #=================================================    
	#GO DUMP RED POMS
	#================================================= 
	backward(900,1000)  #GET AWAY FROM POM PILE #4
	left(900,365) #turn to face FAR side of board
    
	forward_to_black(1400)#BLACK TAPE IN MIDDLE OF TABLE
    
	right(900,120) #slight correction turn after hitting black tape
	forward(1400,7500) # continue towards other side of board
    
	right(500, 1050) #TURN TO FACE SIDE WITH LAZY SUSAN
	backward(900, 2000) #HIT BACK PIPE
	forward_to_black(900)
	forward(900, 2000)  #HIT PIPE NEAR LAZY SUSAN
    
	backward_to_black(700)
	forward(900, 1050)
	left(900, 700) #turn to lazy susan
	lazy_susan_dump_arm()
	forward(500, 2200)
	open_claw() #BIG SCORE!!!
        
#RED POMS DUMPED!!
        
	backward(1000,3000)
	right(900,500)
	backward_to_black(1000)
	right(1000,1900)
	backward(900,800)
	lower_arm()
	forward(900,1000)
	left(900,450)
	forward_to_black(900)
	close_claw()
	left(900,1500)  #sweep poms out of way
	lazy_susan_dump_arm()
	left_to_black(900)
	line_follow_ticks(900,3200)
	left(900,200)
	lower_arm()
	open_claw()
	lazy_susan_dump_arm()
	backward(900, 500) # get away from transporter
	right(900,750)
	right_to_black(900)
	line_follow_ticks(1100, 5500) #go towards center of table
	open_claw()
	lower_arm()
	line_follow_ticks(900,5500) #travel to end of table
	forward(900,3000)
	close_claw()
	lazy_susan_dump_arm()
	right(900,1500)
	#forward(900, 1000)
	right_to_black(900)
        
	line_follow_ticks(900, 6000)
	forward(900, 2000)
	line_follow_ticks(900,8000)
	backward(900,550)
	right(900,250)
	lower_arm()
	open_claw()

if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main();

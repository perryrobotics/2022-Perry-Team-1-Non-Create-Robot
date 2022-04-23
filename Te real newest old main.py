#!/usr/bin/python
import os, sys
import ctypes
import threading
from constants import *
from movement import *
from effectors import *
from shut_down import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
start_function = threading.Thread(target =shut_down)
   
def main():
	KIPR.enable_servos()    
	print "Furry 4 life. UwU"
	KIPR.set_servo_position(ARM, ARM_UP)
	KIPR.set_servo_position(CLAW, CLAW_CLOSED)
	#KIPR.msleep(1500)
	#start_function.start()   # start the 2 minute timer!       
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
	forward_to_black(900)
	forward(900, 2000)  #HIT PIPE NEAR LAZY SUSAN
	backward_to_black(700)
	forward(900, 250)
	lower_arm()
	left(1500, 1600)  #MOVE TRANSPORTER
	right(1500,1500)
	raise_arm()
	left(900, 700) #turn to lazy susan
	lazy_susan_dump_arm()
	forward(500, 2700)
	open_claw() #BIG SCORE!!!
    #=================================================    
	#spin the lazy susan
	#================================================= 

	backward(900,2500)  #get off lazy susan
	close_claw()
	right(700,730)
	forward(700,1000) 
	left(700,900)#FACE THE LAZY SUSAN
	KIPR.set_servo_position(ARM, 1190) #PUT ARM AT SIN HEIGHT
	forward(500,2700) #SPIN THE LAZY SUSAN!
	backward(500,2500) #GET OUT FROM UNDER LAZY SUSAN!!
    #=================================================    
	# GET GREEN CUBE #1
	#================================================= 
	left(900,1575)
	backward(500,2000)#HIT PIPE
	forward_to_black(900) #HIT BLACK TAPE
	left(700, 50)
	cube_arm()
	open_claw()
	forward(900, 3000) #drive to first green cube
	close_claw_cube()  #GOT GREEN CUBE #1
	backward_to_black(900)
	raise_arm()
	right(900, 2450) #TURN AWAY FROM TRANSPORTER
	forward_to_black(900)
	forward(900, 2400)
	left(900,1100)#Turn to Pipe next to Lazy Susan 
	forward(900, 300)#Hit Pipe next to Lazy Susan
	backward(900,500)
	right(900,700)#Turn to Lazy Susan
	forward(900,850)

	lazy_susan_dump_arm()#Score first green cube
	KIPR.msleep(750)
	 
	"""
	left(900, 830) #Turn to Lazy Susan
	forward(900, 2400)
	open_claw() #SCORE 1st cube
    #=================================================    
	#GO GET GREEN CUBE #2!!
	#================================================= 
	
	backward_to_black(900) #Go get second/last pom!
	left(900, 1800)# point towards last cube
	cube_arm()
	forward(900, 3400)
	close_claw_cube()  #GRABBED LAST GREEN CUBE
	backward_to_black(1500)
	raise_arm()
	left(900, 2750)
	forward(1300, 4700)
	KIPR.set_servo_position(ARM, 1125)
	KIPR.set_servo_position(CLAW, 800)
	"""
	#open_claw()   
if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main();

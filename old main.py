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
    
 
LM = 0
RM = 3
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
	right(500,300)
	open_claw()
	lower_arm()
	forward(500, 500)
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
	right(900,1800) #TURN TO POM 2
	lower_arm()
	open_claw()
	forward(900,1400)
	close_claw() #GOT POM #2
	raise_arm()

    #=================================================    
	#GO GET RED POM #3!!
	#================================================= 
	left(500, 650)
	backward(1400, 1900)  #align on side pipe
	forward(900, 3700) #drive toward pom #3
	right(900,380) #turn to POM 3
	backward(900,500)
	lower_arm()
	open_claw()
	forward(900,1200)
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
	forward(900,1200)
	close_claw() #GOT POM #4
	raise_arm()
    #=================================================    
	#GO DUMP RED POMS
	#================================================= 
	backward(900,2500)
	left(900,391) #turn to face side of board
	forward_to_black(1400)#BLACK TAPE IN MIDDLE OF TABLE
	right(900,55)
	forward(1400,11500) # WE HAVE HIT THE FAR PIPE!!!
	backward(1000,2500)
	right(900, 1050)
	backward(1000,1500) #ALIGN ON PIPE WITH CUBES
	forward(1000,9000) #go hit pipe near lazy susan
	#IN POSITION TO START DUMP!!
	#backward(1000, 1900) #get off pipe
	backward_to_black(700)
	forward(900, 350)
	left(900, 650) #turn to lazt susan
	lazy_susan_dump_arm()
	forward(500, 2550)
	open_claw() #BIG SCORE!!!
    #=================================================    
	#GO GET GREEN CUBES!!
	#================================================= 
	backward(900,2000)
	left(900,1575)
	backward(500,3000)#HIT PIPE
	forward_to_black(900) #HIT BLACK TAPE
	left(700, 50)
	cube_arm()
	forward(900, 3000) #drive to first green cube
	close_claw()
	backward_to_black(900)
	raise_arm()
	right(900, 2450) #TURN AWAY FROM TRANSPORTER
	forward_to_black(900)
	forward(900, 2800)
	lazy_susan_dump_arm()
	left(900, 750) #Turn to Lazy Susan
	forward(900, 1400)
	open_claw() #SCORE 1st cube
    #=================================================    
	#GO GET GREEN CUBE #2!!
	#================================================= 
	
	backward_to_black(900) #Go get second/last pom!
	left(900, 1800)# point towards last cube
	cube_arm()
	forward(900, 3400)
	close_claw()  #GRABBED LAST GREEN CUBE
	backward_to_black(1500)
	raise_arm()
	left(900, 2750)
	forward(1300, 4700)
	KIPR.set_servo_position(ARM, 1125)
	KIPR.set_servo_position(CLAW, 800)
	#open_claw()
	
        
if __name__== "__main__":
	sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
	main();

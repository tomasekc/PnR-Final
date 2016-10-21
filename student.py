import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 85
    STOP_DIST = 20

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate servo", self.calibrate),
                "s": ("Battery level", self.status),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        #Check if its clear using superClear method
        print("Is it clear?")
        if(self.superClear()):
            print("Let's dance!")
        #Time to dance
        for x in range(3):
            x = 100
            print("Speed is set to:" + str(x))
            set_speed(x)
            servo(20)
            self.encB(10)
            self.encR(4)
            self.encL(4)
            self.encF(15)
            self.encR(4)
            self.encL(4)
            self.encB(5)
            servo(120)
            time.sleep(.1)


    def superClear(self):
    #Check front distance
        servo(self.MIDPOINT)
        time.sleep(.1)
        scan1 = us_dist(15)
        time.sleep(.5)
        print("Front Distance:" + str(us_dist(15)))
    #Check right distance
        servo(self.MIDPOINT - 60)
        time.sleep(.1)
        scan2 = us_dist(15)
        time.sleep(.5)
        print("Right Distance:" + str(us_dist(15)))
    #Check left distance
        servo(self.MIDPOINT + 60)
        time.sleep(.1)
        scan3 = us_dist(15)
        time.sleep(.5)
        print("Left Distance:" + str(us_dist(15)))
    #Average the 3 scans
        scan0 = (scan1 + scan2 +scan3) / 3
        time.sleep(.1)
        servo(self.MIDPOINT)
        time.sleep(.5)
    #If its safe or not to dance:
        if scan0 < self.STOP_DIST:
            print("There is something in the way, so I'll back up")
            time.sleep(.5)
            self.encB(20)
            return False
        if scan0 > self.STOP_DIST:
            print("It looks pretty clear")
        return True


    def status(self):
        print("My power is at:" + str(volt()) + "volts")
        servo(self.MIDPOINT)
        time.sleep(.1)
        return us_dist(15)

    #INFORMATION: LEFT MOTOR STRONGER THAN RIGHT MOTOR
    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: If while loop fials, check for other paths
        #loop: check that it's clear
        while self.isClear():
            #Let's go forward just a bit
            self.encF(10)
        if self.isClear() is False:
            self.choosePath()



####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()

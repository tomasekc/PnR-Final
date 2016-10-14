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
        print("Is it clear?")
        if(self.superClear()):
            print("Let's dance!")
        for x in range(2):
            #if not self.isClear():
                #print ("Omergosh, it ain't clear!")
                #break
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
        servo(self.MIDPOINT)
        time.sleep(.1)
        scan1 = us_dist(15)
        time.sleep(.5)
        print("Front Distance:" + str(us_dist(15)))
        servo(self.MIDPOINT - 60)
        time.sleep(.1)
        scan2 = us_dist(15)
        time.sleep(.5)
        print("Right Distance:" + str(us_dist(15)))
        servo(self.MIDPOINT + 60)
        time.sleep(.1)
        scan3 = us_dist(15)
        time.sleep(.5)
        print("Left Distance:" + str(us_dist(15)))
        scan0 = (scan1 + scan2 +scan3) / 3
        if scan0 < self.STOP_DIST:
            print("There is something in the way")
            self.encB(20)
            return False

        if scan0 > self.STOP_DIST:
            print("It is clear to move")
        return True


    def status(self):
        print("My power is at:" + str(volt()) + "volts")
        servo(self.MIDPOINT)
        time.sleep(.1)
        return us_dist(15)


    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE


####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()

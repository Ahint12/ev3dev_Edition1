#!/usr/bin/env python3
# 
# Filename: runSelected.py
#

import os
# from re import A
import sys
# import config

from time import sleep, time
from defineRobot import *
from myBlocks import *




def runSelected():

    if (True):        
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)

        '''
        print("count_per_rot = %.2f" % BackMotor.count_per_rot, file=sys.stderr)    
        print("driver_name = %s" % BackMotor.driver_name, file=sys.stderr)

        print("speed = %.2f" % BackMotor.speed, file=sys.stderr)    
        BackMotor.on(100)
        for x in range(1, 100):
            print("speed = %.2f" % BackMotor.speed, file=sys.stderr)    
        '''

        motorStall('D', 20, 10)
        sleep(0.2)
        motorStall('D', -20, -10)
        sleep(0.2)


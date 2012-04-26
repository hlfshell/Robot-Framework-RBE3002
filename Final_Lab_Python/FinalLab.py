#! /usr/bin/env python
'''


'''

import serial, sys, time, string

from RobotClass import *
from AIClass import *

print 'Creating new robot object. Opening serial connection.'
johnny5 = Robot('/dev/ttyUSB1')

print 'Creating our AI'
littleOne = AI()

print 'Giving AI the robot'
littleOne.setRobot(johnny5)

print 'Creating robot behaviors'


print 'Creating robot goals'


print 'Running lab code'

while 1:
	littleOne.run()

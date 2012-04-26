#! /usr/bin/env python

'''
frontalradar2.py

Author: Keith Chester


'''

import sys, math, numpy
from RobotClass import *

print 'Importing the matlab engine'
from mlabwrap import mlab
print 'matlab engine imported'

#Create the robot
johnny5 = Robot('/dev/ttyUSB0')
while not johnny5.Initialize():
	pass
print 'Johnny 5 is Alive!'


johnny5.turret.servo.moveTo(15)


#while 1:
#	johnny5.servo.moveTo(int(raw_input('enter angle > ')))


#Run the pan program, and constantly update the screen with new data
direction = 1
while 1:	
#	if johnny5.turret.servo.Position >= 165:
#		direction = -1
#	elif johnny5.turret.servo.Position <= 15:
#		direction = 1
	data = johnny5.turret.pan()
	mlab.frontalRadar(data)

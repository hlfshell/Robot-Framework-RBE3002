#! /usr/bin/env python

'''

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

distanceToGoForward = 0
heading = 0
origin = [500, 500]

def turn(theta):
	pass
'''
	 tell the robot to turn a known theta. wait for confirmation byte. ADD PROTECTION
'''

def move(distance, start, angle):
	pass
'''
	turn(angle)
	tell the robot to move forward. wait for distance traveled to be sent back. ADD PROTECTION
	take the distance, add it to origin at angle.
'''

while 1:
	turn(heading)
	origin = move(distanceToGoForward, origin, heading)
	data = johnny5.turret.pan()
	[heading, distanceToGoForward]= mlab.DiscoverWorld(data, origin, nout = 2)

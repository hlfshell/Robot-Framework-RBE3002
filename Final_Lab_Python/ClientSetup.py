#!/usr/bin/env python

'''
ClientSetup.py

Author: Keith Chester

Debug/testing program for robot and all objects.

Used as an example of how to work the framework.

'''

import sys, os, serial, time, string, csv

from RobotClass import *

print 'Creating new Robot.'
littleOne = Robot('/dev/ttyUSB1')

#I named it robot to remind you that you can essentially have MULTIPLE connections and just modify
#your functions to accept the serial port as a function

#Initialize the Robot
while not littleOne.Initialize():
	pass

'''littleOne.servo.moveTo(0)
time.sleep(1)'''
'''while 1:
	#print littleOne.potentiometer.grabData()
	#print littleOne.bumper.grabData()
	#print littleOne.bumper.readData()
	print littleOne.infrared.readData()'''

#littleOne.leftMotor.setVoltage(2048)
#littleOne.rightMotor.setVoltage(0)

print 'Setting motor voltages to 100% forward.'
littleOne.leftMotor.setMotor(0)
littleOne.rightMotor.setMotor(0)

#print 'sending command 0xC6'
#littleOne.serialConnection.write(chr(0xC6))
#time.sleep(8)
#print 'sending second command'
#littleOne.serialConnection.write(chr(0x04))
'''print 'sending 411 via hexadecimal. first byte'
littleOne.serialConnection.write(chr(0x9B))
print 'second byte'
littleOne.serialConnection.write(chr(0x01))'''
#	time.sleep(.05)
	#pass


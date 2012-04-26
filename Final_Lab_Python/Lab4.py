#! /usr/bin/env python
'''


'''

import serial, sys, time, string

from RobotClass import *

print 'Creating new robot object. Opening serial connection.'
johnny5 = Robot('/dev/ttyUSB1')

#I named it robot to remind you that you can essentially have MULTIPLE connections and just modify
#your functions to accept the serial port as a function

#Initialize the Robot
while not johnny5.Initialize():
	pass

print 'Johnny 5 is alive!'

johnny5.turret.servo.moveTo(45)
time.sleep(.5)

turretCommand = [45, 1]
turretRange = 135-45
frontRadar = [0 for i in range(0,turretRange/5)]

def setMotors(inputValues):
	johnny5.leftMotor.setMotor(inputValues[0])
	johnny5.rightMotor.setMotor(inputValues[1])

def setMotorVelocities(inputVelocities):
	finalPercentages = [inputVelocities[0]/9.6 * 100, inputVelocities[1]/9.6 * 100]
	setMotors(finalPercentages)

def maintainTimeAtDistance(distance, timeInstance):
	velocityAverage = distance/timeInstance
	setMotorVelocities([velocityAverage, velocityAverage])
	time.sleep(timeInstance)
	setMotors([0,0])

def goTheDistance(distance):
	setMotors([100, 100])
	time.sleep(distance / 9.6)
	setMotors([0, 0])

def turnDegrees(degrees):
	if degrees == 0:
		return	
	if degrees < 0:
		setMotors([-100, 100])
	else:
		setMotors([100, -100])
	time.slee(degrees / 120)
	setMotors([100, 100])

'''maintainTimeAtDistance(19.2, 4)

while 1:
	pass'''

setMotors([100, 100])
TOGGLE = 1
while TOGGLE:
	if turretCommand[1] == -1 and turretCommand[0] <= 45:
		turretCommand[1] = 1
	elif turretCommand[1] == 1 and turretCommand[0] >= 135:
		turretCommand[1] = -1;
	newPosition = turretCommand[0] + (5 * turretCommand[1])
	turretCommand[0] = johnny5.turret.servo.Position
	objectCheck = johnny5.turret.readAt(newPosition)
	#print objectCheck
	
	#Add the value to the radar.
	frontRadar[((turretCommand[0]-45) / 5) - 1] = objectCheck[1]
	
	scanResult = [0, 0]

	tmp = 80
	for i in range(0, len(frontRadar)):
		if frontRadar[i] != 0 and frontRadar[i] < tmp:
			scanResult = [(i * 5) + 45, frontRadar[i]]

	#print scanResult

	if scanResult[1] > 0 and scanResult[1] < 40:
		if scanResult[0] <= 90:
			setMotors([100,-100])
			time.sleep(.25)
			goTheDistance(8)
			setMotors([-100, 100])
			time.sleep(.25)
			goTheDistance(8)
			setMotors([-100, 100])
			time.sleep(.25)
			goTheDistance(8)
			setMotors([100, -100])
			time.sleep(.25)
			TOGGLE = 0
		else:
			setMotors([-100,100])
			time.sleep(.25)
			goTheDistance(8)
			setMotors([100, -100])
			time.sleep(.25)
			goTheDistance(8)
			setMotors([100, -100])
			time.sleep(.25)
			goTheDistance(8)
			setMotors([-100, 100])
			time.sleep(.25)
			TOGGLE = 0
goTheDistance(8)

'''
while 1:
	if turretCommand[1] == -1 and turretCommand[0] <= 45:
		turretCommand[1] = 1
	elif turretCommand[1] == 1 and turretCommand[0] >= 135:
		turretCommand[1] = -1;
	newPosition = turretCommand[0] + (5 * turretCommand[1])
	turretCommand[0] = johnny5.turret.servo.Position
	objectCheck = johnny5.turret.readAt(newPosition)
	#print objectCheck
	
	#Add the value to the radar.
	frontRadar[((turretCommand[0]-45) / 5) - 1] = objectCheck[1]
	
	scanResult = [0, 0]

	tmp = 80
	for i in range(0, len(frontRadar)):
		if frontRadar[i] != 0 and frontRadar[i] < tmp:
			scanResult = [(i * 5) + 45, frontRadar[i]]

	#print scanResult

	if scanResult[1] > 0 and scanResult[1] < 40:
		print scanResult[0]
		if scanResult[0] <= 90:
			setMotors([100,75])
		else:
			setMotors([75, 100])
	else:
		setMotors([100,100])
'''

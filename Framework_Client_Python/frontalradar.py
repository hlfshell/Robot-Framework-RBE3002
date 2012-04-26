#! /usr/bin/env python

'''
frontalradar.py

Author: Keith Chester

Using pygame, create a robot object
and begin pan-scanning in front of the
robot in order to draw a frontal radar
mapping of objects in front of it.

'''

import pygame, sys, math
from RobotClass import *

#Create the robot
johnny5 = Robot('/dev/ttyUSB1')
while not johnny5.Initialize():
	pass
print 'Johnny 5 is Alive!'


johnny5.turret.servo.moveTo(25)

#Initialize pygame
pygame.init()


#Create the pygame screen
size = width, height = 400, 400

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0

screen = pygame.display.set_mode(size)
robot = pygame.image.load("robot.jpg")
robot.convert()
robot = pygame.transform.rotate(robot, 90)
robot = pygame.transform.smoothscale(robot, (45, 75))
robotRectangle = robot.get_rect()
robotRectangle.center = (width/2, height/2)

'''
getXY(polarCoordinate, origin)
	Given a set of polar coordinates and the location
	of the relative origin, generate the X/Y coordinates
	from this data.
@param polarCoordinate - a list of (angle, magnitude)
@param origin - a list of (x coordinate, y coordinate)
@return [X, Y] - a list of (x coordinate, y coordinate)
'''
def getXY( polarCoordinate , origin):
	theta = polarCoordinate[0]
	radius = polarCoordinate[1]
	X = origin[0] + radius * math.cos(math.radians(theta))
	Y = origin[1] - radius * math.sin(math.radians(theta))
	return [X, Y]

#Run the pan program, and constantly update the screen with new data
'''while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
#	for i in range(10, len(data)-10):	
	if johnny5.turret.servo.Position >= 150:
		direction = -1
		screen.fill(black)
	elif johnny5.turret.servo.Position <= 25:
		direction = 1
		screen.fill(black)
	#position = getXY(data[i], robotRectangle.center)
	position = getXY(data, robotRectangle.center)
	screen.set_at([position[0], position[1] - (robotRectangle.height / 2)], green)
	screen.blit(robot, robotRectangle)
	pygame.display.flip()
'''
johnny5.servo.moveTo(45)
time.sleep(.25)
while 1:
	for i in range(45,135,5):
		print johnny5.turret.readAt(i)
		time.sleep(.1)
	#print johnny5.turret.pan()

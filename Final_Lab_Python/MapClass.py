'''

'''

import sys, time, string
from numpy import *

class Map:

	mapMatrix = None
	gridSize = None

	#robotInformation = origin, orientation, dimensions
	robotInformation = None

	def __init__(self, mapDimensions, gridSizeInstance, robotStartingInformation):
		self.gridSize = gridSizeInstance
		dimensions = [mapDimensions[0] / self.gridSize, mapDimensions[1] / self.gridSize]		
		self.mapMatrix = zeros(dimensions)
		self.gridSize = gridSizeInstance
		self.robotInformation = robotStartingInformation
		self.placeRobot()

	def removeRobot(self):
		pass
		#placeRobot in reverse

	def placeRobot(self):
		pass
		#Using self.robotInformation, find the origin of the robot
		#based on the angle and the dimensions of the robot, step around and mark the appropiate
		#boxes as being filled by the robot

	def addObstacle(self, infraredPanData, sensorErrorMagnitude):
		pass

	def update(self, movementVector):
		pass
		#movementVector = polar coordinate. origin moved [0] = angle [1] = magnitude
		#update robot information
		#remove robot from map
		#place new robot
		#Pan the infrared. Get readings.
		#step through readings, add to map

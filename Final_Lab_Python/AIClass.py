'''

'''

import serial, sys, time
from RobotClass import *
from GoalClass import *
from BehaviorClass import *

class AI:

	robot = None
	robotData = None
	robotMap = None
	goals = None
	behavior = None

	__init__(self):
		pass

	setRobot(self, robotInstance):
		self.robot = robotInstance

	addGoal(self, goalInstance):
		try:
			totalGoals = len(self.goals)
		except:
			self.goals = [goalInstance]
		for i in range(0, totalGoals):
			if goals[i].ID == goalInstance.descriptor:
				print 'Error: goal is already added!'
				return
		print 'Goal "', goalInstance.descriptor, '" added.'

	removeGoal(self, goalInstance):
		try:
			self.goals.remove(goalInstance)
		except:
			print 'Error: goal is not in list.'
			return

	addBehavior(self, behaviorInstance):
		try:
			totalBehaviors = len(self.behaviors)
		except:
			self.behaviors = [behaviorInstance]
		for i in range(0, totalBehaviors):
			if behaviors[i].ID == behaviorInstance.descriptor:
				print 'Error: behavior is already added!'
				return
		print 'Behavior "', behaviorInstance.descriptor, '" added.'

	removeBehavior(self, behaviorInstance):
		try:
			self.behaviors.remove(behaviorInstance)
		except:
			print 'Error: behavior is not in list.'
			return

	updateRobot(self):
		pass

	behaviorUpdate(self):
		try:
			totalBehaviors = len(self.behaviors)
		except:
			return
		for i in range(0, totalBehaviors):
			self.behaviors[i].update(robotData, robotMap)

	goalUpdate(self):
		try:
			totalGoals = len(self.goals)
		except:
			return
		for i in range(0, totalGoals):
			self.goals[i].update(robotData, robotMap

	run(self):
		self.updateRobot()
		self.behaviorUpdate()
		self.goalUpdate()

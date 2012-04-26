'''
RobotClass.py

Author: Keith Chester

This is what creates and makes up a robot.
For now, it requires objects to be manually added
to it. In the future, it will contain a simple list
of hardware added to it.

The class shall also contain general sensor update and
map creation functions in the future too.

Each robot requires its own unique connection.

'''


import serial
import Commands
from SensorClass import *
from PotentiometerClass import *
from BumperClass import *
from InfraredClass import *
from ServoClass import *
from TurretClass import *
from MotorClass import *

class Robot:

	serialConnection = None

	#Components that make up my robot
	potentiometer = None
	bumper = None
	infrared = None
	servo = None
	turret = None

	leftMotor = None
	rightMotor = None

	def __init__(self, connectionInstance):
		try:
			self.serialConnection = serial.Serial(connectionInstance, baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=1)
		except:
			print "Failure to create connection"
		self.potentiometer = Potentiometer(self.serialConnection, 0)
		self.bumper = Bumper(self.serialConnection, 5)
		self.infrared = Infrared(self.serialConnection, 0)
		self.servo = Servo(self.serialConnection)
		self.turret = Turret(self.servo, self.infrared)
		self.leftMotor = Motor(self.serialConnection, 'left')
		self.rightMotor = Motor(self.serialConnection, 'right')

	'''
	Initialize()
		Initializes the robot and ensures that we are connected to it (not just an open serial connection).
	@return  boolean - True if connected False if not
	'''
	def Initialize(self):
		global InitializeRobot, SUCCESS
		self.serialConnection.write(InitializeRobot)
		tmp = self.serialConnection.read()
		if tmp is None or tmp != SUCCESS:
			print 'Failure to initialize'
			return False
		else:
			print 'Initialization succeeded.'
			return True


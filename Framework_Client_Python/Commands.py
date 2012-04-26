'''
Commands.py

Author: Keith Chester

This holds all possible commands - should be kept
in sync with Commands.h on robot side.

'''

setID = chr(0x00)
requestID = chr(0x01)
InitializeRobot = chr(0x02)
reset = chr(0x03)

requestPinValue = chr(0xA0)
requestADCchannel = chr(0xA1)

enableMotors = chr(0xC0)
disableMotors = chr(0xC1)
setPID = chr(0xC3)
setMotorRight = chr(0xC4)
setMotorLeft = chr(0xC5)
sendStepperTo = chr(0xC6)
setServoTo = chr(0xD0)
setMotorLeftForward = chr(0xD1)
setMotorRightForward = chr(0xD3)
setMotorLeftReverse = chr(0xD2)
setMotorRightReverse = chr(0xD4)

PING = chr(0xFF)



SUCCESS = chr(0xFF)
FAILURE = chr(0x00)

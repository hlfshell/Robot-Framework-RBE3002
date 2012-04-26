/*
 * Commands.c
 *
 *  Created on: Mar 30, 2009
 *      Author: Keith Chester
 *
 *  Edit this to include new commands.
 */

#include "FunctionalHeader.h"

/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * commandMenu() is called only when we have at least
 * one full byte in our serial buffer. When it is called,
 * we select the appropiate command and react to it.
 *
 * THERE IS NO ERROR CHECKING IF WE ARE "OFF" BY ONE.
 *
 * This is how to add a command to our commandMenu.
 * Assign a command a unique number - a char, so you
 * have 0x00 to 0xFF, or 0 to 255 for 256 possible
 * commands. You may also use definitions declared
 * elsewhere if you wish. I suggest you keep them
 * the same on both client and robot for organization
 * purposes. I won't hold your hand with it though.
 *
 * As soon as a command byte is received, we go in and
 * deal with that information immediately. All forms
 * of communication is initiated by the client side first.
 * If the client wishes to know information, it must REQUEST
 * IT. I suggest using the convention of getINFONAME()
 * throughout your functions in order to retrieve information.
 *
 * Is this the most efficient way to deal with this? Heck no!
 *
 * I do not recommend ever calling commandMenu FROM an interrupt.
 * I am using avrlib's buffer system for remembering as many
 * commands as possible so you can deal with the commands in a
 * linear response (ie. a while(1)) WHILE still being able to
 * service interrupts. This prevents worrying about a super fast
 * timer screwing up your serial read/write as much.
 *
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 */
void commandMenu(){
	char commandByte = readCommand();

	//Administration
	if(commandByte == SETID) setID();
	if(commandByte == REQUESTID) requestID();
	if(commandByte == INITIALIZEROBOT) InitializeRobot();
	if(commandByte == RESET) reset();

	//Sensors
	if(commandByte == REQUESTPINVALUE) requestPinValue();
	if(commandByte == REQUESTADCCHANNEL) requestADCchannel();

	//Actuator Control
	if(commandByte == ENABLEMOTORS) requestPinValue();
	if(commandByte == DISABLEMOTORS) requestPinValue();
	if(commandByte == SETPID) requestPinValue();
	if(commandByte == SENDSTEPPERTO) requestSendStepperTo();
	//if(commandByte == SETLEFTMOTOR) setLeftMotor();
	//if(commandByte == SETRIGHTMOTOR) setRightMotor();
	if(commandByte == SETLEFTMOTORFORWARD) setLeftMotorForward();
	if(commandByte == SETLEFTMOTORREVERSE) setLeftMotorReverse();
	if(commandByte == SETRIGHTMOTORFORWARD) setRightMotorForward();
	if(commandByte == SETRIGHTMOTORREVERSE) setRightMotorReverse();

	if(commandByte == REQUESTSETSERVO) requestSetServo();
	//Variable control
}

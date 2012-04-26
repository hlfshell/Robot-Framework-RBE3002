/*
 * StepperMotor.c
 *
 *  Created on: Apr 2, 2009
 *      Author: Keith Chester
 *
 *  This file shall maintain and control the stepper motor's
 *  movement. This includes support for homing the stepper motor,
 *  stepping it individually, hitting a particular position, and
 *  doing a full sweep.
 */

#include "FunctionalHeader.h"

volatile int positionCurrent = 0;
volatile int positionDesired = 0;
volatile char direction;

/** \fn void InitializeStepper()
 * \brief Initializes the stepper motor pins.
 * \param void
 * \return void
 */
void InitializeStepper(){
	DDRC |= _BV(STEPPERDIRPIN) | _BV(STEPPERDRIVEPIN);
	homeStepper();
}

/** \fn char checkStepperBumper()
 * \brief Checks to see if the stepper bumper is being hit.
 * \param void
 * \return char - 1 (True) or 0 (False)
 */
char checkStepperBumper(){
	return (STEPPERBUMPER);
}

/** \fn void homeStepper()
 * \brief Moves the stepper back to home position
 * \param void
 * \return void
 */
void homeStepper(){
	setStepperDirection(LEFT);
	while(checkStepperBumper()) step();
	positionCurrent = 0;
}

/** \fn void setStepperDirection(char direction)
 * \brief Accepts a direction, LEFT (0) or RIGHT (1). Sets said direction.
 * \param char direction - LEFT (0) or RIGHT (1). Default is left.
 * \return void
 */
void setStepperDirection(char directionNew){
	if(directionNew == RIGHT){
		STEPPERPORT &= ~(1 << STEPPERDIRPIN);
		direction = RIGHT;
	}
	else if(directionNew == LEFT){
		STEPPERPORT |= (1 << STEPPERDIRPIN);
		direction = LEFT;
	}
}

/** \fn void step()
 * \brief Moves the stepper motor in the direction it is set to.
 * \param void
 * \return void
 */
void step(){
	STEPPERPORT ^= (1 << STEPPERDRIVEPIN);
	_delay_us(1000);
	STEPPERPORT ^= (1 << STEPPERDRIVEPIN);
	//_delay_us(500);
	if(direction == LEFT) positionCurrent--;
	if(direction == RIGHT) positionCurrent++;
}

/** \fn void requestStepperPosition()
 * \brief Handles client request for setting the stepper motor's direction
 */
void requestSendStepperTo(){
	/*char tmp;
	unsigned int finalValue;
	while(commandsInQueue() < 2){}
	finalValue = readCommand();
	tmp = readCommand();
	finalValue += (tmp >> 8);
	positionDesired = finalValue;*/
	serialTxString("Entered 1.\r\n");
	positionDesired = 411;
	char tmp = 0x02;
	while(tmp != 0x04){
		while(commandsInQueue() < 1) {}
		tmp = readCommand();
	}
	positionDesired = 50;
}

/** \fn void moveStepper()
 * \brief Determines if the stepper needs to move and in what direction.
 */
void moveStepper(){
	//char str[4];
	if(positionCurrent - positionDesired == 0) return;
	else if(positionCurrent - positionDesired < 0) setStepperDirection(RIGHT);
	else setStepperDirection(LEFT);
	step();
	/*serialTxString("direction = ");
	itoa(direction, str, 10);
	serialTxString(str);
	serialTxString("\r\n");
	serialTxString("position desired = ");
	itoa(positionDesired, str, 10);
	serialTxString(str);
	serialTxString("\r\n");
	serialTxString("position current = ");
	itoa(positionCurrent, str, 10);
	serialTxString(str);
	serialTxString("\r\n");*/
}

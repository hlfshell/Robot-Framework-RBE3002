/*
 * InitializeSystem.c
 *
 *  Created on: Mar 30, 2009
 *      Author: Keith Chester
 *
 *  Handles all hardware and function initialization.
 */

#include "FunctionalHeader.h"

char INITIALIZED = 0;
char n = 0;

#include "util/delay.h"
void InitializeHardware(){
	cli();
	InitializeInputPins();
	initializePWM();
	InitializeSerial();
	InitializeA2D();
	SPIInit();
	//InitializeMotor();
	//InitializeStepper();
	//InitializeTimer2();
	sei();
	motorControl(0, 0);
	motorControl(1, 0);
}

void InitializeRobot(){
	INITIALIZED = 1;
	_delay_us(100);
	serialTx(SUCCESS);
}

void reset(){
	//What does a reset entail? iono. You decide
}

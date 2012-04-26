/*
 * FunctionalHeader.h
 *
 *  Created on: Mar 31, 2009
 *      Author: Keith Chester
 *
 *  General header file for all stuff.
 */

#ifndef FUNCTIONALHEADER_H_
#define FUNCTIONALHEADER_H_

#include "HardwareProfile.h"
#include "Commands.h"

//#define DEBUG

#ifdef DEBUG

#include <stdlib.h>

#endif

#define BUFFERSIZE 256

//Commands.c Definitions and Prototypes
void commandMenu();

//InitializeSystem.c
void InitializeHardware();
void InitializeRobot();
void reset();

//Serial.c
void InitializeSerial(void);
void serialTx( unsigned char output );
void serialTxString(char * str);
unsigned char serialRx( void );
char readCommand(void);
int commandsInQueue(void);
char isThereACommand(void);

//ID.c
void setID();
void requestID();

//Timer2.c
void InitializeTimer2();

//ADC.c
void InitializeA2D();
unsigned int get_adc(unsigned char adc_channel);
void requestADCchannel();

//PinChange.c
void InitializeInputPins();
void requestPinValue();
void DDR();

//StepperMotor.c
void InitializeStepper();
char checkStepperBumper();
void setStepperDirection(char direction);
void step();
void homeStepper();
void requestSendStepperTo();
void moveStepper();
void turretMoveStepper();
#define STEPPERPORT PORTC
#define STEPPERDIRPIN 6
#define STEPPERDRIVEPIN 7
#define STEPPERBUMPER (PINC >> 5) & 0x01
#define LEFT 1
#define RIGHT 0

//Servo.c
void initializePWM( void );
void setDutyCycle(unsigned int dutyCycle);
void setServoAngle(signed char angle);
void requestSetServo();

//MotorControl.c
void SPIInit( void);
void InitializeMotor( void);
void motorControl(char motor, int inputValue);
void dacControl(unsigned int valueDesired, char channel);
#define LEFTMOTOR 0
#define RIGHTMOTOR 1
void setLeftMotorForward();
void setLeftMotorReverse();
void setRightMotorForward();
void setRightMotorReverse();

#endif /* FUNCTIONALHEADER_H_ */

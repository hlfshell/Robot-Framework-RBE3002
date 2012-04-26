/*
 * PinChange.c
 *
 *  Created on: Apr 1, 2009
 *      Author: Keith Chester
 *
 *  This is for bumpers and other, simpler devices. This returns
 *  a pin value - 1 for on, 0 for off.
 */

#include "FunctionalHeader.h"

/** \fn void InitializeInputPins()
 * \brief Initializes Port C as an input port
 * \param void
 * \return void
 */
void InitializeInputPins(){
	DDRC = 0x00;
	DDRA = 0x00;
	DDRD = 0xFF;
}

/** \fn void requestPinValue(void)
 * \brief Handles client request for pin values on Port C
 */
void requestPinValue(){
	char pin, value;
	while(commandsInQueue() < 1){}
	pin = readCommand();
	value = (PINC >> pin) & 0x01;
	serialTx(value);
}

/** \fn void setDDR(void)
 * \brief Handles client control of DDR for appropriate port
 */
void setDDR(){
	char pin, port, dir;
	while(commandsInQueue() < 3){}
	pin = readCommand();
	port = readCommand();
	dir = readCommand();

	/*if(port == 'A') DDR = (*char) DDRA;
	else if(port == 'B') DDR = (*char) DDRB;
	else if(port == 'C') DDR = (*char) DDRC;
	else if(port == 'D') DDR = (*char) DDRD;

	if(dir == 1){
		DDR |= (1 << pin);
	}
	else{
		DDR &= ~(1 << pin);
	}*/

	if(port == 'A'){
		if(dir == 1) DDRA |= (1 << pin);
		else DDRA &= ~(1 << pin);
	}
	else if(port == 'B'){
		if(dir == 1) DDRB |= (1 << pin);
		else DDRB &= ~(1 << pin);
	}
	else if(port == 'C'){
		if(dir == 1) DDRC |= (1 << pin);
		else DDRC &= ~(1 << pin);
	}
	else if(port == 'D'){
		if(dir == 1) DDRD |= (1 << pin);
		else DDRD &= ~(1 << pin);
	}
}

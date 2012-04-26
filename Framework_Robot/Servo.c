/*
 * Servo.c
 *
 *	Manages servo control via the 16 bit timer 1
 *  Created on: Apr 8, 2009
 *      Authors: Matt DeDonato and Keith Chester
 */

#include "FunctionalHeader.h"

#define SERVO_RIGHT 550
#define SERVO_LEFT 2400

/** \fn void initializePWM()
 * \brief Sets up timer 1 to out compare match on channel A.
 * \param void
 * \return void
 */
void initializePWM( void )
{
	/*//Set to Fast PWM mode.  Clear on compare of OCR1A
	TCCR1A = ((1 << COM1A1) | (1 << WGM11));
	//Set prescaler to 8
	TCCR1B = ((1 << WGM13) | (1 << WGM12) | (1 << CS11));
	//Set bit to enable Compare A of Timer 1
	TIMSK1 = (1 << OCIE1B);
	//Setting 20 ms period Top value to ICR1
	ICR1 = 20000;
	OCR1A = SERVO_LEFT;
	OCR1B = 19999;

	DDRD |= 0x20;*/
    /* Both outputs are clear on match, and set on top,
     * top is ICR2.
     */
    TCCR1A = 0xa2; // clear
    /* Mode configuration continued,
     * prescalar clock set to divide by 8.
     */
    TCCR1B = (3<<3) | (2);

    /* assuming a 8Mhz system clock,
     * a 0.020 millisecond period is
     * 0.020 / 0.000001 = 20000
     */
    ICR1 = 20000;

    DDRD |= _BV(5) | _BV(4); // enable timer1 pwm outputs
    setDutyCycle(1475);
}

/** \fn void setDutyCycle(unsigned int dutyCycle)
 * \brief Sets the duty cycle of the signal pulse to the given value.
 * \param unsigned int dutyCycle - 1000 to 2000.
 * \return void
 */
void setDutyCycle(unsigned int dutyCycle)
{
	//Sets Top value in the OCR1A Register
	OCR1A = dutyCycle;
}

/** \fn void requestStepperPosition()
 * \brief Handles client request for setting the stepper motor's direction
 */
void requestSetServo(){
	while(commandsInQueue() < 1){}
	setDutyCycle(readCommand() * 10);
}

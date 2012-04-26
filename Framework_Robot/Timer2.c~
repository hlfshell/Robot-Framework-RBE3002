/*
 * Timer2.c
 *
 *  Created on: Apr 3, 2009
 *      Author: Keith Chester
 *
 *  Sets up and maintains timer2 happenings.
 */

#include "FunctionalHeader.h"

/** \fn void InitializeTimer2()
 * \brief Initializes timer 2 for a high interrupt rate for the global clock.
 * \param void
 * \return void
 */
void InitializeTimer2(){
	TCCR2B = (1 << CS22) | (1 << CS21) | (1 << CS20);
	TIMSK2 = (1 << TOIE2);
	//TCCR0B = (1 << CS22);
	//TIMSK0 = (1 << TOIE0);
}

/* ISR(TIMER2_OVF_vect
 * \brief Interrupt control for timer 2.
 */
ISR(TIMER2_OVF_vect){
	//turretMoveStepper();
	//moveStepper();
}

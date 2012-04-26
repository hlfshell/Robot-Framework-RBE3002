/** \brief Reads the analog to digital convertor for the requested channel.
 *
 * \file ADC.c
 *
 * This file manages the analog to digital convertor - from initialization
 * to actually reading the current value. It also handles voltage to degree
 * conversions required to use the arm's potentiometer.
 *
 * \author keithc@wpi.edu
 * \version 1
 */

#include "FunctionalHeader.h"

/** \fn void InitializeA2D()
 * \brief Initialize the Analog to Digital Convertor.
 * \param void
 * \return void
 */
void InitializeA2D(){
	ADCSRA &= ~(1 << ADATE);
    ADCSRA |= (1 << ADEN) | (1 << ADPS0 ) | (1 << ADPS1 );
	ADCSRA &= ~(1 << ADPS2 );
}

/** \fn unsigned int get_adc(unsigned char adc_channel)
 * \brief Accepts the adc channel desired to be read and returns the current voltage on that channel.
 * \param unsigned char adc_channel
 * \return unsigned int adc_high_byte
 */
unsigned int get_adc(unsigned char adc_channel){
	if(adc_channel > 7) return 0;
	unsigned char adc_low_byte = 0, adc_high_byte = 0;
	ADMUX = adc_channel;
	ADCSRA |= (1 << ADSC);
	while((ADCSRA & (1 << ADIF))  == 0){}; //Wait until the adc grab is complete
	adc_low_byte = ADCL;
	adc_high_byte = ADCH;
	ADCSRA |= (1 << ADIF);

	return (int) adc_high_byte * 256 + adc_low_byte; //Convert high and low bit to single value.
}

/** \fn void requestADCchannel(void)
 * \brief Handles client request for an ADC channel's value
 */
void requestADCchannel(){
	char channel;
	unsigned int value;
	while(commandsInQueue() < 1){}
	channel = readCommand();
	value = get_adc(channel);
	serialTx(value);
	serialTx((value >> 8));
}

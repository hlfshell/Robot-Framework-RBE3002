/** \brief Controls both of the arm's motors via SPI.
 *
 * \file motorControl.c
 *
 * Controls spi communication for motor control, as well as general
 * motor control functions.
 *
 * \author keithc@wpi.edu
 * \version 1
 */

#include "FunctionalHeader.h"

/** \fn void SPIInit()
 * \brief Initializes the SPI Motor Control
 * \param void
 * \return void
 */
//void InitializeMotor( void)
//{
//      DDR_SPI  = (_BV(SS)|_BV(SCK)|_BV(MOSI));
//      SPI_PORT |= (1<<SS);
//      SPI_CTRL = SPI_EN;
//}
//
///** \fn void SPITx( unsigned char high_byte, unsigned char low_byte)
// * \brief Transmits a low and high byte over SPI, high byte first.
// * \param unsigned char high_byte, unsigned char low_byte
// * \return void
// */
//void SPITx( unsigned char high_byte, unsigned char low_byte)
//{
//      SPI_PORT &= ~(1<<SS);
//      SPI_DATA = high_byte;
//      while ( !( SPSR & (1<<SPIF)) ){}
//      SPI_DATA = low_byte;
//      while ( !( SPSR & (1<<SPIF)) ){}
//      SPI_PORT |= (1<<SS);
//}
//
///** \fn void motorControl(char motor, int inputValue)
// * \brief Allows for a motor voltage (-2048 to 2048) to be chosen an converts it for SPI.
// * \param char motor, int inputValue
// * \return void
// */
//void motorControl(char motor, int inputValue){
//	if(inputValue > 2048) inputValue = 2048;
//	else if(inputValue < -2048) inputValue = -2048;
//	if(inputValue < 0) inputValue = 2048 + inputValue;
//	else if(inputValue > 0) inputValue = 2048 + inputValue;
//	else inputValue = 2048;
//	dacControl(2048, 0);//(unsigned int) inputValue, 0);//(unsigned int) inputValue, motor);
//}
//
//
///** \fn void dacControl(unsigned int valueDesired, char channel)
// * \brief Takes the desired voltage and adds the DAC address bit for the channel to the output.
// * \param unsigned int valueDesired, char channel
// * \return void
// */
//void dacControl(unsigned int valueDesired, char channel){
//	unsigned char outputHigh = 0, outputLow = 0;
//	if(valueDesired < 0 ) valueDesired = 0;
//	if(valueDesired > 4095) valueDesired = 4095;
//
//	//The following if statements determine what information to append
//	//to the output to the DAC in order to select the proper channel.
//	if(channel == LEFTMOTOR) outputHigh = (1 << 7) | (1 << 5) | (valueDesired >> 8);
//	else if(channel == RIGHTMOTOR) outputHigh = (1 << 7) | (1 << 4) | (valueDesired >> 8);
//
//	outputLow = valueDesired;
//	SPITx(outputHigh, outputLow);
//}

/** \fn void requestLeftMotor()
 * \brief Takes the desired voltage and adds the DAC address bit for the channel to the output.
 */
void setLeftMotorForward(){
	while(commandsInQueue() < 1){}
	motorControl(0, readCommand() * 10);
}

void setLeftMotorReverse(){
	while(commandsInQueue() < 1){}
	motorControl(0, readCommand() * -10);
}

/** \fn void requestRightMotor()
 * \brief Takes the desired voltage and adds the DAC address bit for the channel to the output.
 */
void setRightMotorForward(){
	while(commandsInQueue() < 1){}
	motorControl(1, readCommand() * 10);
}

void setRightMotorReverse(){
	while(commandsInQueue() < 1){}
	motorControl(1, readCommand() * -10);
}

/** \brief Controls both of the arm's motors via SPI.
 *
 * \file motorControl.c
 *
 * Controls spi communication for motor control, as well as general
 * motor control functions.
 *
 * \author keithc@wpi.edu
 * \version 1
 */

#include "FunctionalHeader.h"

/** \fn void SPIInit()
 * \brief Initializes the SPI Motor Control
 * \param void
 * \return void
 */
void SPIInit( void)
{
      DDR_SPI  = (_BV(SS)|_BV(SCK)|_BV(MOSI));
      SPI_PORT |= (1<<SS);
      SPI_CTRL = SPI_EN;
}


/** \fn void SPITx( unsigned char high_byte, unsigned char low_byte)
 * \brief Transmits a low and high byte over SPI, high byte first.
 * \param unsigned char high_byte, unsigned char low_byte
 * \return void
 */
void SPITx( unsigned char high_byte, unsigned char low_byte)
{
      SPI_PORT &= ~(1<<SS);
      SPI_DATA = high_byte;
      while ( !( SPSR & (1<<SPIF)) ){}
      SPI_DATA = low_byte;
      while ( !( SPSR & (1<<SPIF)) ){}
      SPI_PORT |= (1<<SS);
}

/** \fn void motorControl(char motor, int inputValue)
 * \brief Allows for a motor voltage (-2048 to 2048) to be chosen an converts it for SPI.
 * \param char motor, int inputValue
 * \return void
 */
void motorControl(char motor, int inputValue){
	if(inputValue > 2048) inputValue = 2048;
	else if(inputValue < -2048) inputValue = -2048;
	if(inputValue < 0) inputValue = 2048 + inputValue;
	else if(inputValue > 0) inputValue = 2048 + inputValue;
	else inputValue = 2048;
	dacControl((unsigned int) inputValue, motor);
}

///** \fn void magnetControl(unsigned int inputValue);
// * \brief allows easy pass-through control of the electromagnet
// * \param unsigned int inputValue
// * \return void
// */
//void magnetControl(unsigned int inputValue){
//	dacControl(inputValue, MAGNET);
//}

#define A 0
#define B 1

/** \fn void dacControl(unsigned int valueDesired, char channel)
 * \brief Takes the desired voltage and adds the DAC address bit for the channel to the output.
 * \param unsigned int valueDesired, char channel
 * \return void
 */
void dacControl(unsigned int valueDesired, char channel){
	unsigned char outputHigh = 0, outputLow = 0;
	if(valueDesired < 0 ) valueDesired = 0;
	if(valueDesired > 4095) valueDesired = 4095;

	//The following if statements determine what information to append
	//to the output to the DAC in order to select the proper channel.
	if(channel == A) outputHigh = (1 << 7) | (1 << 4) | (1 << 5) | (valueDesired >> 8);
	else if(channel == B) outputHigh = (1 << 7) | (1 << 4) | (valueDesired >> 8);
	//else if(channel == MAGNET) outputHigh = (1 <<7) | (1 << 5) | (valueDesired >> 8);

	outputLow = valueDesired;
	SPITx(outputHigh, outputLow);
}

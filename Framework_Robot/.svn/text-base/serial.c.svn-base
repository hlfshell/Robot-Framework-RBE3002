/** \brief Controls serial communication
 *
 * \file serial.c
 *
 * Initializes and controls serial communication
 *
 * \author keithc@wpi.edu
 * \version 1
 */

#include "FunctionalHeader.h"

volatile char commandBuffer[BUFFERSIZE];
volatile int bufferStepThrough = 0;
volatile int commandCount = 0;

/** \fn void InitializeSerial()
 * \brief Initializes the USART0.
 * \param void
 * \return void
 */
void InitializeSerial(void)
{
                UBRR0H = (unsigned char)(BAUD_CALC>>8);//Set baud rate
                UBRR0L = (unsigned char)BAUD_CALC;//Set baud rate
                UCSR0B = _BV(TXEN0) | _BV(RXEN0) | _BV(RXCIE0);
                UCSR0C = (1<<USBS0)|(3<<UCSZ00);//Set frame format
}


/** \fn void serialTx( unsigned char output )
 * \brief Transmits an individual byte over serial.
 * \param unsigned char output
 * \return void
 */
void serialTx( unsigned char output )
{
	//Disable timer interrupts during this sending
	//TIMSK2 = 0;
	//TIMSK1 = 0;
                while ( !( UCSR0A & (1<<UDRE0)) ){//Wait to see if buffer is empty
                }
                UDR0 = output;//Sends data through buffer
                //TIMSK2 = (1 << TOIE2); //reenable interrupts after send
                //TIMSK1 = (1 << OCIE1B);
}

/** \fn unsigned char serialRx()
 * \brief Receives an individual byte for serial and echoes it back.
 * \param void
 * \return unsigned char received
 */
unsigned char serialRx( void )
{
                char received = UDR0;
                serialTx(received);//echos data recived
                return received;//Get and return received data
}

/** \fn void serialTxString( char * str)
 * \brief Transmits a string, byte by byte, until it sees a null terminator.
 * \param char * str
 * \return void
 */
void serialTxString(char * str) {
                int i=0;
                while(str[i] != '\0') {
                	serialTx(str[i++]);
                }
}

/** \fn void addToBuffer(char newInput)
 * \brief Given a new element, add it to the end of the buffer
 *  given we have not already filled it. If the buffer is full,
 *  it will OVERWRITE THE RECENT COMMANDS, so BEWARE.
 * \param newInput - a new character byte to add.
 * \return void
 */
void addToBuffer(char newInput){
	bufferStepThrough++;
	commandCount++;
	if(bufferStepThrough >= BUFFERSIZE) bufferStepThrough = 0;
	commandBuffer[bufferStepThrough] = newInput;
}

/** \fn char readCommand(void)
 * \brief returns the most recent command in the buffer.
 * \param void
 * \return void
 */
char readCommand(void){
	char tmp = commandBuffer[bufferStepThrough];
	if(bufferStepThrough == 0) bufferStepThrough = BUFFERSIZE - 1;
	else bufferStepThrough--;
	commandCount--;
	return tmp;
}

/** \fn char isThereACommand(void)
 * \brief Returns 1 if true, 0 if false.
 * \param void
 * \return void
 */
char isThereACommand(void){
	if(commandCount > 0) return 1;
	else return 0;
	return 0; //This should never be reached, really.
}

/** \fn int commandsInQueue(void)
 * \brief Returns the amount of commands in queue
 * \param void
 * \return int
 */
int commandsInQueue(void){
	return commandCount;
}

/** \fn ISR(USART0_RX_vect)
 * \brief Handles serial receive interrupts.
 * \param void
 * \return void
 */
ISR(USART0_RX_vect){
	addToBuffer(UDR0); //Add to buffer
}

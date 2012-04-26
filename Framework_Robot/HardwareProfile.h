/*
 * HardwareProfile.h
 *
 *  Created on: Mar 30, 2009
 *      Author: Keith Chester
 *
 * If it effects the HARDWARE the robot is on, such as pin
 * #s, put it in here.
 */

#ifndef HARDWAREPROFILE_H_
#define HARDWAREPROFILE_H_

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdlib.h>


#define BAUDRATE 19200
#define BAUD_CALC ((F_CPU/BAUDRATE/16)-1)

//SPI Declarations
#define MOSI                  PB5
#define SCK                   PB7
#define SS                    PB4
#define SSACCEL				  PB2
#define DDR_SPI               DDRB
#define SPI_PORT        PORTB
#define SPI_CTRL        SPCR
#define SPI_EN                (_BV(SPE)|_BV(MSTR)|_BV(SPR0)|_BV(SPR1)|_BV(CPHA))
#define SPI_DATA        SPDR

#endif /* HARDWAREPROFILE_H_ */

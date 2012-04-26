/*
 * Commands.h
 *
 *  Created on: Apr 1, 2009
 *      Author: Keith Chester
 *
 *  This file holds declarations of values of commands. This should
 *  match the client side's declartaion of commands for organizational
 *  reasons. These values are the bytes being sent when the framework
 *  is calling that command.
 */

#ifndef COMMANDS_H_
#define COMMANDS_H_

#define SETID  0x00
#define REQUESTID 0x01
#define INITIALIZEROBOT 0x02
#define RESET 0x03

#define REQUESTPINVALUE 0xA0
#define REQUESTADCCHANNEL 0xA1

#define ENABLEMOTORS 0xC0
#define DISABLEMOTORS 0xC1
#define SETPID 0xC3
#define SETLEFTMOTOR 0xC4
#define SETRIGHTMOTOR 0xC5
#define SENDSTEPPERTO 0xC6
#define REQUESTSETSERVO 0xD0
#define SETLEFTMOTORFORWARD 0xD1
#define SETLEFTMOTORREVERSE 0xD2
#define SETRIGHTMOTORFORWARD 0xD3
#define SETRIGHTMOTORREVERSE 0xD4

#define PING 0xFF



#define SUCCESS 0xFF
#define FAILURE 0x00

#endif /* COMMANDS_H_ */

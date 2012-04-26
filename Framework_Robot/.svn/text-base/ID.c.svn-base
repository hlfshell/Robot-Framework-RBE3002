/*
 * ID.c
 *
 *  Created on: Mar 30, 2009
 *      Author: Keith Chester
 *
 * So why do we have an Identification System? This is for when
 * we need multiple robots. This way you can implement easily later
 * an "ID" check for each command. If multiple robots are on the same
 * "channel," the "ID" check tells the robot to ignore the command
 * or not.
 *
 * Possible future expansions: GROUP IDs so you create multiple groups
 * for multi-commands.
 */

#include "FunctionalHeader.h"

char IDNumber;

void setID(){
	while(commandsInQueue() < 1){} //Don't go reading bytes that aren't there.
	IDNumber = readCommand();
}

void requestID(){
	serialTx(IDNumber);
}

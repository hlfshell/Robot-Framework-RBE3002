/*
 * main.c
 *
 *  Created on: Mar 30, 2009
 *      Author: Keith Chester
 *
 *  The circus tent of everything main.
 */
#include "FunctionalHeader.h"

extern char INITIALIZED; //Grab the initialization state from elsewhere

int main(){

	InitializeHardware();
	while(INITIALIZED == 0) if(isThereACommand()) commandMenu(); //Wait until you get the "go" from client

	while(1){
		//Do stuff if you want. I mean, you don't have to. But it'd be nice.
		if(isThereACommand()) commandMenu();
	}

	return 0;
}

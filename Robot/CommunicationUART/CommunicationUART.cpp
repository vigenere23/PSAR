//
// Created by Dominic on 2020-02-07.
//

#include "CommunicationUART.h"

CommunicationUART::CommunicationUART(PinName txPinName, PinName rxPinName):
rPiSerial(txPinName, rxPinName)
 {

    //  IN
    //     ROTATE:[-100, 100]
    //     MOVE:50,50
    //     RESISTOR
    //     GRIPPER:[0,1]

    // OUT
    //     POWER:M1POWER,M2POWER,M3POWER,M4POWER,GRIPPERPOWER,(STM)
    //     PUCKTAKEN:[0,1]

    // UART communication Setup
    rPiSerial.baud(19200);
    rPiSerial.printf("bonjour\n");
    thread.start(callback(this, &CommunicationUART::handleUART));
}

void CommunicationUART::handleUART(){
    while(1){
        //Example pour ayoub
        // char a[]="MOVE:25,40";
        // char b[]="MOVE";
        // char *output = NULL;
        // output = strstr (a,b);
        // int x;
        // int y;
        // if(output) {
        //     printf("String Found");
        //     sscanf (a, "MOVE:%d,%d", &x, &y);
        //     printf("the value x is : %d, the value y is : %d", x, y);
        // }

    }
}
//
// Created by Dominic on 2020-02-07.
//

#include "CommunicationUART.h"

CommunicationUART::CommunicationUART(PinName txPinName, PinName rxPinName):
rPiSerial(txPinName, rxPinName)
 {
    // UART communication Setup
    rPiSerial.baud(19200);
    rPiSerial.printf("bonjour\n\r");
    thread.start(callback(this, &CommunicationUART::handleUART));
}

void CommunicationUART::handleUART(){
    while(1){
        // exemple echo back character on the serial
        rPiSerial.putc(rPiSerial.getc());
        // example echo back string when space or enter receive
        // char str[80];
        // scanf ("%79s",str);
        // printf("%s\n", str);
    }
}
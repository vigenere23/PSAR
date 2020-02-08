//
// Created by Dominic on 2020-02-07.
//

#ifndef EMBEDDED_COMMUNICATIONUART_H
#define EMBEDDED_COMMUNICATIONUART_H

#include "mbed.h"
#include "rtos.h"

class CommunicationUART {
private:
    Thread thread;
    Serial rPiSerial;  // tx, rx
    void handleUART();

public:
    CommunicationUART(PinName txPinName, PinName rxPinName);

};


#endif //EMBEDDED_COMMUNICATIONUART_H

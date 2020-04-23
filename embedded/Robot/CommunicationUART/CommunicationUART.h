//
// Created by Dominic on 2020-02-07.
//

#ifndef EMBEDDED_COMMUNICATIONUART_H
#define EMBEDDED_COMMUNICATIONUART_H

#include "mbed.h"
#include "rtos.h"
#include "Robot.h"

class Robot;
class CommunicationUART {
private:
    // Thread thread;
    Robot* robot;
    void read_data();
    int rx_index = 0;
    char rx_buffer[80];
    bool input_available = false;

public:
    RawSerial rPiSerial;  // tx, rx
    void handleUART();
    CommunicationUART(Robot* robot, PinName txPinName, PinName rxPinName);

};


#endif //EMBEDDED_COMMUNICATIONUART_H
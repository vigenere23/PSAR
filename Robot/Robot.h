//
// Created by Dominic on 2020-02-06.
//

#ifndef EMBEDDED_ROBOT_H
#define EMBEDDED_ROBOT_H
#include "mbed.h"
#include "CommunicationUART/CommunicationUART.h"


class Robot {
private:
    CommunicationUART communicationUART;
    AnalogIn analogInServo1; // current measurement
    AnalogIn analogInServo2;
    AnalogIn analogInMotor1;
    AnalogIn analogInMotor2;
    AnalogIn analogInMotor3;
    AnalogIn analogInMotor4;
    AnalogIn analogInResistor;

public:
    Robot();
};


#endif //EMBEDDED_ROBOT_H

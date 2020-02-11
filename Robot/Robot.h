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
    AnalogIn analogInServo1; // voltage measurement
    AnalogIn analogInServo2;
    AnalogIn analogInMotor1;
    AnalogIn analogInMotor2;
    AnalogIn analogInMotor3;
    AnalogIn analogInMotor4;
    AnalogIn analogInResistor;

public:
    Robot();
    void move(int x, int y);
    void rotate(int directionSpeed);
    unsigned int getResistor();
    void setGripper(bool state);
};


#endif //EMBEDDED_ROBOT_H

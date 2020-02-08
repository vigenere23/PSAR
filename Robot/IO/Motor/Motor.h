//
// Created by Dominic on 2020-02-06.
//

#ifndef EMBEDDED_MOTOR_H
#define EMBEDDED_MOTOR_H

#include "mbed.h"
typedef enum {
    MOTOR_NOTHING = 0,
    MOTOR_CW      = 1,     // CW   => CLOCK WISE
    MOTOR_CCW     = 2,     // CCW  => COUNTER CLOCK WISE
    MOTOR_BRAKE   = 3
} MotorMode;

class Motor {

private:
    InterruptIn enc1;
    InterruptIn enc2;
    PwmOut pwmOut;
    Ticker motorControlInterrupt;
    DigitalOut motorModeDigitalOut1;
    DigitalOut motorModeDigitalOut2;
    MotorMode motorMode;
    unsigned int targetMotorSpeed = 0;
    unsigned int actualMotorSpeed = 0;
    void enc1Rising();
    void enc1Falling();
    void enc2Rising();
    void enc2Falling();
    void motorControl();

public:
    Motor(PinName enc1PinName, PinName enc2PinName, PinName pwmOutPinName, PinName motorMode1PinName, PinName motorMode2PinName);
    void setMotorMode(MotorMode motorMode);
    unsigned int getMotorMode() { return motorMode; }
    void setTargetMotorSpeed(unsigned int newTargetMotorSpeed);
    unsigned int getTargetMotorSpeed() { return targetMotorSpeed; }


};


#endif //EMBEDDED_MOTOR_H

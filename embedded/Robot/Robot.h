//
// Created by Dominic on 2020-02-06.
//
#ifndef EMBEDDED_ROBOT_H
#define EMBEDDED_ROBOT_H
#include "mbed.h"
#include "CommunicationUART.h"
#include "Motor.h"
#include "Encoder.h"
#define ENC_1_1_Pin GPIO_PIN_1
#define ENC_1_2_Pin GPIO_PIN_5
#define ENC_2_1_Pin GPIO_PIN_6
#define ENC_2_2_Pin GPIO_PIN_7
#define ENC_3_1_Pin GPIO_PIN_12
#define ENC_3_2_Pin GPIO_PIN_13
#define ENC_4_1_Pin GPIO_PIN_6
#define ENC_4_2_Pin GPIO_PIN_7
class CommunicationUART;

class Robot {
private:
    AnalogIn analogInServo1; // voltage measurement
    AnalogIn analogInServo2;
    AnalogIn analogInMotor1;
    AnalogIn analogInMotor2;
    AnalogIn analogInMotor3;
    AnalogIn analogInMotor4;
    AnalogIn analogInResistor;
    int moveX = 0;
    int moveY = 0;
    int rotationSpeed = 0;
    void updateMotorsTarget();
    TIM_Encoder_InitTypeDef encoderMotor1, encoderMotor2, encoderMotor3, encoderMotor4;
    void initEncoder();
    void initEncoderGPIO();
    void setCom(CommunicationUART *communicationUART);
    Ticker motorControlInterrupt;
    void motorControl();    

public:
    CommunicationUART *communicationUART;
    Motor motor1;
    Motor motor2;
    Motor motor3;
    Motor motor4;
    Robot();
    void move(int x, int y);
    void rotate(int rotationSpeed);
    unsigned int getResistor();
    void setGripper(bool state);
    TIM_HandleTypeDef  timerMotor1,  timerMotor2,  timerMotor3,  timerMotor4;

};


#endif //EMBEDDED_ROBOT_H

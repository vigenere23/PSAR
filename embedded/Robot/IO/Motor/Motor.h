//
// Created by Dominic on 2020-02-06.
//

#ifndef EMBEDDED_MOTOR_H
#define EMBEDDED_MOTOR_H
#include "mbed.h"

#define MAX_ERROR_SUM 4000
#define MIN_ERROR_SUM -4000

/// Speed PID configuration
#define DT (0.01) // [s] time between passes
#define SPEED_KP (0.2)
#define SPEED_KI (0.01)
#define MAX_VOLT_I (12) // [V] Windup for integrator
#define MAX_PWM_VALUE (1024)

#define ENCODER_TO_TURN_FACTOR (3200.0)
#define SPEED_FILTER_AMOUNT (1)
#define TARGET_FILTER_AMOUNT (0.1)
#define MAX_ENCODER_VALUE 65535

#define CURRENT_VOLT() (14) // Hardcode 12V

#define MAX_RPM 97.0

// Util function to filter a signal
#define MATH_LOWPASS(var, new, strength) var -= (strength * ((var) - (new)))


typedef enum {
    MOTOR_NOTHING = 0,
    MOTOR_CW      = 1,     // CW   => CLOCK WISE
    MOTOR_CCW     = 2,     // CCW  => COUNTER CLOCK WISE
    MOTOR_BRAKE   = 3
} MotorMode;

class Motor {

private:
    TIM_HandleTypeDef *timer;
    PwmOut pwmOut;
    DigitalOut motorModeDigitalOut1;
    DigitalOut motorModeDigitalOut2;
    MotorMode motorMode;
    float targetMotorSpeed = 0;
    float targetMotorSpeedFiltered = 0;
    float sens = 1;
    float voltage = 0;
    float speedMotor = 0;

    //Variable pour l'asservissement
    int speedMotorErrorPrevious = 0;
    int speedMotorErrorSum = 0;
    int speedMotorError = 0;
    float integrator = 0.0f; // Integrator
    long last_count = 0;
    void motorSetVoltage();

public:
    void motorControl();
    Motor(TIM_HandleTypeDef *timer, PinName pwmOutPinName, PinName motorMode1PinName, PinName motorMode2PinName, float sens);
    void setMotorMode(MotorMode motorMode);
    unsigned int getMotorMode() const { return motorMode; }
    void setTargetMotorSpeed(float newTargetMotorSpeed);
    float getTargetMotorSpeed() const { return (((float)targetMotorSpeedFiltered/100.0f)*MAX_RPM); }
};


#endif //EMBEDDED_MOTOR_H

//
// Created by Dominic on 2020-02-06.
//

#include "Motor.h"

Motor::Motor(PinName enc1PinName, PinName enc2PinName, PinName pwmOutPinName, PinName motorMode1PinName, PinName motorMode2PinName):
enc1(enc1PinName), enc2(enc2PinName), pwmOut(pwmOutPinName), motorModeDigitalOut1(motorMode1PinName), motorModeDigitalOut2(motorMode2PinName)  {
    // ENC setup
    
    enc1.rise(callback(this, &Motor::enc1Rising));
    enc1.fall(callback(this, &Motor::enc1Falling));
    enc2.rise(callback(this, &Motor::enc2Rising));
    enc2.fall(callback(this, &Motor::enc2Falling));

    // PWM Setup
    pwmOut.period(1.0f);   // 1 second period
    pwmOut.write(0.50f);  // 50% duty cycle, relative to period

    // Motor Mode Setup
    motorMode = MOTOR_NOTHING;

    // Motor Control Setup
    motorControlInterrupt.attach(callback(this, &Motor::motorControl), 1.0); // the address of the function to be attached (flip) and the interval (1 seconds)
}
void Motor::setMotorMode(MotorMode newMotorMode) {
    motorMode = newMotorMode;
    // change motorModeDigitalOut1 and motorModeDigitalOut1 according to the motor mode
}

void Motor::enc1Rising() {

}

void Motor::enc1Falling() {

}

void Motor::enc2Rising() {

}

void Motor::enc2Falling() {

}

void Motor::motorControl() {
    // this function manage the pwm out and calculate the pid
}

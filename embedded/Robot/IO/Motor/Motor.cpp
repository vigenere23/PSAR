//
// Created by Dominic on 2020-02-06.
//

#include "Motor.h"


Motor::Motor(TIM_HandleTypeDef *timer, PinName pwmOutPinName, PinName motorMode1PinName, PinName motorMode2PinName, float sens):
pwmOut(pwmOutPinName), motorModeDigitalOut1(motorMode1PinName), motorModeDigitalOut2(motorMode2PinName)  {
    // ENC setup
    this->timer = timer;
    // PWM Setup
    pwmOut.period(0.00001f);   // 0.01 second period
    pwmOut.write(0.0f);  // 0% duty cycle, relative to period

    // Motor Mode Setup
    motorMode = MOTOR_NOTHING;


    this->sens = sens;
}
void Motor::setMotorMode(MotorMode newMotorMode) {
    motorMode = newMotorMode;
    switch(motorMode){
        case MOTOR_NOTHING:
            motorModeDigitalOut1.write(0);
            motorModeDigitalOut2.write(0);
            break;
        case MOTOR_CW:
            motorModeDigitalOut1.write(0);
            motorModeDigitalOut2.write(1);
            break;
        case MOTOR_CCW:
            motorModeDigitalOut1.write(1);
            motorModeDigitalOut2.write(0);
            break;
        case MOTOR_BRAKE:
            motorModeDigitalOut1.write(1);
            motorModeDigitalOut2.write(1);
            break;
    }

}
void Motor::setTargetMotorSpeed(float newTargetMotorSpeed){
    targetMotorSpeed = newTargetMotorSpeed;
}

void Motor::motorSetVoltage(){
    float volt = voltage;
    if(volt == 0){
        setMotorMode(MOTOR_NOTHING);
    }
    else if (volt > 0){
        setMotorMode(MOTOR_CW);
    }
    else if (volt < 0) {
        volt *= -1;
        setMotorMode(MOTOR_CCW);
    }
    pwmOut.write((float)volt/CURRENT_VOLT());
    
}

void Motor::motorControl() {
    long count = __HAL_TIM_GET_COUNTER(timer);

    long err =  count - last_count;

    // Filter target
    MATH_LOWPASS(targetMotorSpeedFiltered, targetMotorSpeed, TARGET_FILTER_AMOUNT);

    err = err*sens;
    while (err > MAX_ENCODER_VALUE/2) err -= MAX_ENCODER_VALUE;
    while (err < -MAX_ENCODER_VALUE/2) err += MAX_ENCODER_VALUE;
    float new_speed = ((float)err) / ENCODER_TO_TURN_FACTOR / DT * 60;
    
    MATH_LOWPASS(speedMotor, new_speed, SPEED_FILTER_AMOUNT);

    float error = getTargetMotorSpeed() - speedMotor;

    // Perform PI
    float P = error * SPEED_KP;
    integrator += SPEED_KI * error;
    voltage = P + integrator;

    // Anti windup
    if(voltage > MAX_VOLT_I) {voltage = MAX_VOLT_I; integrator = MAX_VOLT_I - P;}
    if(voltage < -MAX_VOLT_I){voltage = -MAX_VOLT_I;  integrator = -MAX_VOLT_I - P;}

    motorSetVoltage();

    last_count = count;
}

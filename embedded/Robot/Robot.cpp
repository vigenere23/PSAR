//
// Created by Dominic on 2020-02-06.
//

#include "Robot.h"


Robot::Robot():
 analogInMotor1(PA_0), analogInMotor2(PA_0), 
 analogInMotor3(PA_0), analogInMotor4(PA_0), 
 analogInServo1(PA_0), analogInServo2(PA_0),
 analogInResistor(PA_0), 
 motor1(&timerMotor1, PE_9, PB_1, PE_7, 1),
 motor2(&timerMotor2, PE_11, PE_8, PE_10, -1),
 motor3(&timerMotor3, PE_13, PE_12, PE_15, -1),
 motor4(&timerMotor4, PE_14, PB_10, PB_11, -1)
 
{
    initEncoderGPIO();
    initEncoder();
    
    // Motor Control Setup
    motorControlInterrupt.attach(callback(this, &Robot::motorControl), DT); // the address of the function to be attached (flip) and the interval (1 seconds)

  
}


void Robot::initEncoder(){


    EncoderInit(&encoderMotor1, &timerMotor1, TIM2, 65535, TIM_ENCODERMODE_TI2);


    EncoderInit(&encoderMotor2, &timerMotor2, TIM3, 65535, TIM_ENCODERMODE_TI2);


    EncoderInit(&encoderMotor3, &timerMotor3, TIM4, 65535, TIM_ENCODERMODE_TI2);


    EncoderInit(&encoderMotor4, &timerMotor4, TIM8, 65535, TIM_ENCODERMODE_TI2);
}

void Robot::initEncoderGPIO(){
    GPIO_InitTypeDef GPIO_InitStruct;

// Encoders Motor 1
    __HAL_RCC_TIM2_CLK_ENABLE();
  
    __HAL_RCC_GPIOA_CLK_ENABLE();
    /**TIM2 GPIO Configuration    
    PA1     ------> TIM2_CH2
    PA5     ------> TIM2_CH1 
    */
    GPIO_InitStruct.Pin = ENC_1_1_Pin|ENC_1_2_Pin;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF1_TIM2;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

// Encoders Motor 2
    __HAL_RCC_TIM3_CLK_ENABLE();

    __HAL_RCC_GPIOA_CLK_ENABLE();
    /**TIM3 GPIO Configuration    
    PA6     ------> TIM3_CH1
    PA7     ------> TIM3_CH2 
    */
    GPIO_InitStruct.Pin = ENC_2_1_Pin|ENC_2_2_Pin;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM3;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

// Encoders Motor 3
    __HAL_RCC_TIM4_CLK_ENABLE();

    __HAL_RCC_GPIOD_CLK_ENABLE();
    /**TIM4 GPIO Configuration    
    PD12     ------> TIM4_CH1
    PD13     ------> TIM4_CH2 
    */
    GPIO_InitStruct.Pin = ENC_3_1_Pin|ENC_3_2_Pin;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF2_TIM4;
    HAL_GPIO_Init(GPIOD, &GPIO_InitStruct);

// Encoders Motor 4
    __HAL_RCC_TIM8_CLK_ENABLE();

    __HAL_RCC_GPIOC_CLK_ENABLE();
    /**TIM8 GPIO Configuration    
    PC6     ------> TIM8_CH1
    PC7     ------> TIM8_CH2 
    */
    GPIO_InitStruct.Pin = ENC_4_1_Pin|ENC_4_2_Pin;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    GPIO_InitStruct.Alternate = GPIO_AF3_TIM8;
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

}

void Robot::setCom(CommunicationUART *communicationUART){
    this->communicationUART = communicationUART;
}

unsigned int Robot::getResistor(){
    return 0;
}

void Robot::move(int x, int y){
    moveX = x;
    moveY = y;
    this->updateMotorsTarget();
    
}

void Robot::rotate(int rotationSpeed){
    this->rotationSpeed = rotationSpeed;
    this->updateMotorsTarget();
}

void Robot::updateMotorsTarget(){
    int motor1Target = max(min(moveX + rotationSpeed, 100), -100);
    int motor4Target = max(min(-moveX + rotationSpeed, 100), -100);
    int motor2Target = max(min(moveY + rotationSpeed, 100), -100);
    int motor3Target = max(min(-moveY + rotationSpeed, 100), -100);
    motor1.setTargetMotorSpeed(motor1Target);
    motor2.setTargetMotorSpeed(motor2Target);
    motor3.setTargetMotorSpeed(motor3Target);
    motor4.setTargetMotorSpeed(motor4Target);
}

void Robot::motorControl()
{
    motor1.motorControl();
    motor2.motorControl();
    motor3.motorControl();
    motor4.motorControl();
}

void Robot::setGripper(bool state){
    
}
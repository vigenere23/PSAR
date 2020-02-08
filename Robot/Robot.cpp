//
// Created by Dominic on 2020-02-06.
//

#include "Robot.h"


Robot::Robot():
communicationUART(SERIAL_TX, SERIAL_RX),
 analogInMotor1(PA_0), analogInMotor2(PA_0), 
 analogInMotor3(PA_0), analogInMotor4(PA_0), 
 analogInServo1(PA_0), analogInServo2(PA_0),
 analogInResistor(PA_0)
{


}
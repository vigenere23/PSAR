//
// Created by Dominic on 2020-02-07.
//

#include "CommunicationUART.h"

CommunicationUART::CommunicationUART(Robot *robot, PinName txPinName, PinName rxPinName):
rPiSerial(txPinName, rxPinName)
 {

    //  IN
    //     ROTATE:[-100, 100],0
    //     MOVE:[-100, 100],[-100, 100]
    //     RESISTOR:0,0
    //     GRIPPER:[0,1],0

    // OUT
    //     PUCKTAKENOWER,M3POWER,M4POWER,GRIPPERPOWER,(STM)
    //     PUCKTAKEN:[0,1]
    //     RESISTOR:Value

    // UART communication Setup
    this->robot = robot;
    rPiSerial.baud(19200);
    rPiSerial.attach(callback(this, &CommunicationUART::read_data));
    // thread.start(callback(this, &CommunicationUART::handleUART));


}

void CommunicationUART::handleUART(){
    if (input_available == true) {
        input_available = false;
        int param_1 = 0, param_2 = 0;
        int detecteur_pour_switch;
        char received[50];
        memset(received, 0, sizeof received);
        sscanf(rx_buffer, "%s", received);
        if(strstr(received,"MOVE"))
        {
            sscanf(received,"MOVE:%d,%d", &param_1, &param_2);
            robot->move(param_1, param_2);
        }
        else if(strstr(received,"ROTATE"))
        {
            sscanf (received,"ROTATE:%d,%d", &param_1, &param_2);
            robot->rotate(param_1);
        }
        else if(strstr(received,"GRIPPER"))
        {
            sscanf (received,"ROTATE:%d,%d", &param_1, &param_2);
            robot->setGripper(param_1);
        }
        else if(strstr(received,"RESISTANCE"))
        {
            sscanf (received,"RESISTANCE:%d,%d", &param_1, &param_2);
            robot->getResistor();
        }
    }
}

void CommunicationUART::read_data() 
{
    char c;
    while(rPiSerial.readable())
    {
        c = rPiSerial.getc();
       
        rx_buffer[rx_index] = c;
        rx_index ++;
        if(c == '\n' || c == '\r')
        {
            rx_buffer[rx_index] = '\0';
            input_available = true;
            rx_index = 0;         
        }
        rx_index = rx_index % 80;
    }
}
 

#include "CommunicationUART.h"
#include "Robot.h"
 
int main() {
    
    Robot robot;
    CommunicationUART communicationUART(&robot, SERIAL_TX, SERIAL_RX);

    robot.move(0, 0);
    while(1) {
        communicationUART.handleUART();
        // thread_sleep_for(1);
    }
}
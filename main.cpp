#include "Robot/Robot.h"
 
int main() {
    Robot robot;
    DigitalOut led1(LED1);
    while(1) {
        led1 = !led1;
        thread_sleep_for(500);
    }
}
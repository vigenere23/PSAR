# UART Communication between RaspberryPi and STM

## Commands *from* RPI *to* STM

- ### `MOVE:x_vextor,y_vector`

  Set the robot movement direction and speed.

  - `x_vextor`: vector representing x movement of the robot. (type : `int`; Possible values: [-100, 100])
  - `y_vextor`: vector representing y movement of the robot. (type : `int`; Possible values: [-100, 100])

- ### `ROTATE:rotation_speed,0`

  Set the robot rotation speed.

  - `rotation_speed`: speed of rotation for the robot. (type : `int`; Possible values: [-100 (CCW), 100 (CW)])

- ### `RESISTOR:0,0`

  Trigger resistor measurement.

- ### `GRIPPER:state,0`

  Activate or desactivate the gripper electromagnet

  - `state`: state of the electromagnet. (type : `boolean` [True: ON, False: OFF])

---

## Commands *from* STM *to* RPI

- ### `POWER:m1_power,m2_power,m3_power,m4_power,gripper_power,robot_power`

  Send to RPI all robot power readings.

  - `m1_power`: Power value of the motor 1 (type : `Int`)
  - `m2_power`: Power value of the motor 2 (type : `Int`)
  - `m3_power`: Power value of the motor 3 (type : `Int`)
  - `m4_power`: Power value of the motor 4 (type : `Int`)
  - `gripper_power`: Power value of the gripper (type : `Int`)
  - `robot_power`: Power value of the entire robot (type : `Int`)

- ### `GRIPPER_PROXIMITY:state`

  Send to RPI the gripper proximity sensor state

  - `state`: This boolean value indicate if there is something in near proximity of the gripper. (Like when the puck is taken)

- ### `RESISTOR:value`

  Send to RPI the resistor value

  - `value`: value of the resistor (type : `Int`)

- ### `BATTERY:charge`

  Send to RPI the battery charge

  - `charge`: percentage of charge of the battery (type : `Int`)

[BACK](./README.md)

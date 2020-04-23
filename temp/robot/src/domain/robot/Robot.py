from injector import inject
from socketio.client import Client
from src.domain.stm.STMWriter import STMWriter
from src.domain.robot.RobotPower import RobotPower


class Robot:

    @inject
    def __init__(self, socket: Client, stm_writer: STMWriter):
        self.__socket = socket
        self.__stm_writer = stm_writer

        self.move_x = 0
        self.move_y = 0

        self.rotation_speed = 0

        self.gripper_state = False

        self.__powers = RobotPower(0, 0, 0, 0, 0)
        self.__powers_changed_listeners = []

        self.__gripper_proximity = False
        self.__gripper_proximity_changed_listeners = []

        self.__resistor = 0
        self.__resistor_changed_listeners = []

    # Communication RPI -> STM

    def move(self, x: int, y: int):
        """
        Send via STMCommunicator the move command with x and y cartesian projection
            of the direction vector
        :param x: Speed of movement in X axis from -100 to 100
        :param y: Speed of movement in Y axis from -100 to 100
        """
        self.move_x = x
        self.move_y = y
        print(f"move: x: {x}, y: {y}")
        self.__stm_writer.send_move(self.move_x, self.move_y)

    def rotate(self, rotate_speed: int):
        """
        Send via STMCommunicator the rotate command with the rotation speed
        :param rotate_speed: Speed to turn from -100 to 100. Negative -> CCW, Positive -> CW
        """
        self.rotation_speed = rotate_speed
        print(f"rotate: rotate_speed: {rotate_speed}")
        self.__stm_writer.send_rotate(self.rotation_speed)

    def resistor_measurement(self):
        """
        Send via STMCommunicator the resistor command to trigger a resistor measurement
        """
        self.__stm_writer.send_mesure_resistance()

    def set_gripper_magnet(self, state: bool):
        """
        Send via STMCommunicator the gripper command to set the state of the electromagnet
        :param state: state of the electromagnet. (True: ON, False: OFF)
        """
        self.gripper_state = state
        self.__stm_writer.send_gripper_status(self.gripper_state)

    # Communication STM <- RPI
    # todo change to use Observer object instead like in BaseStation
    def add_powers_changed_listener(self, fn):
        self.__powers_changed_listeners.append(fn)

    def remove_powers_changed_listener(self, fn):
        self.__powers_changed_listeners.pop(fn)

    def add_gripper_proximity_changed_listener(self, fn):
        self.__gripper_proximity_changed_listeners.append(fn)

    def remove_gripper_proximity_changed_listener(self, fn):
        self.__gripper_proximity_changed_listeners.pop(fn)

    def add_resistor_changed_listener(self, fn):
        self.__resistor_changed_listeners.append(fn)

    def remove_resistor_changed_listener(self, fn):
        self.__resistor_changed_listeners.pop(fn)

    def trig_listeners(self, listeners_list, *arg):
        for listener_fn in listeners_list:
            self.__socket.start_background_task(listener_fn, arg)

    @property
    def powers(self):
        return self.__powers

    @powers.setter
    def powers(self, new_powers: RobotPower):
        self.__powers = new_powers
        self.trig_listeners(self.__powers_changed_listeners, self.__powers)

    @property
    def gripper_proximity(self):
        return self.__gripper_proximity

    @gripper_proximity.setter
    def gripper_proximity(self, new_state):
        self.__gripper_proximity = new_state
        self.trig_listeners(self.__gripper_proximity_changed_listeners, self.__gripper_proximity)

    @property
    def resistor(self):
        return self.__resistor

    @resistor.setter
    def resistor(self, new_resistor):
        self.__resistor = new_resistor
        self.trig_listeners(self.__resistor_changed_listeners, self.__resistor)

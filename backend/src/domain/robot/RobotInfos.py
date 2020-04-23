from src.domain.Observer import Observer
from src.domain.data_classes.Point2D import Point2D
from src.domain.robot.data_classes.Resistor import ResistorControl, ResistorInfo
from src.domain.robot.data_classes.RobotBattery import RobotBattery
from src.domain.robot.data_classes.RobotCamera import RobotCamera
from src.domain.robot.data_classes.RobotGripper import RobotGripperControl, RobotGripperInfo
from src.domain.robot.data_classes.RobotMovement import RobotMovement
from src.domain.robot.data_classes.RobotPowers import RobotPowers
from src.domain.robot.data_classes.RobotPuckTransporter import RobotPuckTransporterControl, RobotPuckTransporterInfo


class RobotInfos:
    def __init__(self):
        self.__position = Point2D(0, 0)
        self.position_observer = Observer()

        self.__camera = RobotCamera()
        self.camera_observer = Observer()

        self.__gripper_control = RobotGripperControl()
        self.gripper_control_observer = Observer()

        self.__gripper_info = RobotGripperInfo()
        self.gripper_info_observer = Observer()

        self.__movement = RobotMovement()
        self.movement_observer = Observer()

        self.__powers = RobotPowers()
        self.powers_observer = Observer()

        self.__puck_transporter_control = RobotPuckTransporterControl()
        self.puck_transporter_control_observer = Observer()

        self.__puck_transporter_info = RobotPuckTransporterInfo()
        self.puck_transporter_info_observer = Observer()

        self.__angle = 0
        self.angle_observer = Observer()

        self.__battery = RobotBattery()
        self.battery_observer = Observer()

        self.__resistor_control = ResistorControl()
        self.resistor_control_observer = Observer()

        self.__resistor_info = ResistorInfo()
        self.resistor_info_observer = Observer()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position: Point2D):
        self.__position = new_position
        self.position_observer.trig_listeners(new_position)

    @property
    def camera(self):
        return self.__camera

    @camera.setter
    def camera(self, new_camera: RobotCamera):
        self.__camera = new_camera
        self.camera_observer.trig_listeners(new_camera)

    @property
    def gripper_control(self):
        return self.__gripper_control

    @gripper_control.setter
    def gripper_control(self, new_gripper_control: RobotGripperControl):
        self.__gripper_control = new_gripper_control
        self.gripper_control_observer.trig_listeners(new_gripper_control)

    @property
    def gripper_info(self):
        return self.__gripper_info

    @gripper_info.setter
    def gripper_info(self, new_gripper_info: RobotGripperInfo):
        self.__gripper_info = new_gripper_info
        self.gripper_info_observer.trig_listeners(new_gripper_info)

    @property
    def movement(self):
        return self.__movement

    @movement.setter
    def movement(self, new_movement: RobotMovement):
        self.__movement = new_movement
        self.movement_observer.trig_listeners(new_movement)

    @property
    def powers(self):
        return self.__powers

    @powers.setter
    def powers(self, new_powers: RobotPowers):
        self.__powers = new_powers
        self.powers_observer.trig_listeners(new_powers)

    @property
    def puck_transporter_control(self):
        return self.__puck_transporter_control

    @puck_transporter_control.setter
    def puck_transporter_control(self, new_puck_transporter_control: RobotPuckTransporterControl):
        self.__puck_transporter_control = new_puck_transporter_control
        self.puck_transporter_control_observer.trig_listeners(new_puck_transporter_control)

    @property
    def puck_transporter_info(self):
        return self.__puck_transporter_info

    @puck_transporter_info.setter
    def puck_transporter_info(self, new_puck_transporter_info: RobotPuckTransporterInfo):
        self.__puck_transporter_info = new_puck_transporter_info
        self.puck_transporter_info_observer.trig_listeners(new_puck_transporter_info)

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, new_angle: int):
        self.__angle = new_angle
        self.angle_observer.trig_listeners(new_angle)

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, new_battery: RobotBattery):
        self.__battery = new_battery
        self.battery_observer.trig_listeners(new_battery)

    @property
    def resistor_control(self):
        return self.__resistor_control

    @resistor_control.setter
    def resistor_control(self, new_resistor_control: ResistorControl):
        self.__resistor_control = new_resistor_control
        self.resistor_control_observer.trig_listeners(new_resistor_control)

    @property
    def resistor_info(self):
        return self.__resistor_info

    @resistor_info.setter
    def resistor_info(self, new_resistor_info: ResistorInfo):
        self.__resistor_info = new_resistor_info
        self.resistor_info_observer.trig_listeners(new_resistor_info)

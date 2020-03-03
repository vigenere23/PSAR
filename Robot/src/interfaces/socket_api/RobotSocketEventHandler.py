from injector import inject
from socketio import ClientNamespace
from src.domain.data_classes.Resistor import ResistorControl
from src.domain.data_classes.RobotCamera import RobotCamera
from src.domain.data_classes.RobotGripper import RobotGripperControl
from src.domain.data_classes.RobotMovement import RobotMovement
from src.domain.data_classes.RobotPuckTransporter import RobotPuckTransporterControl
from src.domain.robot.Robot import Robot


class RobotSocketEventHandler(ClientNamespace):

    @inject
    def __init__(self, robot: Robot):
        super().__init__('/robot')
        self.robot = robot

    def on_movement(self, robot_movement_json: str):
        robot_movement: RobotMovement = RobotMovement.from_json(robot_movement_json)
        self.robot.move(robot_movement.x, robot_movement.y)
        self.robot.rotate(robot_movement.rotation)

    def on_gripper_control(self, robot_gripper_control_json: str):
        robot_gripper_control: RobotGripperControl = RobotGripperControl.from_json(robot_gripper_control_json)
        self.robot.set_gripper_magnet(robot_gripper_control.active)
        # todo add handle gripper position

    def on_camera(self, robot_camera_json: str):
        robot_camera: RobotCamera = RobotCamera.from_json(robot_camera_json)
        # todo handle robot camera

    def on_puck_transporter_control(self, robot_puck_transporter_control_json: str):
        robot_puck_transporter_control: RobotPuckTransporterControl = RobotPuckTransporterControl.from_json(
            robot_puck_transporter_control_json)
        # todo handle robot puck transporter control

    def on_resistor_control(self, resistor_control_json: str):
        resistor_control: ResistorControl = ResistorControl.from_json(resistor_control_json)
        if resistor_control.start_measurement:
            self.robot.resistor_measurement()

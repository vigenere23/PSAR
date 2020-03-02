from injector import inject
from src.domain.GlobalInfos import GlobalInfos
from src.domain.data_classes.RobotCamera import RobotCamera
from src.domain.data_classes.RobotGripper import RobotGripperControl
from src.domain.data_classes.RobotMovement import RobotMovement
from src.domain.data_classes.RobotPuckTransporter import RobotPuckTransporterControl
from src.domain.robot.RobotInfos import RobotInfos
from src.domain.robot.RobotEventEmitter import RobotEventEmitter
from src.domain.sequence.SequenceEventEmitter import SequenceEventEmitter
from src.domain.sequence.TaskContainer import TaskContainer
from src.domain.sequence.tasks.RobotMoveLoopTask import RobotMoveSquareTask


class RobotTestTaskContainer(TaskContainer):

    @inject
    def __init__(self,
                 global_infos: GlobalInfos,
                 robot_infos: RobotInfos,
                 sequence_event_emitter: SequenceEventEmitter,
                 robot_event_emitter: RobotEventEmitter,
                 robot_move_square_task: RobotMoveSquareTask):
        super().__init__(global_infos, sequence_event_emitter)
        self.__robot_infos = robot_infos
        self.__robot_event_emitter = robot_event_emitter
        self._add_task(robot_move_square_task)

    def create_robot_event_listeners(self):
        def robot_movement_changed_event_listener(robot_movement: RobotMovement):
            self.__robot_event_emitter.send_movement(robot_movement)

        def robot_camera_changed_event_listener(robot_camera: RobotCamera):
            self.__robot_event_emitter.send_camera(robot_camera)

        def robot_gripper_control_changed_event_listener(robot_gripper_control: RobotGripperControl):
            self.__robot_event_emitter.send_gripper(robot_gripper_control)

        def robot_puck_transporter_control_changed_event_listener(
                puck_transporter_control: RobotPuckTransporterControl):
            self.__robot_event_emitter.send_puck_transporter_control(puck_transporter_control)

        def setup():
            self.__robot_infos.movement_observer.add_listener(robot_movement_changed_event_listener)
            self.__robot_infos.camera_observer.add_listener(robot_camera_changed_event_listener)
            self.__robot_infos.gripper_control_observer.add_listener(robot_gripper_control_changed_event_listener)
            self.__robot_infos.puck_transporter_control_observer.add_listener(
                robot_puck_transporter_control_changed_event_listener)

        self.setup = setup

        def tear_down():
            self.__robot_infos.movement_observer.remove_listener(robot_movement_changed_event_listener)
            self.__robot_infos.camera_observer.remove_listener(robot_camera_changed_event_listener)
            self.__robot_infos.gripper_control_observer.remove_listener(robot_gripper_control_changed_event_listener)
            self.__robot_infos.puck_transporter_control_observer.remove_listener(
                robot_puck_transporter_control_changed_event_listener)

        self.tear_down = tear_down

    def _before_execution(self):
        self.create_robot_event_listeners()
        self.setup()

    def _after_execution(self):
        self.tear_down()

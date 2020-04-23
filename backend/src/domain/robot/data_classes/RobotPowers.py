from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RobotPowers:
    motor1: int = 0
    motor2: int = 0
    motor3: int = 0
    motor4: int = 0
    gripper: int = 0
    servos: int = 0
    robot: int = 0

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RobotMovement:
    x: int = 0          # motor speed in x direction [-100, 100] in reference to the robot
    y: int = 0          # motor speed in y direction [-100, 100] in reference to the robot
    rotation: int = 0   # rotation speed [-100, 100]

from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RobotGripperControl:
    active: bool = False
    position: int = 0


@dataclass_json
@dataclass
class RobotGripperInfo:
    active: bool = False
    making_contact: bool = False
    position: int = 0

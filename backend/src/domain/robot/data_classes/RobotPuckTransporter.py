from dataclasses import dataclass, field
from typing import List
from src.domain.data_classes.Puck import Puck
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RobotPuckTransporterControl:
    position: int = 0


@dataclass_json
@dataclass
class RobotPuckTransporterInfo:
    position: int = 0
    contain: List[Puck] = field(default_factory=list)



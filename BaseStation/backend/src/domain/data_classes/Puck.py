from dataclasses import dataclass
from src.domain.data_classes.Point2D import Point2D
from src.domain.robot.enums import ResistorColors
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Puck:
    position: Point2D
    color: ResistorColors

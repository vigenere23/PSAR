from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RobotBattery:
    charge: int = 0

    @property
    def time_remaining(self) -> int:
        # todo to implement
        return 0

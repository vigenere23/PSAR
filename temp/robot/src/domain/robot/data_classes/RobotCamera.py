from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RobotCamera:
    tilt_angle: int = 0                 # [-82.0, 41.5]
    pan_angle: int = 0                  # [-62.5, 62.5]
    stream_camera_feed: bool = False

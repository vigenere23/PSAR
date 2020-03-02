from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ResistorControl:
    start_measurement: bool


@dataclass_json
@dataclass
class ResistorInfo:
    value: int

    @property
    def first_digit(self) -> int:
        if self.value < 100:
            raise ValueError
        else:
            return int(str(self.value)[0])

    @property
    def second_digit(self) -> int:
        if self.value < 100:
            raise ValueError
        else:
            return int(str(self.value)[1])

    @property
    def multiplier(self) -> int:
        for i in range(8):
            if self.value/(10**i) < 100:
                return i
        raise ValueError

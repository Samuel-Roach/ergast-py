from dataclasses import dataclass
import datetime

@dataclass
class Timing:
    """
    Representation of a single timing from a lap in Formula One
    Timings may contain:
        driverId: String
        position: Integer
        time: datetime.time
    """

    def __init__(self, driverId: str, position: int, time: datetime.time) -> None:
        self.driverId = driverId
        self.position = position
        self.time = time
        pass

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
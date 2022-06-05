from dataclasses import dataclass
import datetime

@dataclass
class PitStop:
    """
    Representation of a single Pit Stop from a Formula One race
    PitStops may contain:
        driverId: String
        lap: Integer
        stop: Integer
        localTime: datetime.datetime
        duration: datetime.time
    """

    def __init__(self, driverId: str, lap: int, stop: int, localTime: datetime.datetime,
                 duration: datetime.time) -> None:
        self.driverId = driverId
        self.lap = lap
        self.stop = stop
        self.localTime = localTime
        self.duration = duration
        pass

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
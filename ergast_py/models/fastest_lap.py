from dataclasses import dataclass
from ergast_py.models.average_speed import AverageSpeed
import datetime

@dataclass
class FastestLap:
    """
    Representation of a Fastest Lap for a Formula One Driver
    Fastest Laps may contain:
        rank: Integer
        lap: Integer
        time: datetime.time
        averageSpeed: AverageSpeed
    """

    def __init__(self, rank: int, lap: int, time: datetime.time, averageSpeed: AverageSpeed) -> None:
        self.rank = rank
        self.lap = lap
        self.time = time
        self.averageSpeed = averageSpeed
        pass

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
""" FastestLap class """

import datetime
from dataclasses import dataclass

from ergast_py.models.average_speed import AverageSpeed


@dataclass
class FastestLap():
    """
    Representation of a Fastest Lap for a Formula One Driver

    Fastest Laps may contain:
        rank: Integer
        lap: Integer
        time: datetime.time
        average_speed: AverageSpeed
    """

    def __init__(self, rank: int, lap: int, time: datetime.time,
                 average_speed: AverageSpeed) -> None:
        self.rank = rank
        self.lap = lap
        self.time = time
        self.average_speed = average_speed

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, FastestLap) and (
            self.rank == __o.rank and
            self.lap == __o.lap and
            self.time == __o.time and
            self.average_speed == __o.average_speed
        )

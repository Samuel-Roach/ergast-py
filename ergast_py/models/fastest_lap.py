""" FastestLap class """

import datetime
from dataclasses import dataclass

from ergast_py.models.average_speed import AverageSpeed
from ergast_py.models.model import Model


@dataclass
class FastestLap(Model):
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

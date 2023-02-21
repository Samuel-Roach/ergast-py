""" FastestLap class """
import datetime
from dataclasses import dataclass

from ergast_py.models.average_speed import AverageSpeed
from ergast_py.models.base_model import BaseModel


@dataclass
class FastestLap(BaseModel):
    """
    Representation of a Fastest Lap for a Formula One Driver

    Fastest Laps may contain:
        rank: Integer
        lap: Integer
        time: datetime.time
        average_speed: AverageSpeed
    """

    rank: int
    lap: int
    time: datetime.time
    average_speed: AverageSpeed

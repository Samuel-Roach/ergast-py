""" PitStop class """

import datetime
from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class PitStop(Model):
    """
    Representation of a single Pit Stop from a Formula One race

    PitStops may contain:
        driver_id: String
        lap: Integer
        stop: Integer
        local_time: datetime.datetime
        duration: datetime.time
    """

    def __init__(self, driver_id: str, lap: int, stop: int, local_time: datetime.datetime,
                 duration: datetime.time) -> None:
        self.driver_id = driver_id
        self.lap = lap
        self.stop = stop
        self.local_time = local_time
        self.duration = duration

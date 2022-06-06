""" Timing class """

import datetime
from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class Timing(Model):
    """
    Representation of a single timing from a lap in Formula One
    Timings may contain:
        driver_id: String
        position: Integer
        time: datetime.time
    """

    def __init__(self, driver_id: str, position: int, time: datetime.time) -> None:
        self.driver_id = driver_id
        self.position = position
        self.time = time

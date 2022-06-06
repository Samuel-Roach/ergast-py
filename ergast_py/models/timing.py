""" Timing class """

import datetime
from dataclasses import dataclass


@dataclass
class Timing():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

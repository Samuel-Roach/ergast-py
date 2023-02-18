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

    driver_id: str
    position: int
    time: datetime.time

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Timing) and (
            self.driver_id == __o.driver_id and
            self.position == __o.position and
            self.time == __o.time
        )

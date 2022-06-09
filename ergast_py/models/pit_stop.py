""" PitStop class """

import datetime
from dataclasses import dataclass


@dataclass
class PitStop():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, PitStop) and (
            self.driver_id == __o.driver_id and
            self.lap == __o.lap and
            self.stop == __o.stop and
            self.local_time == __o.local_time and
            self.duration == __o.duration
        )

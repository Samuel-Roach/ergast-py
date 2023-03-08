""" Time class """

import datetime
from dataclasses import dataclass


@dataclass
class Time:
    """
    Representation of a Formula One Team

    Time may contain:
        millis: datetime.time
        time: String
    """

    def __init__(self, millis: datetime.time, time: str) -> None:
        self.millis = millis
        self.time = time

    def __repr__(self) -> str:
        members = ", ".join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Time) and (
            self.millis == __o.millis and self.time == __o.time
        )

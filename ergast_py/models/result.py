""" Result class """

import datetime
from dataclasses import dataclass

from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver
from ergast_py.models.fastest_lap import FastestLap


@dataclass
class Result():
    """
    Representation of a single Result from a Formula One race

    Results may contain:
        number: Integer
        position: Integer
        position_text: String
        points: Integer
        driver: Driver
        constructor: Constructor
        grid: Integer
        laps: Integer
        status: Integer
        time: datetime.time
        fastest_lap: FastestLap
        qual_1: datetime.time
        qual_2: datetime.time
        qual_3: datetime.time
    """

    number: int
    position: int
    position_text: str
    points: float
    driver: Driver
    constructor: Constructor
    grid: int
    laps: int
    status: int
    time: datetime.time
    fastest_lap: FastestLap
    qual_1: datetime.time
    qual_2: datetime.time
    qual_3: datetime.time

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Result) and (
            self.number == __o.number and
            self.position == __o.position and
            self.position_text == __o.position_text and
            self.points == __o.points and
            self.driver == __o.driver and
            self.constructor == __o.constructor and
            self.grid == __o.grid and
            self.laps == __o.laps and
            self.status == __o.status and
            self.time == __o.time and
            self.fastest_lap == __o.fastest_lap and
            self.qual_1 == __o.qual_1 and
            self.qual_2 == __o.qual_2 and
            self.qual_3 == __o.qual_3
        )

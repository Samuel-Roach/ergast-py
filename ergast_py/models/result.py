""" Result class """

import datetime
from dataclasses import dataclass

from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver
from ergast_py.models.fastest_lap import FastestLap
from ergast_py.models.model import Model


@dataclass
class Result(Model):
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

    def __init__(self, number: int, position: int, position_text: str, points: float,
                 driver: Driver, constructor: Constructor, grid: int, laps: int, status: int,
                 time: datetime.time, fastest_lap: FastestLap, qual_1: datetime.time,
                 qual_2: datetime.time, qual_3: datetime.time) -> None:
        self.number = number
        self.position = position
        self.position_text = position_text
        self.points = points
        self.driver = driver
        self.constructor = constructor
        self.grid = grid
        self.laps = laps
        self.status = status
        self.time = time
        self.fastest_lap = fastest_lap
        self.qual_1 = qual_1
        self.qual_2 = qual_2
        self.qual_3 = qual_3

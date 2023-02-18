""" Result class """

import datetime
from dataclasses import dataclass

from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver
from ergast_py.models.fastest_lap import FastestLap
from ergast_py.models.base_model import BaseModel


@dataclass
class Result(BaseModel):
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

""" DriverStanding class """
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel
from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver


@dataclass
class DriverStanding(BaseModel):
    """
    Representation of a Formula One Driver's standing in a Season

    Driver Standings may contain:
        position: Integer
        position_text: String
        points: Float
        wins: Integer
        driver: Driver
        constructors: Constructor[]
    """

    position: int
    position_text: str
    points: float
    wins: int
    driver: Driver
    constructors: list[Constructor]

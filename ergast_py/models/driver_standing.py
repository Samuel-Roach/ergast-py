""" DriverStanding class """

from dataclasses import dataclass

from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver


@dataclass
class DriverStanding():
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

    def __init__(self, position: int, position_text: str, points: float, wins: int, driver: Driver, #pylint: disable=too-many-arguments
                 constructors: list[Constructor]) -> None:
        self.position = position
        self.position_text = position_text
        self.points = points
        self.wins = wins
        self.driver = driver
        self.constructors = constructors

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

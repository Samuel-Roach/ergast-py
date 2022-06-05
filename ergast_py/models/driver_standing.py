from dataclasses import dataclass
from ergast_py.models.constructor import Constructor

from ergast_py.models.driver import Driver

@dataclass
class DriverStanding:
    """
    Representation of a Formula One Driver's standing in a Season
    Driver Standings may contain:
        position: Integer
        positionText: String
        points: Float
        wins: Integer
        driver: Driver
        constructors: Constructor[]
    """

    def __init__(self, position: int, positionText: str, points: float, wins: int, driver: Driver,
                 constructors: list[Constructor]) -> None:
        self.position = position
        self.positionText = positionText
        self.points = points
        self.wins = wins
        self.driver = driver
        self.constructors = constructors
        pass

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
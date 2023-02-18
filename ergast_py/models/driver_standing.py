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

    position: int
    position_text: str
    points: float
    wins: int
    driver: Driver
    constructors: list[Constructor]

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, DriverStanding) and (
            self.position == __o.position and
            self.position_text == __o.position_text and
            self.points == __o.points and
            self.wins == __o.wins and
            self.driver == __o.driver and
            self.constructors == __o.constructors
        )

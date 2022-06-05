from dataclasses import dataclass

from ergast_py.models.constructor import Constructor

@dataclass
class ConstructorStanding:
    """
    Representation of a Formula One Constructor's standing in a Season
    Constructor Standings may contain:
        position: Integer
        positionText: String
        points: Float
        wins: Integer
        constructor: Constructor
    """

    def __init__(self, position: int, positionText: str, points: float, wins: int, constructor: Constructor) -> None:
        self.position = position
        self.positionText = positionText
        self.points = points
        self.wins = wins
        self.constructor = constructor
        pass

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
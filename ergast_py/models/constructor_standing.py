""" ConstructorStanding class """

from dataclasses import dataclass

from ergast_py.models.constructor import Constructor
from ergast_py.models.model import Model


@dataclass
class ConstructorStanding(Model):
    """
    Representation of a Formula One Constructor's standing in a Season

    Constructor Standings may contain:
        position: Integer
        position_text: String
        points: Float
        wins: Integer
        constructor: Constructor
    """

    def __init__(self, position: int, position_text: str, points: float, wins: int, #pylint: disable=too-many-arguments
                 constructor: Constructor) -> None:
        self.position = position
        self.position_text = position_text
        self.points = points
        self.wins = wins
        self.constructor = constructor

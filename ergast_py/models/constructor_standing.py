""" ConstructorStanding class """

from dataclasses import dataclass

from ergast_py.models.constructor import Constructor
from ergast_py.models.base_model import BaseModel


@dataclass
class ConstructorStanding(BaseModel):
    """
    Representation of a Formula One Constructor's standing in a Season

    Constructor Standings may contain:
        position: Integer
        position_text: String
        points: Float
        wins: Integer
        constructor: Constructor
    """

    position: int
    position_text: str
    points: float
    wins: int
    constructor: Constructor

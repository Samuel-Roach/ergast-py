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

    def __str__(self):
        return f"ConstructorStanding(position={self.position}, positionText={self.positionText}, points={self.points}, wins={self.wins}, constructor={self.constructor})"

    def __repr__(self):
        return f"ConstructorStanding(position={self.position}, positionText={self.positionText}, points={self.points}, wins={self.wins}, constructor={self.constructor})"
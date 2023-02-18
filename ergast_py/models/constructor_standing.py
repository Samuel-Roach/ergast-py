""" ConstructorStanding class """

from dataclasses import dataclass

from ergast_py.models.constructor import Constructor


@dataclass
class ConstructorStanding():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ConstructorStanding) and (
            self.position == __o.position and
            self.position_text == __o.position_text and
            self.points == __o.points and
            self.wins == __o.wins and
            self.constructor == __o.constructor
        )

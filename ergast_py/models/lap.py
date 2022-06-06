""" Lap class """

from dataclasses import dataclass

from ergast_py.models.timing import Timing


@dataclass
class Lap():
    """
    Representation of a single Lap from a Formula One race

    Laps may contain:
        number: Integer
        timings: Timing[]
    """

    def __init__(self, number: int, timings: list[Timing]) -> None:
        self.number = number
        self.timings = timings

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

""" Lap class """

from dataclasses import dataclass

from ergast_py.models.model import Model
from ergast_py.models.timing import Timing


@dataclass
class Lap(Model):
    """
    Representation of a single Lap from a Formula One race

    Laps may contain:
        number: Integer
        timings: Timing[]
    """

    def __init__(self, number: int, timings: list[Timing]) -> None:
        self.number = number
        self.timings = timings

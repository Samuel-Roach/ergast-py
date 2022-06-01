from dataclasses import dataclass

from ergast_py.models.timing import Timing

@dataclass
class Lap:
    """
    Representation of a single Lap from a Formula One race
    Laps may contain:
        number: Integer
        timings: Timing[]
    """

    def __init__(self, number: int, timings: list[Timing]) -> None:
        self.number = number
        self.timings = timings
        pass

    def __str__(self):
        return f"Lap(number={self.number}, timings={self.timings})"

    def __repr__(self):
        return f"Lap(number={self.number}, timings={self.timings})"
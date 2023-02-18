""" Lap class """

from dataclasses import dataclass

from ergast_py.models.timing import Timing
from ergast_py.models.base_model import BaseModel


@dataclass
class Lap(BaseModel):
    """
    Representation of a single Lap from a Formula One race

    Laps may contain:
        number: Integer
        timings: Timing[]
    """

    number: int
    timings: list[Timing]

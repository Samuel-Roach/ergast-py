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

    number: int
    timings: list[Timing]

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Lap) and (
            self.number == __o.number and
            self.timings == __o.timings
        )

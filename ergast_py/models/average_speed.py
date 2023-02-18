""" AverageSpeed class """

from dataclasses import dataclass


@dataclass
class AverageSpeed():
    """
    Representation of a Drivers Average Speed

    Average Speeds may contain:
        units: String
        speed: Float
    """

    units: str
    speed: float

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AverageSpeed) and (
            self.units == __o.units and
            self.speed == __o.speed
        )

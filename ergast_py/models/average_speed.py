""" AverageSpeed class """

from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class AverageSpeed(Model):
    """
    Representation of a Drivers Average Speed

    Average Speeds may contain:
        units: String
        speed: Float
    """

    def __init__(self, units: str, speed: float) -> None:
        self.units = units
        self.speed = speed

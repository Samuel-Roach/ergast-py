""" AverageSpeed class """
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class AverageSpeed(BaseModel):
    """
    Representation of a Drivers Average Speed

    Average Speeds may contain:
        units: String
        speed: Float
    """

    units: str
    speed: float

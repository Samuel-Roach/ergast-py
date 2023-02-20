""" Season class """
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class Season(BaseModel):
    """
    Representation of a single Season in Formula One

    Seasons may contain:
        season: Integer
        url: String
    """

    season: int
    url: str

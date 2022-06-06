""" Season class """

from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class Season(Model):
    """
    Representation of a single Season in Formula One

    Seasons may contain:
        season: Integer
        url: String
    """

    def __init__(self, season: int, url: str) -> None:
        self.season = season
        self.url = url

""" Constructor class """

from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class Constructor(Model):
    """
    Representation of a Formula One Team

    Constructors may contain:
        constructor_id: String
        url: String
        name: String
        nationality: String
    """

    def __init__(self, constructor_id: str, url: str, name: str, nationality: str) -> None:
        self.constructor_id = constructor_id
        self.url = url
        self.name = name
        self.nationality = nationality

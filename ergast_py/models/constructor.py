""" Constructor class """

from dataclasses import dataclass


@dataclass
class Constructor():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

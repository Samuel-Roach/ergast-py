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

    constructor_id: str
    url: str
    name: str
    nationality: str

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Constructor) and (
            self.constructor_id == __o.constructor_id and
            self.url == __o.url and
            self.name == __o.name and
            self.nationality == __o.nationality
        )

from dataclasses import dataclass
from ergast_py.models.location import Location

@dataclass
class Circuit:
    """
    Representation of a Formula One Circuit
    Circuits may contain:
        circuitId: String
        url: String
        circuitName: String
        location: Location
    """

    def __init__(self, circuitId: str, url: str, circuitName: str, location: Location) -> None:
        self.circuitId = circuitId
        self.url = url
        self.circuitName = circuitName
        self.location = location
        pass

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
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

    def __str__(self):
        return f"Circuit(circuitId={self.circuitId}, url={self.url}, circuitName={self.circuitName}, location={self.location})"

    def __repr__(self):
        return f"Circuit(circuitId={self.circuitId}, url={self.url}, circuitName={self.circuitName}, location={self.location})"
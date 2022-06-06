""" Circuit class """

from dataclasses import dataclass

from ergast_py.models.location import Location
from ergast_py.models.model import Model


@dataclass
class Circuit(Model):
    """
    Representation of a Formula One Circuit

    Circuits may contain:
        circuit_id: String
        url: String
        circuit_name: String
        location: Location
    """

    def __init__(self, circuit_id: str, url: str, circuit_name: str, location: Location) -> None:
        self.circuit_id = circuit_id
        self.url = url
        self.circuit_name = circuit_name
        self.location = location

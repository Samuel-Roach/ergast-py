""" Circuit class """
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel
from ergast_py.models.location import Location


@dataclass
class Circuit(BaseModel):
    """
    Representation of a Formula One Circuit

    Circuits may contain:
        circuit_id: String
        url: String
        circuit_name: String
        location: Location
    """

    circuit_id: str
    url: str
    circuit_name: str
    location: Location

""" Location class """

from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class Location(BaseModel):
    """
    Representation of a Location for a Formula One Circuit

    Locations may contain:
        lat: Float
        long: Float
        locality: String
        country: String
    """

    latitude: float
    longitude: float
    locality: str
    country: str

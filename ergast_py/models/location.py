""" Location class """

from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class Location(Model):
    """
    Representation of a Location for a Formula One Circuit

    Locations may contain:
        lat: Float
        long: Float
        locality: String
        country: String
    """

    def __init__(self, latitude: float, longitude: float, locality: str, country: str) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.locality = locality
        self.country = country

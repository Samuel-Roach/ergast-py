""" Location class """

from dataclasses import dataclass


@dataclass
class Location():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

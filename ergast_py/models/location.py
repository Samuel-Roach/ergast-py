from dataclasses import dataclass

@dataclass
class Location:
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
        pass

    def __str__(self):
        return f"Location(latitude={self.latitude},longitude={self.longitude}, locality={self.locality}, country={self.country})"

    def __repr__(self):
        return f"Location(latitude={self.latitude},longitude={self.longitude}, locality={self.locality}, country={self.country})"
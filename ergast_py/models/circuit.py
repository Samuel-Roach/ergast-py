""" Circuit class """

from dataclasses import dataclass

from ergast_py.models.location import Location


@dataclass
class Circuit():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Circuit) and (
            self.circuit_id == __o.circuit_id and
            self.url == __o.url and
            self.circuit_name == __o.circuit_name and
            self.location == __o.location
        )

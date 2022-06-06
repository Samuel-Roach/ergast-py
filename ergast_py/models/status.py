""" Status class """

from dataclasses import dataclass


@dataclass
class Status():
    """
    Representation of the finishing status of a Driver in a Race

    Statuses may contain:
        status_id: Integer
        count: Integer
        status: String
    """

    def __init__(self, status_id: int, count: int, status: str) -> None:
        self.status_id = status_id
        self.count = count
        self.status = status

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

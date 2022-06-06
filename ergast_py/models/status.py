""" Status class """

from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class Status(Model):
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

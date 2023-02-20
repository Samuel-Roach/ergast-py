""" Status class """
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class Status(BaseModel):
    """
    Representation of the finishing status of a Driver in a Race

    Statuses may contain:
        status_id: Integer
        count: Integer
        status: String
    """

    status_id: int
    count: int
    status: str

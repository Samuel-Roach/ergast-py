""" Driver class """
import datetime
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class Driver(BaseModel):
    """
    Representation of a Formula One driver

    Drivers may contain:
        driver_id: String
        permanent_number: Integer
        code: String
        url: String
        given_name: String
        family_name: String
        date_of_birth: datetime.date
        nationality: String
    """

    driver_id: str
    code: str
    url: str
    given_name: str
    family_name: str
    date_of_birth: datetime.date
    nationality: str
    permanent_number: int

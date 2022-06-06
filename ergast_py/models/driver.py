""" Driver class """

import datetime
from dataclasses import dataclass

from ergast_py.models.model import Model


@dataclass
class Driver(Model):
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

    def __init__(self, driver_id: str, code: str, url: str, given_name: str, family_name: str,
                 date_of_birth: datetime.date, nationality: str, permanent_number: int) -> None:
        self.driver_id = driver_id
        self.permanent_number = permanent_number
        self.code = code
        self.url = url
        self.given_name = given_name
        self.family_name = family_name
        self.date_of_birth = date_of_birth
        self.nationality = nationality

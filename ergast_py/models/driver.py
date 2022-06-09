""" Driver class """

import datetime
from dataclasses import dataclass


@dataclass
class Driver():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Driver) and (
            self.driver_id == __o.driver_id and
            self.permanent_number == __o.permanent_number and
            self.code == __o.code and
            self.url == __o.url and
            self.given_name == __o.given_name and
            self.family_name == __o.family_name and
            self.date_of_birth == __o.date_of_birth and
            self.nationality == __o.nationality
        )

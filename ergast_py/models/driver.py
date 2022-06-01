from dataclasses import dataclass
from ergast_py.helpers import Helpers
import datetime

@dataclass
class Driver:
    """
    Representation of a Formula One driver
    Drivers may contain:
        driverId: String
        permanentNumber: Integer
        code: String
        url: String
        givenName: String
        familyName: String
        dateOfBirth: datetime.date
        nationality: String
    """

    def __init__(self, driverId: str, code: str, url: str, givenName: str, familyName: str, dateOfBirth: datetime.date,
                 nationality: str, permanentNumber: int) -> None:
        self.driverId = driverId
        self.permanentNumber = permanentNumber
        self.code = code
        self.url = url
        self.givenName = givenName
        self.familyName = familyName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality
        pass

    def __str__(self):
        return f"Driver(driverId={self.driverId}, permanentNumber={self.permanentNumber}, code={self.code}, url={self.url}, givenName={self.givenName}, familyName={self.familyName}, dateOfBirth={self.dateOfBirth}, nationality={self.nationality})"

    def __repr__(self):
        return f"Driver(driverId={self.driverId}, permanentNumber={self.permanentNumber}, code={self.code}, url={self.url}, givenName={self.givenName}, familyName={self.familyName}, dateOfBirth={self.dateOfBirth}, nationality={self.nationality})"
 
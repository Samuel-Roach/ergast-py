""" StandingsList class """

from dataclasses import dataclass

from ergast_py.models.constructor_standing import ConstructorStanding
from ergast_py.models.driver_standing import DriverStanding
from ergast_py.models.model import Model


@dataclass
class StandingsList(Model):
    """
    Representation of a set of Standings from a time in Formula One

    StandingsLists may contain:
        season: Integer
        round_no: Integer
        driver_standings: DriverStanding[]
        constructor_standings: ConstructorStanding[]
    """

    def __init__(self, season: int, round_no: int, driver_standings: list[DriverStanding],
                 constructor_standings: list[ConstructorStanding]) -> None:
        self.season = season
        self.round_no = round_no
        self.driver_standings = driver_standings
        self.constructor_standings = constructor_standings

""" StandingsList class """
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel
from ergast_py.models.constructor_standing import ConstructorStanding
from ergast_py.models.driver_standing import DriverStanding


@dataclass
class StandingsList(BaseModel):
    """
    Representation of a set of Standings from a time in Formula One

    StandingsLists may contain:
        season: Integer
        round_no: Integer
        driver_standings: DriverStanding[]
        constructor_standings: ConstructorStanding[]
    """

    season: int
    round_no: int
    driver_standings: list[DriverStanding]
    constructor_standings: list[ConstructorStanding]

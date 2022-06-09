""" StandingsList class """

from dataclasses import dataclass

from ergast_py.models.constructor_standing import ConstructorStanding
from ergast_py.models.driver_standing import DriverStanding


@dataclass
class StandingsList():
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

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, StandingsList) and (
            self.season == __o.season and
            self.round_no == __o.round_no and
            self.driver_standings == __o.driver_standings and
            self.constructor_standings == __o.constructor_standings
        )

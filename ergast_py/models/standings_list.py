from dataclasses import dataclass
from ergast_py.models.driver_standing import DriverStanding
from ergast_py.models.constructor_standing import ConstructorStanding

@dataclass
class StandingsList:
    """
    Representation of a set of Standings from a time in Formula One
    StandingsLists may contain:
        season: Integer
        round: Integer
        driverStandings: DriverStanding[]
        constructorStandings: ConstructorStanding[]
    """

    def __init__(self, season: int, round: int, driverStandings: list[DriverStanding],
                 constructorStandings: list[ConstructorStanding]) -> None:
        self.season = season
        self.round = round
        self.driverStandings = driverStandings
        self.constructorStandings = constructorStandings
        pass

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
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

    def __str__(self):
        return f"StandingsList(season={self.season}, round={self.round}, driverStandings={self.driverStandings}, constructorStandings={self.constructorStandings})"

    def __repr__(self):
        return f"StandingsList(season={self.season}, round={self.round}, driverStandings={self.driverStandings}, constructorStandings={self.constructorStandings})"
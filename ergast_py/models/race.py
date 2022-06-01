from dataclasses import dataclass
import datetime

from ergast_py.helpers import Helpers
from ergast_py.models.circuit import Circuit
from ergast_py.models.lap import Lap
from ergast_py.models.result import Result
from ergast_py.models.pit_stop import PitStop

@dataclass
class Race:
    """
    Representation of a single Race from a Formula One season
    Races may contain:
        season: Integer
        round: Integer
        url: String
        raceName: String
        circuit: Circuit
        date: datetime.datetime
        results: Result[]
        firstPractice: datetime.datetime
        secondPractice: datetime.datetime
        thirdPractice: datetime.datetime
        sprint: datetime.datetime
        sprintResults: Result[]
        qualifying: datetime.datetime
        qualifyingResults: Result[]
        pitStops: PitStop[]
        laps: Lap[]
    """

    def __init__(self, season: int, round: int, url: str, raceName: str, circuit: Circuit, date: datetime.datetime,
                 results: list[Result], firstPractice: datetime.datetime, secondPractice: datetime.datetime,
                 thirdPractice: datetime.datetime, sprint: datetime.datetime, sprintResults: list[Result],
                 qualifying: datetime.datetime, qualifyingResults: list[Result], pitStops: list[PitStop],
                 laps: list[Lap]) -> None:
        self.season = season
        self.round = round
        self.url = url
        self.raceName = raceName
        self.circuit = circuit
        self.date = date
        self.results = results
        self.firstPractice = firstPractice
        self.secondPractice = secondPractice
        self.thirdPractice = thirdPractice
        self.sprint = sprint
        self.sprintResults = sprintResults
        self.qualifying = qualifying
        self.qualifyingResults = qualifyingResults
        self.pitStops = pitStops
        self.laps = laps
        pass

    def __str__(self):
        return f"Race(season={self.season}, round={self.round}, url={self.url}, raceName={self.raceName}, circuit={self.circuit}, date={self.date}, results={self.results}, firstPractice={self.firstPractice}, secondPractice={self.secondPractice}, thirdPractice={self.thirdPractice}, sprint={self.sprint}, sprintResults={self.sprintResults}, qualifying={self.qualifying}, qualifyingResults={self.qualifyingResults}, pitStops={self.pitStops}, laps={self.laps})"

    def __repr__(self):
        return f"Race(season={self.season}, round={self.round}, url={self.url}, raceName={self.raceName}, circuit={self.circuit}, date={self.date}, results={self.results}, firstPractice={self.firstPractice}, secondPractice={self.secondPractice}, thirdPractice={self.thirdPractice}, sprint={self.sprint}, sprintResults={self.sprintResults}, qualifying={self.qualifying}, qualifyingResults={self.qualifyingResults}, pitStops={self.pitStops}, laps={self.laps})"


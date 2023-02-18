""" Race class """

import datetime
from dataclasses import dataclass

from ergast_py.models.circuit import Circuit
from ergast_py.models.lap import Lap
from ergast_py.models.pit_stop import PitStop
from ergast_py.models.result import Result


@dataclass
class Race():
    """
    Representation of a single Race from a Formula One season

    Races may contain:
        season: Integer
        round_no: Integer
        url: String
        race_name: String
        circuit: Circuit
        date: datetime.datetime
        results: Result[]
        first_practice: datetime.datetime
        second_practice: datetime.datetime
        third_practice: datetime.datetime
        sprint: datetime.datetime
        sprint_results: Result[]
        qualifying: datetime.datetime
        qualifying_results: Result[]
        pit_stops: PitStop[]
        laps: Lap[]
    """

    season: int
    round_no: int
    url: str
    race_name: str
    circuit: Circuit
    date: datetime.datetime
    results: list[Result]
    first_practice: datetime.datetime
    second_practice: datetime.datetime
    third_practice: datetime.datetime
    sprint: datetime.datetime
    sprint_results: list[Result]
    qualifying: datetime.datetime
    qualifying_results: list[Result]
    pit_stops: list[PitStop]
    laps: list[Lap]

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Race) and (
            self.season == __o.season and
            self.round_no == __o.round_no and
            self.url == __o.url and
            self.race_name == __o.race_name and
            self.circuit == __o.circuit and
            self.date == __o.date and
            self.results == __o.results and
            self.first_practice == __o.first_practice and
            self.second_practice == __o.second_practice and
            self.third_practice == __o.third_practice and
            self.sprint == __o.sprint and
            self.sprint_results == __o.sprint_results and
            self.qualifying == __o.qualifying and
            self.qualifying_results == __o.qualifying_results and
            self.pit_stops == __o.pit_stops and
            self.laps == __o.laps
        )

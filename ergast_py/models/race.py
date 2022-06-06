""" Race class """

import datetime
from dataclasses import dataclass

from ergast_py.models.circuit import Circuit
from ergast_py.models.lap import Lap
from ergast_py.models.model import Model
from ergast_py.models.pit_stop import PitStop
from ergast_py.models.result import Result


@dataclass
class Race(Model):
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

    def __init__(self, season: int, round_no: int, url: str, race_name: str, circuit: Circuit,
                 date: datetime.datetime, results: list[Result], first_practice: datetime.datetime,
                 second_practice: datetime.datetime, third_practice: datetime.datetime,
                 sprint: datetime.datetime, sprint_results: list[Result],
                 qualifying: datetime.datetime, qualifying_results: list[Result],
                 pit_stops: list[PitStop], laps: list[Lap]) -> None:
        self.season = season
        self.round_no = round_no
        self.url = url
        self.race_name = race_name
        self.circuit = circuit
        self.date = date
        self.results = results
        self.first_practice = first_practice
        self.second_practice = second_practice
        self.third_practice = third_practice
        self.sprint = sprint
        self.sprint_results = sprint_results
        self.qualifying = qualifying
        self.qualifying_results = qualifying_results
        self.pit_stops = pit_stops
        self.laps = laps

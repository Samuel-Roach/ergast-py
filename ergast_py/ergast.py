from __future__ import annotations

from ergast_py.models.driver import Driver
from ergast_py.models.circuit import Circuit
from ergast_py.models.constructor import Constructor
from ergast_py.models.standings_list import StandingsList
from ergast_py.models.status import Status
from ergast_py.constants.status_type import StatusType
from ergast_py.models.season import Season
from ergast_py.models.race import Race
from ergast_py.models.lap import Lap
from ergast_py.models.pit_stop import PitStop

from ergast_py.requester import Requester
from ergast_py.type_constructor import TypeConstructor

class Ergast():
    """
    Class for querying the Ergast API
    """

    def __init__(self) -> None:
        self.reset()
        self.requester = Requester()
        self.type_constructor = TypeConstructor()


    def reset(self) -> None:
        self.params = {
            "season": None,
            "seasons": None,
            "round": None,
            "driver": None,
            "constructor": None,
            "grid": None,
            "qualifying": None,
            "sprint": None,
            "result": None,
            "fastest": None,
            "circuit": None,
            "status": None,
            "standing": None,
            "races": None,
            "limit": None,
            "offset": None,
            "lap": None,
            "pit_stop": None,
        }

    #
    #   FILTER FUNCTIONS
    #

    def season(self, year: int="current") -> Ergast:
        self.params["season"] = year
        return self

    def round(self, round: int="last") -> Ergast:
        self.params["round"] = round
        return self

    def driver(self, driver: Driver) -> Ergast:
        self.params["driver"] = driver.driverId
        return self

    def driver_str(self, driver: str) -> Ergast:
        self.params["driver"] = driver
        return self

    def constructor(self, constructor: Constructor) -> Ergast:
        self.params["constructor"] = constructor.constructorId
        return self

    def constructor_str(self, constructor: str) -> Ergast:
        self.params["constructor"] = constructor
        return self

    def qualifying(self, position: int) -> Ergast:
        self.params["qualifying"] = position
        return self

    def sprint(self, position: int) -> Ergast:
        self.params["sprint"] = position
        return self

    def grid(self, position: int) -> Ergast:
        self.params["grid"] = position
        return self

    def result(self, position: int) -> Ergast:
        self.params["result"] = position
        return self

    def fastest(self, position: int) -> Ergast:
        self.params["fastest"] = position
        return self

    def circuit(self, circuit: Circuit) -> Ergast:
        self.params["circuit"] = circuit.circuitId
        return self

    def circuit_str(self, circuit: str) -> Ergast:
        self.params["circuit"] = circuit
        return self

    def status(self, status: int) -> Ergast:
        self.params["status"] = status
        return self

    def status_str(self, status: str) -> Ergast:
        self.params["status"] = StatusType().status_map[status]
        return self

    def standing(self, position: int) -> Ergast:
        self.params["standing"] = position
        return self

    def lap(self, lap_number: int) -> Ergast:
        self.params["lap"] = lap_number
        return self

    def pit_stop(self, stop_number: int) -> Ergast:
        self.params["pit_stop"] = stop_number
        return self

    #
    #   PAGING FUNCTIONS
    #

    def limit(self, amount: int) -> Ergast:
        self.params["limit"] = amount
        return self

    def offset(self, amount: int) -> Ergast:
        self.params["offset"] = amount
        return self

    #
    #   RETURN FUNCTIONS
    #

    #   Race and Results Queries

    def get_circuits(self) -> list[Circuit]:
        circuits_json = self.requester.get_circuits(self.params)
        circuits = self.type_constructor.construct_circuits(circuits_json)
        self.reset()
        return circuits

    def get_circuit(self) -> Circuit:
        circuits_json = self.requester.get_circuits(self.params)
        circuits = self.type_constructor.construct_circuits(circuits_json)
        self.reset()
        return circuits[0]

    def get_constructors(self) -> list[Constructor]:
        constructors_json = self.requester.get_constructors(self.params)
        constructors = self.type_constructor.construct_constructors(constructors_json)
        self.reset()
        return constructors

    def get_constructor(self) -> Constructor:
        constructors_json = self.requester.get_constructors(self.params)
        constructors = self.type_constructor.construct_constructors(constructors_json)
        self.reset()
        return constructors[0]

    def get_drivers(self) -> list[Driver]:
        drivers_json = self.requester.get_drivers(self.params)
        drivers = self.type_constructor.construct_drivers(drivers_json)
        self.reset()
        return drivers

    def get_driver(self) -> Driver:
        drivers_json = self.requester.get_drivers(self.params)
        drivers = self.type_constructor.construct_drivers(drivers_json)
        self.reset()
        return drivers[0]

    def get_qualifyings(self) -> list[Race]:
        qualify_json = self.requester.get_qualifying(self.params)
        qualifying = self.type_constructor.construct_races(qualify_json)
        self.reset()
        return qualifying

    def get_qualifying(self) -> Race:
        qualify_json = self.requester.get_qualifying(self.params)
        qualifying = self.type_constructor.construct_races(qualify_json)
        self.reset()
        return qualifying[0]

    def get_sprints(self) -> list[Race]:
        sprint_json = self.requester.get_sprints(self.params)
        sprint = self.type_constructor.construct_races(sprint_json)
        self.reset()
        return sprint

    def get_sprint(self) -> Race:
        sprint_json = self.requester.get_sprints(self.params)
        sprint = self.type_constructor.construct_races(sprint_json)
        self.reset()
        return sprint[0]

    def get_results(self) -> list[Race]:
        results_json = self.requester.get_results(self.params)
        results = self.type_constructor.construct_races(results_json)
        self.reset()
        return results

    def get_result(self) -> Race:
        results_json = self.requester.get_results(self.params)
        results = self.type_constructor.construct_races(results_json)
        self.reset()
        return results[0]

    def get_races(self) -> list[Race]:
        races_json = self.requester.get_races(self.params)
        races = self.type_constructor.construct_races(races_json)
        self.reset()
        return races

    def get_race(self) -> Race:
        races_json = self.requester.get_races(self.params)
        races = self.type_constructor.construct_races(races_json)
        self.reset()
        return races[0]

    def get_seasons(self) -> list[Season]:
        seasons_json = self.requester.get_seasons(self.params)
        seasons = self.type_constructor.construct_seasons(seasons_json)
        self.reset()
        return seasons

    def get_season(self) -> Season:
        seasons_json = self.requester.get_seasons(self.params)
        seasons = self.type_constructor.construct_seasons(seasons_json)
        self.reset()
        return seasons[0]

    def get_statuses(self) -> list[Status]:
        statuses_json = self.requester.get_statuses(self.params)
        statuses = self.type_constructor.construct_statuses(statuses_json)
        self.reset()
        return statuses

    def get_status(self) -> Status:
        statuses_json = self.requester.get_statuses(self.params)
        statuses = self.type_constructor.construct_statuses(statuses_json)
        self.reset()
        return statuses[0]

    #   Standings Queries

    def get_driver_standings(self) -> list[StandingsList]:
        standings_lists_json = self.requester.get_driver_standings(self.params)
        standings_lists = self.type_constructor.construct_standings_lists(standings_lists_json)
        self.reset()
        return standings_lists

    def get_driver_standing(self) -> StandingsList:
        standings_lists_json = self.requester.get_driver_standings(self.params)
        standings_lists = self.type_constructor.construct_standings_lists(standings_lists_json)
        self.reset()
        return standings_lists[0]

    def get_constructor_standings(self) -> list[StandingsList]:
        standings_lists_json = self.requester.get_constructor_standings(self.params)
        standings_lists = self.type_constructor.construct_standings_lists(standings_lists_json)
        self.reset()
        return standings_lists

    def get_constructor_standing(self) -> StandingsList:
        standings_lists_json = self.requester.get_constructor_standings(self.params)
        standings_lists = self.type_constructor.construct_standings_lists(standings_lists_json)
        self.reset()
        return standings_lists[0]

    #   Laps and Pit Stops Queries

    def get_laps(self) -> list[Race]:
        laps_json = self.requester.get_laps(self.params)
        laps = self.type_constructor.construct_races(laps_json)
        self.reset()
        return laps

    def get_lap(self) -> Race:
        laps_json = self.requester.get_laps(self.params)
        laps = self.type_constructor.construct_races(laps_json)
        self.reset()
        return laps[0]

    def get_pit_stops(self) -> list[Race]:
        pit_stops_json = self.requester.get_pit_stops(self.params)
        pit_stops = self.type_constructor.construct_races(pit_stops_json)
        self.reset()
        return pit_stops

    def get_pit_stop(self) -> Race:
        pit_stops_json = self.requester.get_pit_stops(self.params)
        pit_stops = self.type_constructor.construct_races(pit_stops_json)
        self.reset()
        return pit_stops[0]
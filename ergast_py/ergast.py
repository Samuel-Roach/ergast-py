from __future__ import annotations

from typing import Callable

from ergast_py.constants.status_type import StatusType
from ergast_py.models.circuit import Circuit
from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver
from ergast_py.models.race import Race
from ergast_py.models.season import Season
from ergast_py.models.standings_list import StandingsList
from ergast_py.models.status import Status
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

    def round(self, round_no: int="last") -> Ergast:
        self.params["round"] = round_no
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

    #   Lambda queries

    def _get_items(self, get_items: Callable, construct_items: Callable):
        items_json = get_items(self.params)
        items = construct_items(items_json)
        self.reset()
        return items

    def _get_item(self, get_items: Callable, construct_items: Callable):
        items = self._get_items(get_items, construct_items)
        if len(items) == 1:
            return items[0]
        raise Warning("More than 1 element found")

    #   Race and Results Queries

    def get_circuits(self) -> list[Circuit]:
        return self._get_items(self.requester.get_circuits, self.type_constructor.construct_circuits)

    def get_circuit(self) -> Circuit:
        return self._get_item(self.requester.get_circuits, self.type_constructor.construct_circuits)

    def get_constructors(self) -> list[Constructor]:
        constructors_json = self.requester.get_constructors(self.params)
        constructors = self.type_constructor.construct_constructors(constructors_json)
        self.reset()
        return constructors

    def get_constructor(self) -> Constructor:
        constructors_json = self.requester.get_constructors(self.params)
        constructors = self.type_constructor.construct_constructors(constructors_json)
        self.reset()
        if len(constructors) == 1:
            return constructors[0]
        else:
            raise Exception("More than 1 item found")

    def get_drivers(self) -> list[Driver]:
        drivers_json = self.requester.get_drivers(self.params)
        drivers = self.type_constructor.construct_drivers(drivers_json)
        self.reset()
        return drivers

    def get_driver(self) -> Driver:
        drivers_json = self.requester.get_drivers(self.params)
        drivers = self.type_constructor.construct_drivers(drivers_json)
        self.reset()
        if len(drivers) == 1:
            return drivers[0]
        else:
            raise Exception("More than 1 item found")

    def get_qualifyings(self) -> list[Race]:
        qualify_json = self.requester.get_qualifying(self.params)
        qualifying = self.type_constructor.construct_races(qualify_json)
        self.reset()
        return qualifying

    def get_qualifying(self) -> Race:
        qualify_json = self.requester.get_qualifying(self.params)
        qualifying = self.type_constructor.construct_races(qualify_json)
        self.reset()
        if len(qualifying) == 1:
            return qualifying[0]
        else:
            raise Exception("More than 1 item found")

    def get_sprints(self) -> list[Race]:
        sprint_json = self.requester.get_sprints(self.params)
        sprint = self.type_constructor.construct_races(sprint_json)
        self.reset()
        return sprint

    def get_sprint(self) -> Race:
        sprint_json = self.requester.get_sprints(self.params)
        sprint = self.type_constructor.construct_races(sprint_json)
        self.reset()
        if len(sprint) == 1:
            return sprint[0]
        else:
            raise Exception("More than 1 item found")

    def get_results(self) -> list[Race]:
        results_json = self.requester.get_results(self.params)
        results = self.type_constructor.construct_races(results_json)
        self.reset()
        return results

    def get_result(self) -> Race:
        results_json = self.requester.get_results(self.params)
        results = self.type_constructor.construct_races(results_json)
        self.reset()
        if len(results) == 1:
            return results[0]
        else:
            raise Exception("More than 1 item found")

    def get_races(self) -> list[Race]:
        races_json = self.requester.get_races(self.params)
        races = self.type_constructor.construct_races(races_json)
        self.reset()
        return races

    def get_race(self) -> Race:
        races_json = self.requester.get_races(self.params)
        races = self.type_constructor.construct_races(races_json)
        self.reset()
        if len(races) == 1:
            return races[0]
        else:
            raise Exception("More than 1 item found")

    def get_seasons(self) -> list[Season]:
        seasons_json = self.requester.get_seasons(self.params)
        seasons = self.type_constructor.construct_seasons(seasons_json)
        self.reset()
        return seasons

    def get_season(self) -> Season:
        seasons_json = self.requester.get_seasons(self.params)
        seasons = self.type_constructor.construct_seasons(seasons_json)
        self.reset()
        if len(seasons) == 1:
            return seasons[0]
        else:
            raise Exception("More than 1 item found")

    def get_statuses(self) -> list[Status]:
        statuses_json = self.requester.get_statuses(self.params)
        statuses = self.type_constructor.construct_statuses(statuses_json)
        self.reset()
        return statuses

    def get_status(self) -> Status:
        statuses_json = self.requester.get_statuses(self.params)
        statuses = self.type_constructor.construct_statuses(statuses_json)
        self.reset()
        if len(statuses) == 1:
            return statuses[0]
        else:
            raise Exception("More than 1 item found")

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
        if len(standings_lists) == 1:
            return standings_lists[0]
        else:
            raise Exception("More than 1 item found")

    def get_constructor_standings(self) -> list[StandingsList]:
        standings_lists_json = self.requester.get_constructor_standings(self.params)
        standings_lists = self.type_constructor.construct_standings_lists(standings_lists_json)
        self.reset()
        return standings_lists

    def get_constructor_standing(self) -> StandingsList:
        standings_lists_json = self.requester.get_constructor_standings(self.params)
        standings_lists = self.type_constructor.construct_standings_lists(standings_lists_json)
        self.reset()
        if len(standings_lists) == 1:
            return standings_lists[0]
        else:
            raise Exception("More than 1 item found")

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
        if len(laps) == 1:
            return laps[0]
        else:
            raise Exception("More than 1 item found")

    def get_pit_stops(self) -> list[Race]:
        pit_stops_json = self.requester.get_pit_stops(self.params)
        pit_stops = self.type_constructor.construct_races(pit_stops_json)
        self.reset()
        return pit_stops

    def get_pit_stop(self) -> Race:
        pit_stops_json = self.requester.get_pit_stops(self.params)
        pit_stops = self.type_constructor.construct_races(pit_stops_json)
        self.reset()
        if len(pit_stops) == 1:
            return pit_stops[0]
        else:
            raise Exception("More than 1 item found")

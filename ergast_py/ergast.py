""" Ergast class """
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


# pylint: disable=too-many-public-methods
class Ergast:
    """
    Ergast
    ~~~~~~
    Class for querying the Ergast API.

    Build up the queries using the available functions.

    >>> e = ergast_py.Ergast()
    >>> e.season(2021).round(1).driver("alonso")

    Get the data using ``.get_xyz()`` functions.

    >>> print(e.get_result())
    """

    def __init__(self) -> None:
        self.params = {}
        self.reset()
        self.requester = Requester()
        self.type_constructor = TypeConstructor()

    def reset(self) -> None:
        """
        Reset the Ergast query building.

        Should be called after a query is run to prevent forward interraction.
        """
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

    def season(self, year: int = "current") -> Ergast:
        """
        Add a season to the current query

        >>> e.season(2022).get_races()
        """
        self.params["season"] = year
        return self

    def round(self, round_no: int = "last") -> Ergast:
        """
        Add a round to the current query

        >>> e.season(1999).round(3).get_circuit()
        """
        self.params["round"] = round_no
        return self

    def driver(self, driver) -> Ergast:
        """
        Add a driver to the current query

        >>> alonso = e.driver("alonso").get_driver()
        >>> e.driver(alonso).get_results()
        """
        if isinstance(driver, str):
            self.params["driver"] = driver
        elif isinstance(driver, Driver):
            self.params["driver"] = driver.driver_id
        else:
            raise TypeError("Function parameter must be of type Driver or str")
        return self

    def constructor(self, constructor: Constructor) -> Ergast:
        """
        Add a constructor to the current query

        >>> mercedes = e.constructor("mercedes").get_constructor()
        >>> e.constructor(mercedes).get_constructor_standings()
        """
        if isinstance(constructor, str):
            self.params["constructor"] = constructor
        elif isinstance(constructor, Constructor):
            self.params["constructor"] = constructor.constructor_id
        else:
            raise TypeError("Function parameter must be of type Constructor or str")
        return self

    def qualifying(self, position: int) -> Ergast:
        """
        Add a qualifying position to the current query

        >>> e.season(2021).qualifying(1).get_drivers()
        """
        self.params["qualifying"] = position
        return self

    def sprint(self, position: int) -> Ergast:
        """
        Add a sprint result to the current query

        >>> e.season(2021).sprint(3).get_sprints()
        """
        self.params["sprint"] = position
        return self

    def grid(self, position: int) -> Ergast:
        """
        Add a starting grid position to the current query

        >>> e.season(2021).round(1).grid(1).get_result()
        """
        self.params["grid"] = position
        return self

    def result(self, position: int) -> Ergast:
        """
        Add a final result to the current query

        >>> e.season(2021).round(1).result(20).get_result()
        """
        self.params["result"] = position
        return self

    def fastest(self, position: int) -> Ergast:
        """
        Add a driver's fastest lap ranking to the current query

        >>> e.season(2021).round(1).fastest(1).get_driver()
        """
        self.params["fastest"] = position
        return self

    def circuit(self, circuit) -> Ergast:
        """
        Add a circuit to the current query

        >>> silverstone = e.circuit("silverstone").get_circuit()
        >>> e.circuit(silverstone)
        """
        if isinstance(circuit, str):
            self.params["circuit"] = circuit
        elif isinstance(circuit, Circuit):
            self.params["circuit"] = circuit.circuit_id
        else:
            raise TypeError("Function parameter must be of type Circuit or str")
        return self

    def status(self, status) -> Ergast:
        """
        Add a finishing status to the current query

        >>> e.driver("alonso").status(2)
        """
        if isinstance(status, str):
            self.params["status"] = status
        elif isinstance(status, int):
            self.params["status"] = StatusType().string_to_id[status]
        else:
            raise TypeError("Function parameter must be of type int or str")
        return self

    def standing(self, position: int) -> Ergast:
        """
        Add a position in the standings to the current query

        >>> e.standing(1).get_driver_standings()
        """
        self.params["standing"] = position
        return self

    def lap(self, lap_number: int) -> Ergast:
        """
        Add a certain lap to the current query

        >>> e.season(2021).round(1).lap(1).get_laps()
        """
        self.params["lap"] = lap_number
        return self

    def pit_stop(self, stop_number: int) -> Ergast:
        """
        Add a certain pit stop to the current query

        >>> e.season(2021).round(1).pit_stop(1).get_pit_stops()
        """
        self.params["pit_stop"] = stop_number
        return self

    #
    #   PAGING FUNCTIONS
    #

    def limit(self, amount: int) -> Ergast:
        """
        Limit the results in the current query

        >>> e.season(2021).limit(2).get_drivers()
        """
        self.params["limit"] = amount
        return self

    def offset(self, amount: int) -> Ergast:
        """
        Offset the results in the current query

        >>> e.season(2021).limit(2).offset(4).get_drivers()
        """
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
        raise Exception(
            f"Data loss will occur with this query. 1 item"
            f" requested but {len(items)} found."
        )

    #   Race and Results Queries

    def get_circuits(self) -> list[Circuit]:
        """
        Get a list of circuits from the current query
        """
        return self._get_items(
            self.requester.get_circuits, self.type_constructor.construct_circuits
        )

    def get_circuit(self) -> Circuit:
        """
        Get a circuit from the current query
        """
        return self._get_item(
            self.requester.get_circuits, self.type_constructor.construct_circuits
        )

    def get_constructors(self) -> list[Constructor]:
        """
        Get a list of constructors from the current query
        """
        return self._get_items(
            self.requester.get_constructors,
            self.type_constructor.construct_constructors,
        )

    def get_constructor(self) -> Constructor:
        """
        Get a constructor from the current query
        """
        return self._get_item(
            self.requester.get_constructors,
            self.type_constructor.construct_constructors,
        )

    def get_drivers(self) -> list[Driver]:
        """
        Get a list of drivers from the current query
        """
        return self._get_items(
            self.requester.get_drivers, self.type_constructor.construct_drivers
        )

    def get_driver(self) -> Driver:
        """
        Get a driver from the current query
        """
        return self._get_item(
            self.requester.get_drivers, self.type_constructor.construct_drivers
        )

    def get_qualifyings(self) -> list[Race]:
        """
        Get a list of qualifyings from the current query
        """
        return self._get_items(
            self.requester.get_qualifying, self.type_constructor.construct_races
        )

    def get_qualifying(self) -> Race:
        """
        Get a qualifying from the current query
        """
        return self._get_item(
            self.requester.get_qualifying, self.type_constructor.construct_races
        )

    def get_sprints(self) -> list[Race]:
        """
        Get a list of sprints from the current query
        """
        return self._get_items(
            self.requester.get_sprints, self.type_constructor.construct_races
        )

    def get_sprint(self) -> Race:
        """
        Get a sprint from the current query
        """
        return self._get_item(
            self.requester.get_sprints, self.type_constructor.construct_races
        )

    def get_results(self) -> list[Race]:
        """
        Get a list of results from the current query
        """
        return self._get_items(
            self.requester.get_results, self.type_constructor.construct_races
        )

    def get_result(self) -> Race:
        """
        Get a result from the current query
        """
        return self._get_item(
            self.requester.get_results, self.type_constructor.construct_races
        )

    def get_races(self) -> list[Race]:
        """
        Get a list of races from the current query
        """
        return self._get_items(
            self.requester.get_races, self.type_constructor.construct_races
        )

    def get_race(self) -> Race:
        """
        Get a race from the current query
        """
        return self._get_item(
            self.requester.get_races, self.type_constructor.construct_races
        )

    def get_seasons(self) -> list[Season]:
        """
        Get a list of seasons from the current query
        """
        return self._get_items(
            self.requester.get_seasons, self.type_constructor.construct_seasons
        )

    def get_season(self) -> Season:
        """
        Get a season from the current query
        """
        return self._get_item(
            self.requester.get_seasons, self.type_constructor.construct_seasons
        )

    def get_statuses(self) -> list[Status]:
        """
        Get a list of statuses from the current query
        """
        return self._get_items(
            self.requester.get_statuses, self.type_constructor.construct_statuses
        )

    def get_status(self) -> Status:
        """
        Get a status from the current query
        """
        return self._get_item(
            self.requester.get_statuses, self.type_constructor.construct_statuses
        )

    #   Standings Queries

    def get_driver_standings(self) -> list[StandingsList]:
        """
        Get a list of driver standings from the current query
        """
        return self._get_items(
            self.requester.get_driver_standings,
            self.type_constructor.construct_standings_lists,
        )

    def get_driver_standing(self) -> StandingsList:
        """
        Get a driver standing from the current query
        """
        return self._get_item(
            self.requester.get_driver_standings,
            self.type_constructor.construct_standings_lists,
        )

    def get_constructor_standings(self) -> list[StandingsList]:
        """
        Get a list of constructor standings from the current query
        """
        return self._get_items(
            self.requester.get_constructor_standings,
            self.type_constructor.construct_standings_lists,
        )

    def get_constructor_standing(self) -> StandingsList:
        """
        Get a constructor standing from the current query
        """
        return self._get_item(
            self.requester.get_constructor_standings,
            self.type_constructor.construct_standings_lists,
        )

    #   Laps and Pit Stops Queries

    def get_laps(self) -> list[Race]:
        """
        Get a list of laps from the current query
        """
        return self._get_items(
            self.requester.get_laps, self.type_constructor.construct_races
        )

    def get_lap(self) -> Race:
        """
        Get a lap from the current query
        """
        return self._get_item(
            self.requester.get_laps, self.type_constructor.construct_races
        )

    def get_pit_stops(self) -> list[Race]:
        """
        Get a list of pit stops from the current query
        """
        return self._get_items(
            self.requester.get_pit_stops, self.type_constructor.construct_races
        )

    def get_pit_stop(self) -> Race:
        """
        Get a pit stop from the current query
        """
        return self._get_item(
            self.requester.get_pit_stops, self.type_constructor.construct_races
        )

""" Requester class """

import json
from typing import Callable

import requests
from uritemplate import URITemplate

HOST = "https://ergast.com/api"
SERIES = "f1"


class Requester:
    """
    Perform requests to the Ergast API
    """

    def _get_race_results_params(self, param: dict) -> dict:
        return {
            "season": param["season"],
            "round": param["round"],
            "filters": {
                "drivers": param["driver"],
                "constructors": param["constructor"],
                "grid": param["grid"],
                "qualifying": param["qualifying"],
                "sprint": param["sprint"],
                "fastest": param["fastest"],
                "circuits": param["circuit"],
                "status": param["status"],
                "results": param["result"],
                "races": param["races"],
                "seasons": param["seasons"],
            },
            "paging": {
                "limit": param["limit"],
                "offset": param["offset"],
            },
        }

    def _get_race_results_criteria(self, params: dict, resource: str) -> dict:
        criteria = []
        for key, value in params["filters"].items():
            if key != resource and value is not None:
                criteria.append(key)
                criteria.append(value)

        value = params["filters"][resource]

        return {"resource": resource, "value": value, "criteria": criteria}

    def _get_standings_params(self, param: dict) -> dict:
        return {
            "season": param["season"],
            "round": param["round"],
            "filters": {
                "standing": param["standing"],
                "drivers": param["driver"],
                "constructors": param["constructor"],
            },
            "paging": {
                "limit": param["limit"],
                "offset": param["offset"],
            },
        }

    def _get_standings_criteria(self, params: dict, resource: str) -> dict:
        criteria = []
        for key, value in params["filters"].items():
            if key != "standing" and value is not None:
                criteria.append(key)
                criteria.append(value)

        value = params["filters"]["standing"]

        return {"resource": resource, "value": value, "criteria": criteria}

    def _get_laps_pit_stops_params(self, param: dict) -> dict:
        return {
            "season": param["season"],
            "round": param["round"],
            "filters": {
                "pitstops": param["pit_stop"],
                "laps": param["lap"],
                "drivers": param["driver"],
            },
            "paging": {
                "limit": param["limit"],
                "offset": param["offset"],
            },
        }

    def _get_laps_pit_stops_criteria(self, params: dict, resource: str) -> dict:
        criteria = []
        for key, value in params["filters"].items():
            if key != resource and value is not None:
                criteria.append(key)
                criteria.append(value)

        value = params["filters"][resource]

        return {"resource": resource, "value": value, "criteria": criteria}

    def run_request(
        self, season, round_no, criteria, resource, value=None, limit=None, offset=None
    ) -> dict:
        """
        Run a request against the API and return the JSON dictionary result
        """
        url_tmpl = URITemplate(
            "https://ergast.com/api{/series}{/season}{/round}"
            "{/criteria*}{/resource}{/value}.json{?limit,offset}"
        )
        url = url_tmpl.expand(
            host=HOST,
            series=SERIES,
            season=season,
            round=round_no,
            criteria=criteria,
            resource=resource,
            value=value,
            limit=limit,
            offset=offset,
        )

        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        raise Exception(
            f"Failed with status code {response.status_code}. Error: {response.reason}"
        )

    def _get_api_json(
        self, get_params: Callable, get_criteria: Callable, resource: str, param: dict
    ) -> dict:
        params = get_params(param)
        filters = get_criteria(params, resource)

        return self.run_request(
            season=params["season"],
            round_no=params["round"],
            criteria=filters["criteria"],
            resource=filters["resource"],
            value=filters["value"],
            limit=params["paging"]["limit"],
            offset=params["paging"]["offset"],
        )

    #
    #   Race and Results
    #

    def get_circuits(self, param: dict) -> dict:
        """
        Get the Circuits JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "circuits",
            param,
        )

        return api_json["MRData"]["CircuitTable"]["Circuits"]

    def get_constructors(self, param: dict) -> dict:
        """
        Get the Constructors JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "constructors",
            param,
        )

        return api_json["MRData"]["ConstructorTable"]["Constructors"]

    def get_drivers(self, param: dict) -> dict:
        """
        Get the Drivers JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "drivers",
            param,
        )

        return api_json["MRData"]["DriverTable"]["Drivers"]

    def get_qualifying(self, param: dict) -> dict:
        """
        Get the Qualifying JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "qualifying",
            param,
        )

        return api_json["MRData"]["RaceTable"]["Races"]

    def get_sprints(self, param: dict) -> dict:
        """
        Get the Sprints JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "sprint",
            param,
        )

        return api_json["MRData"]["RaceTable"]["Races"]

    def get_results(self, param: dict) -> dict:
        """
        Get the Results JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "results",
            param,
        )

        return api_json["MRData"]["RaceTable"]["Races"]

    def get_races(self, param: dict) -> dict:
        """
        Get the Races JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "races",
            param,
        )

        return api_json["MRData"]["RaceTable"]["Races"]

    def get_seasons(self, param: dict) -> dict:
        """
        Get the Seasons JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "seasons",
            param,
        )

        return api_json["MRData"]["SeasonTable"]["Seasons"]

    def get_statuses(self, param: dict) -> dict:
        """
        Get the Statuses JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_race_results_params,
            self._get_race_results_criteria,
            "status",
            param,
        )

        return api_json["MRData"]["StatusTable"]["Status"]

    #
    #   Standings
    #

    def get_driver_standings(self, param: dict) -> dict:
        """
        Get the Driver Standings JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_standings_params,
            self._get_standings_criteria,
            "driverStandings",
            param,
        )

        return api_json["MRData"]["StandingsTable"]["StandingsLists"]

    def get_constructor_standings(self, param: dict) -> dict:
        """
        Get the Constructor Standings JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_standings_params,
            self._get_standings_criteria,
            "constructorStandings",
            param,
        )

        return api_json["MRData"]["StandingsTable"]["StandingsLists"]

    #
    #   Laps and Pit Stops
    #

    def get_laps(self, param: dict) -> dict:
        """
        Get the Laps JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_laps_pit_stops_params,
            self._get_laps_pit_stops_criteria,
            "laps",
            param,
        )

        return api_json["MRData"]["RaceTable"]["Races"]

    def get_pit_stops(self, param: dict) -> dict:
        """
        Get the Pit Stops JSON from the Ergast API
        """
        api_json = self._get_api_json(
            self._get_laps_pit_stops_params,
            self._get_laps_pit_stops_criteria,
            "pitstops",
            param,
        )

        return api_json["MRData"]["RaceTable"]["Races"]

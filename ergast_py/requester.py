import json
import requests

from uritemplate import URITemplate

HOST = 'https://ergast.com/api'
SERIES = 'f1'

class Requester():
    """
        Perform requests to the Ergast API
    """

    def __init__(self) -> None:
        pass


    def _get_race_results_params(self, param: dict) -> dict:
        """ Acquire only the appropriate filters for Race/Results data """
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
            }
        }

    def _get_race_results_criteria(self, params: dict, resource: str) -> dict:
        """ Split the data into criteria and resource for Race/Results """
        criteria = []
        for key, value in params["filters"].items():
            if (key != resource and value != None):
                criteria.append(key)
                criteria.append(value)

        value = params["filters"][resource]

        return {
            "resource": resource,
            "value": value,
            "criteria": criteria
        }

    def _get_standings_params(self, param: dict) -> dict:
        """ Acquire only the appropriate filters for Standings data """
        return {
            "season": param["season"],
            "round": param["round"],
            "filters": {
                "standing": param["standing"],
                "drivers": param["driver"],
                "constructors": param["constructor"]
            },
            "paging": {
                "limit": param["limit"],
                "offset": param["offset"],
            }
        }

    def _get_standings_criteria(self, params: dict, resource: str) -> dict:
        """ Split the data into criteria and resource for standings """
        criteria = []
        for key, value in params["filters"].items():
            if (key != "standing" and value != None):
                criteria.append(key)
                criteria.append(value)

        value =  params["filters"]["standing"]

        return {
            "resource": resource,
            "value": value,
            "criteria": criteria
        }

    def _get_laps_pit_stops_params(self, param: dict) -> dict:
        """ Acquire only the appropriate filters for Laps and Pit Stops data """
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
            }
        }

    def _get_laps_pit_stops_criteria(self, params: dict, resource: str) -> dict:
        """ Split the data into criteria and resource for Laps and Pit Stops """
        criteria = []
        for key, value in params["filters"].items():
            if (key != resource and value != None):
                criteria.append(key)
                criteria.append(value)

        value = params["filters"][resource]

        return {
            "resource": resource,
            "value": value,
            "criteria": criteria
        }


    def run_request(self, season, round, criteria, resource, value=None, limit=None, offset=None) -> dict:
        """ Takes values to run the request and return a dict """
        url_tmpl = URITemplate('https://ergast.com/api{/series}{/season}{/round}'
                           '{/criteria*}{/resource}{/value}.json{?limit,offset}')
        url = url_tmpl.expand(host=HOST, series=SERIES, 
                              season=season, round=round,
                              criteria=criteria, resource=resource,
                              value=value, limit=limit, offset=offset)

        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(f"Failed with status code {response.status_code}. Error: {response.reason}")

    #
    #   Race and Results
    #

    def get_circuits(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "circuits")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["CircuitTable"]["Circuits"]


    def get_constructors(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "constructors")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["ConstructorTable"]["Constructors"]


    def get_drivers(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "drivers")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["DriverTable"]["Drivers"]


    def get_qualifying(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "qualifying")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["RaceTable"]["Races"]

    def get_sprints(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "sprint")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["RaceTable"]["Races"]

    def get_results(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "results")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["RaceTable"]["Races"]

    def get_races(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "races")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["RaceTable"]["Races"]

    def get_seasons(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "seasons")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["SeasonTable"]["Seasons"]

    def get_statuses(self, param: dict) -> dict:
        params = self._get_race_results_params(param)
        filters = self._get_race_results_criteria(params, "status")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["StatusTable"]["Status"]

    #
    #   Standings
    #

    def get_driver_standings(self, param: dict) -> dict:
        params = self._get_standings_params(param)
        filters = self._get_standings_criteria(params, "driverStandings")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["StandingsTable"]["StandingsLists"]

    def get_constructor_standings(self, param: dict) -> dict:
        params = self._get_standings_params(param)
        filters = self._get_standings_criteria(params, "constructorStandings")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["StandingsTable"]["StandingsLists"]

    #
    #   Laps and Pit Stops
    #

    def get_laps(self, param: dict) -> dict:
        params = self._get_laps_pit_stops_params(param)
        filters = self._get_laps_pit_stops_criteria(params, "laps")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["RaceTable"]["Races"]

    def get_pit_stops(self, param: dict) -> dict:
        params = self._get_laps_pit_stops_params(param)
        filters = self._get_laps_pit_stops_criteria(params, "pitstops")

        json = self.run_request(season=params["season"], round=params["round"],
                                criteria=filters["criteria"], resource=filters["resource"], value=filters["value"],
                                limit=params["paging"]["limit"], offset=params["paging"]["offset"])

        return json["MRData"]["RaceTable"]["Races"]
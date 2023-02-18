""" Tests for the Requester class """

import pytest
from ergast_py.requester import Requester

from tests import constants


class TestRequester():
    """
    Tests for the Requester class
    ~~~
    <Note>
    """

    r = Requester()

    def _construct_test_params(self, season=None, seasons=None, round_no=None, driver=None,
                               constructor=None, grid=None, qualifying=None, sprint=None,
                               result=None, fastest=None, circuit=None, status=None, standing=None,
                               races=None, limit=None, offset=None, lap=None, pit_stop=None):
        return {
            "season": season,
            "seasons": seasons,
            "round": round_no,
            "driver": driver,
            "constructor": constructor,
            "grid": grid,
            "qualifying": qualifying,
            "sprint": sprint,
            "result": result,
            "fastest": fastest,
            "circuit": circuit,
            "status": status,
            "standing": standing,
            "races": races,
            "limit": limit,
            "offset": offset,
            "lap": lap,
            "pit_stop": pit_stop,
        }


    def test_run_request_doesnt_fail(self):
        """ Assert a valid request doesn't fail """
        self.r.run_request(season=2008, round_no=5, criteria=["drivers", "alonso"],
                           resource="driverStandings")


    def test_run_request_fails(self):
        """ Assert an invalid request fails """
        with pytest.raises(Exception):
            self.r.run_request(season=2008, round_no=5, criteria=["drivers", "alonso"],
                               resource="bad request")


    def test_get_circuit(self):
        """ Test the get_circuit function """
        expected = [constants.ISTANBUL]

        params = self._construct_test_params(season=2008, round_no=5)

        assert self.r.get_circuits(params) == expected


    def test_get_constructors(self):
        """ Test the get_constructors function """
        expected = [constants.FERRARI]

        params = self._construct_test_params(constructor="ferrari")

        assert self.r.get_constructors(params) == expected


    def test_get_drivers(self):
        """ Test the get_drivers function """
        expected = [constants.ALONSO]

        params = self._construct_test_params(driver="alonso")

        assert self.r.get_drivers(params) == expected


    def test_get_qualifying(self):
        """ Test the get_qualifying function """
        expected = [
            {
                "season":"2008",
                "round":"5",
                "url":"http://en.wikipedia.org/wiki/2008_Turkish_Grand_Prix",
                "raceName":"Turkish Grand Prix",
                "Circuit": constants.ISTANBUL,
                "date":"2008-05-11",
                "time":"12:00:00Z",
                "QualifyingResults":[
                    {
                        "number":"5",
                        "position":"7",
                        "Driver": constants.ALONSO,
                        "Constructor": constants.RENAULT,
                        "Q1":"1:26.836",
                        "Q2":"1:26.522",
                        "Q3":"1:28.422"
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2008, round_no=5, qualifying=7)

        assert self.r.get_qualifying(params) == expected


    def test_get_sprints(self):
        """ Test the get_sprints function """
        expected = [
            {
                "season":"2021",
                "round":"10",
                "url":"http://en.wikipedia.org/wiki/2021_British_Grand_Prix",
                "raceName":"British Grand Prix",
                "Circuit": constants.SILVERSTONE,
                "date":"2021-07-18",
                "time":"14:00:00Z",
                "SprintResults":[
                    {
                        "number":"14",
                        "position":"7",
                        "positionText":"7",
                        "points":"0",
                        "Driver": constants.ALONSO,
                        "Constructor": constants.ALPINE,
                        "grid":"11",
                        "laps":"17",
                        "status":"Finished",
                        "Time":{
                            "millis":"1581953",
                            "time":"+43.527"
                        },
                        "FastestLap":{
                            "lap":"17",
                            "Time":{
                                "time":"1:31.773"
                            }
                        }
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2021, round_no=10, sprint=7)

        assert self.r.get_sprints(params) == expected


    def test_get_results(self):
        """ Test the get_results function """
        expected = [
            {
                "season":"2021",
                "round":"16",
                "url":"http://en.wikipedia.org/wiki/2021_Turkish_Grand_Prix",
                "raceName":"Turkish Grand Prix",
                "Circuit": constants.ISTANBUL,
                "date":"2021-10-10",
                "time":"12:00:00Z",
                "Results":[
                    {
                        "number":"14",
                        "position":"16",
                        "positionText":"16",
                        "points":"0",
                        "Driver": constants.ALONSO,
                        "Constructor": constants.ALPINE,
                        "grid":"5",
                        "laps":"57",
                        "status":"+1 Lap",
                        "FastestLap":{
                            "rank":"14",
                            "lap":"55",
                            "Time":{
                                "time":"1:33.252"
                            },
                            "AverageSpeed":{
                                "units":"kph",
                                "speed":"206.073"
                            }
                        }
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2021, round_no=16, result=16)

        assert self.r.get_results(params) == expected


    def test_get_races(self):
        """ Test the get_races function """
        expected = [
            {
                "season":"2021",
                "round":"16",
                "url":"http://en.wikipedia.org/wiki/2021_Turkish_Grand_Prix",
                "raceName":"Turkish Grand Prix",
                "Circuit": constants.ISTANBUL,
                "date":"2021-10-10",
                "time":"12:00:00Z",
                "FirstPractice":{
                    "date":"2021-10-08"
                },
                "SecondPractice":{
                    "date":"2021-10-08"
                },
                "ThirdPractice":{
                    "date":"2021-10-09"
                },
                "Qualifying":{
                    "date":"2021-10-09"
                }
            }
        ]

        params = self._construct_test_params(season=2021, round_no=16)

        assert self.r.get_races(params) == expected


    def test_get_seasons(self):
        """ Test the get_seasons function """
        expected = [
            {
                "season":"2021",
                "url":"http://en.wikipedia.org/wiki/2021_Formula_One_World_Championship"
            }
        ]

        params = self._construct_test_params(season=2021)

        assert self.r.get_seasons(params) == expected


    def test_get_statuses(self):
        """ Test the get_statuses function """
        expected = [
            {
                "statusId":"11",
                "count":"1",
                "status":"+1 Lap"
            }
        ]

        params = self._construct_test_params(season=2021, round_no=16, result=16)

        assert self.r.get_statuses(params) == expected


    def test_get_driver_standings(self):
        """ Test the get_driver_standings function """
        expected = [
            {
                "season":"2021",
                "round":"16",
                "DriverStandings":[
                    {
                        "position":"10",
                        "positionText":"10",
                        "points":"58",
                        "wins":"0",
                        "Driver": constants.ALONSO,
                        "Constructors":[
                            constants.ALPINE
                        ]
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2021, round_no=16, driver="alonso")

        assert self.r.get_driver_standings(params) == expected


    def test_get_constructor_standings(self):
        """ Test the get_constructor_standi function """
        expected = [
            {
                "season":"2021",
                "round":"16",
                "ConstructorStandings":[
                    {
                        "position":"5",
                        "positionText":"5",
                        "points":"104",
                        "wins":"1",
                        "Constructor": constants.ALPINE
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2021, round_no=16, standing=5)

        assert self.r.get_constructor_standings(params) == expected


    def test_get_laps(self):
        """ Test the get_laps function """
        expected = [
            {
                "season":"2008",
                "round":"5",
                "url":"http://en.wikipedia.org/wiki/2008_Turkish_Grand_Prix",
                "raceName":"Turkish Grand Prix",
                "Circuit": constants.ISTANBUL,
                "date":"2008-05-11",
                "time":"12:00:00Z",
                "Laps":[
                    {
                        "number":"1",
                        "Timings":[
                            {
                                "driverId":"alonso",
                                "position":"5",
                                "time":"1:57.681"
                            }
                        ]
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2008, round_no=5, driver="alonso", lap=1)

        assert self.r.get_laps(params) == expected


    def test_get_pit_stops(self):
        """ Test the get_pit_stops function """
        expected = [
            {
                "season":"2021",
                "round":"16",
                "url":"http://en.wikipedia.org/wiki/2021_Turkish_Grand_Prix",
                "raceName":"Turkish Grand Prix",
                "Circuit": constants.ISTANBUL,
                "date":"2021-10-10",
                "time":"12:00:00Z",
                "PitStops":[
                    {
                        "driverId":"alonso",
                        "lap":"30",
                        "stop":"1",
                        "time":"15:51:43",
                        "duration":"29.116"
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2021, round_no=16, driver="alonso", pit_stop=1)

        assert self.r.get_pit_stops(params) == expected

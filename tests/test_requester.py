import ergast_py
import pytest
import tests.test_constants as test_constants

class TestRequester():
    """
    Tests for the Requester class
    """

    r = ergast_py.Requester()

    def _construct_test_params(self, season=None, seasons=None, round=None, driver=None, constructor=None, grid=None,
                               qualifying=None, sprint=None, result=None, fastest=None, circuit=None, status=None,
                               standing=None, races=None, limit=None, offset=None, lap=None, pit_stop=None):
        return {
            "season": season,
            "seasons": seasons,
            "round": round,
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


    def test_run_request(self):
        self.r.run_request(season=2008, round=5, criteria=["drivers", "alonso"], resource="driverStandings")


    def test_run_request_fails(self):
        with pytest.raises(Exception):
            self.r.run_request(season=2008, round=5, criteria=["drivers", "alonso"], resource="bad request")


    def test_get_circuit(self):
        expected = [test_constants.istanbul]

        params = self._construct_test_params(season=2008, round=5)

        assert self.r.get_circuits(params) == expected


    def test_get_constructors(self):
        expected = [test_constants.ferrari]

        params = self._construct_test_params(constructor="ferrari")

        assert self.r.get_constructors(params) == expected


    def test_get_drivers(self):
        expected = [test_constants.alonso]

        params = self._construct_test_params(driver="alonso")

        assert self.r.get_drivers(params) == expected

    
    def test_get_qualifying(self):
        expected = [
            {
                "season":"2008",
                "round":"5",
                "url":"http://en.wikipedia.org/wiki/2008_Turkish_Grand_Prix",
                "raceName":"Turkish Grand Prix",
                "Circuit": test_constants.istanbul,
                "date":"2008-05-11",
                "time":"12:00:00Z",
                "QualifyingResults":[
                    {
                        "number":"5",
                        "position":"7",
                        "Driver": test_constants.alonso,
                        "Constructor": test_constants.renault,
                        "Q1":"1:26.836",
                        "Q2":"1:26.522",
                        "Q3":"1:28.422"
                    }
                ]
            }
        ]

        params = self._construct_test_params(season=2008, round=5, qualifying=7)

        assert self.r.get_qualifying(params) == expected
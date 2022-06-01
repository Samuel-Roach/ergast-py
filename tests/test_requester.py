import ergast_py
import pytest

class TestRequester():
    """
    Tests for the Requester class
    """

    r = ergast_py.Requester()

    def test_run_request(self):
        self.r.run_request(season=2008, round=5, criteria=["drivers", "alonso"], resource="driverStandings")

    def test_run_request_fails(self):
        with pytest.raises(Exception):
            self.r.run_request(season=2008, round=5, criteria=["drivers", "alonso"], resource="bad request")
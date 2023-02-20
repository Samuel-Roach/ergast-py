""" Tests for the Ergast class """

import ergast_py


class TestErgast:
    """
    Tests for the Ergast class
    """

    e = ergast_py.Ergast()

    def test_paging(self):
        """ Assert that paging changes the results pages """
        hamilton = self.e.season(2021).limit(1).offset(1).get_driver_standings()
        assert hamilton[0].driver_standings[0].driver.driver_id == "hamilton"

    def test_reset(self):
        """ Assert the function resetting works """
        self.e.season(2021).limit(1).offset(1)
        self.e.reset()
        verstappen = self.e.season(2021).limit(1)
        assert verstappen.get_driver_standing().driver_standings[0].driver.driver_id == "max_verstappen"

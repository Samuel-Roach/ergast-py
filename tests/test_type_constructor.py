from copyreg import constructor
import datetime
from ergast_py.models.average_speed import AverageSpeed

from ergast_py.models.circuit import Circuit
from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver
from ergast_py.models.fastest_lap import FastestLap
from ergast_py.models.location import Location
from ergast_py.models.result import Result
from ergast_py.requester import Requester
from ergast_py.type_constructor import TypeConstructor

import tests.test_constants as test_constants


class TestTypeConstructor():
    """
    Tests for the Type Constructor class
    """

    t = TypeConstructor()
    r = Requester()

    def _assert_locations(self, expected: Location, actual: Location):
        assert actual.latitude == expected.latitude
        assert actual.longitude == expected.longitude
        assert actual.locality == expected.locality
        assert actual.country == expected.country

    def _assert_circuits(self, expected: Circuit, actual: Circuit):
        assert actual.circuit_id == expected.circuit_id
        assert actual.url == expected.url
        assert actual.circuit_name == expected.circuit_name
        self._assert_locations(expected.location, actual.location)

    def _assert_constructors(self, expected: Constructor, actual: Constructor):
        assert actual.constructor_id == expected.constructor_id
        assert actual.url == expected.url
        assert actual.name == expected.name
        assert actual.nationality == expected.nationality

    def _assert_drivers(self, expected: Driver, actual: Driver):
        assert actual.driver_id == expected.driver_id
        assert actual.code == expected.code
        assert actual.url == expected.url
        assert actual.given_name == expected.given_name
        assert actual.family_name == expected.family_name
        assert actual.date_of_birth == expected.date_of_birth
        assert actual.nationality == expected.nationality
        assert actual.permanent_number == expected.permanent_number

    def _assert_average_speeds(self, expected: AverageSpeed, actual: AverageSpeed):
        assert actual.units == expected.units
        assert actual.speed == expected.speed

    def _assert_fastest_laps(self, expected: FastestLap, actual: FastestLap):
        assert actual.rank == expected.rank
        assert actual.lap == expected.lap
        assert actual.time == expected.time
        assert actual.average_speed == expected.average_speed

    def _assert_results(self, expected: Result, actual: Result):
        assert actual.number == expected.number
        assert actual.position == expected.position
        assert actual.position_text == expected.position_text
        assert actual.points == expected.points
        self._assert_drivers(expected.driver, actual.driver)
        self._assert_constructors(expected.constructor, actual.constructor)
        assert actual.grid == expected.grid
        assert actual.laps == expected.laps
        assert actual.status == expected.status
        assert actual.time == expected.time
        self._assert_fastest_laps(expected.fastest_lap, actual.fastest_lap)
        assert actual.qual_1 == expected.qual_1
        assert actual.qual_2 == expected.qual_2
        assert actual.qual_3 == expected.qual_3

    #
    #   Tests
    #

    def test_construct_circuit(self):
        params = {
            "circuitId":"bahrain",
            "url":"http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
            "circuitName":"Bahrain International Circuit",
            "Location":{
                "lat":"26.0325",
                "long":"50.5106",
                "locality":"Sakhir",
                "country":"Bahrain"
            }
        }

        location = Location(latitude=26.0325,
                            longitude=50.5106,
                            locality="Sakhir",
                            country="Bahrain")

        expected = Circuit(circuit_id="bahrain",
                            url="http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
                            circuit_name="Bahrain International Circuit",
                            location=location)

        actual = self.t.construct_circuit(params)
        self._assert_circuits(expected, actual)

    def test_construct_constructor(self):
        params = test_constants.ALPINE

        expected = Constructor(constructor_id="alpine",
                                url="http://en.wikipedia.org/wiki/Alpine_F1_Team",
                                name="Alpine F1 Team",
                                nationality="French")

        actual = self.t.construct_constructor(params)
        self._assert_constructors(expected, actual)

    def test_construct_driver(self):
        params = test_constants.ALONSO

        expected = Driver(driver_id="alonso",
                           code="ALO",
                           url="http://en.wikipedia.org/wiki/Fernando_Alonso",
                           given_name="Fernando",
                           family_name="Alonso",
                           date_of_birth=datetime.date(year=1981, month=7, day=29),
                           nationality="Spanish",
                           permanent_number=14
                           )

        actual = self.t.construct_driver(params)
        self._assert_drivers(expected, actual)

    def test_construct_races(self):
        pass

    def test_construct_results(self):
        params ={
            "number":"16",
            "position":"1",
            "positionText":"1",
            "points":"26",
            "Driver": test_constants.LECLERC,
            "Constructor": test_constants.FERRARI,
            "grid":"1",
            "laps":"57",
            "status":"Finished",
            "Time":{
                "millis":"5853584",
                "time":"1:37:33.584"
            },
            "FastestLap":{
                "rank":"1",
                "lap":"51",
                "Time":{
                    "time":"1:34.570"
                },
                "AverageSpeed":{
                    "units":"kph",
                    "speed":"206.018"
                }
            }
        }

        avg_speed = AverageSpeed(units="kph", speed=206.018)
        fastest_lap = FastestLap(rank=1, lap=51,
                                 time=datetime.time(minute=1, second=34, microsecond=570000),
                                 average_speed=avg_speed)
        driver = Driver(driver_id="leclerc", code="LEC",
                        url="http://en.wikipedia.org/wiki/Charles_Leclerc",
                        given_name="Charles", family_name="Leclerc",
                        date_of_birth=datetime.date(year=1997, month=10, day=16),
                        nationality="Monegasque", permanent_number=16)
        constructor = Constructor(constructor_id="ferrari",
                                  url="http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                                  name="Ferrari", nationality="Italian")
        
        expected = Result(number=16, position=1, position_text="1", points=26, driver=driver,
                           constructor=constructor, grid=1, laps=57, status=1,
                           time=datetime.time(hour=1, minute=37, second=33, microsecond=584000),
                           fastest_lap=fastest_lap, qual_1=None, qual_2=None, qual_3=None)

        actual = self.t.construct_result(params)
        self._assert_results(expected, actual)

    def test_construct_pit_stops(self):
        pass

    def test_construct_laps(self):
        # Check Timings too
        pass

    def test_construct_seasons(self):
        pass

    def test_construct_statuses(self):
        pass

    def test_construct_standings_lists(self):
        # Check Driver Standings
        # Check constructor standings
        pass

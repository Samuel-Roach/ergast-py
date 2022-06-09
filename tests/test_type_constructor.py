from copyreg import constructor
import datetime
from this import d
from ergast_py.models.average_speed import AverageSpeed

from ergast_py.models.circuit import Circuit
from ergast_py.models.constructor import Constructor
from ergast_py.models.driver import Driver
from ergast_py.models.fastest_lap import FastestLap
from ergast_py.models.location import Location
from ergast_py.models.pit_stop import PitStop
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

    #
    #   Tests
    #

    def test_construct_circuit(self):
        params = [{
            "circuitId":"bahrain",
            "url":"http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
            "circuitName":"Bahrain International Circuit",
            "Location":{
                "lat":"26.0325",
                "long":"50.5106",
                "locality":"Sakhir",
                "country":"Bahrain"
            }
        }]

        location = Location(latitude=26.0325,
                            longitude=50.5106,
                            locality="Sakhir",
                            country="Bahrain")

        expected = [Circuit(circuit_id="bahrain",
                            url="http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
                            circuit_name="Bahrain International Circuit",
                            location=location)]

        assert expected == self.t.construct_circuits(params)

    def test_construct_constructor(self):
        params = [test_constants.ALPINE]

        expected = [Constructor(constructor_id="alpine",
                                url="http://en.wikipedia.org/wiki/Alpine_F1_Team",
                                name="Alpine F1 Team",
                                nationality="French")]

        assert expected == self.t.construct_constructors(params)

    def test_construct_driver(self):
        params = [test_constants.ALONSO]

        expected = [Driver(driver_id="alonso",
                           code="ALO",
                           url="http://en.wikipedia.org/wiki/Fernando_Alonso",
                           given_name="Fernando",
                           family_name="Alonso",
                           date_of_birth=datetime.date(year=1981, month=7, day=29),
                           nationality="Spanish",
                           permanent_number=14
                           )]

        assert expected == self.t.construct_drivers(params)

    def test_construct_races(self):
        pass

    def test_construct_results(self):
        params = [{
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
        }]

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
        
        expected = [Result(number=16, position=1, position_text="1", points=26, driver=driver,
                           constructor=constructor, grid=1, laps=57, status=1,
                           time=datetime.time(hour=1, minute=37, second=33, microsecond=584000),
                           fastest_lap=fastest_lap, qual_1=None, qual_2=None, qual_3=None)]

        assert expected == self.t.construct_results(params)

    def test_construct_pit_stops(self):
        params = [{
            "driverId":"alonso",
            "lap":"11",
            "stop":"1",
            "time":"18:22:10",
            "duration":"25.365"
        }]

        expected = [PitStop(
            driver_id="alonso",
            lap=11,
            stop=1,
            local_time=datetime.time(hour=18, minute=22, second=10),
            duration=datetime.time(second=25, microsecond=365000)
        )]
        
        assert expected == self.t.construct_pit_stops(params)

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
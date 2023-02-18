""" Tests for the Type Constructor class """

import datetime

from ergast_py.models.average_speed import AverageSpeed
from ergast_py.models.circuit import Circuit
from ergast_py.models.constructor import Constructor
from ergast_py.models.constructor_standing import ConstructorStanding
from ergast_py.models.driver import Driver
from ergast_py.models.driver_standing import DriverStanding
from ergast_py.models.fastest_lap import FastestLap
from ergast_py.models.lap import Lap
from ergast_py.models.location import Location
from ergast_py.models.pit_stop import PitStop
from ergast_py.models.race import Race
from ergast_py.models.result import Result
from ergast_py.models.season import Season
from ergast_py.models.standings_list import StandingsList
from ergast_py.models.status import Status
from ergast_py.models.timing import Timing
from ergast_py.requester import Requester
from ergast_py.type_constructor import TypeConstructor

from tests import constants


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
        """ Assert construct_circuit function works"""
        params = [constants.BAHRAIN]

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
        """ Assert construct_constructor function works"""
        params = [constants.ALPINE]

        expected = [Constructor(constructor_id="alpine",
                                url="http://en.wikipedia.org/wiki/Alpine_F1_Team",
                                name="Alpine F1 Team",
                                nationality="French")]

        assert expected == self.t.construct_constructors(params)

    def test_construct_driver(self):
        """ Assert construct_driver function works"""
        params = [constants.ALONSO]

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
        """ Assert construct_races function works"""
        params = [{
            "season":"2022",
            "round":"1",
            "url":"http://en.wikipedia.org/wiki/2022_Bahrain_Grand_Prix",
            "raceName":"Bahrain Grand Prix",
            "Circuit": constants.BAHRAIN,
            "date":"2022-03-20",
            "time":"15:00:00Z",
            "FirstPractice":{
                "date":"2022-03-18",
                "time":"12:00:00Z"
            },
            "SecondPractice":{
                "date":"2022-03-18",
                "time":"15:00:00Z"
            },
            "ThirdPractice":{
                "date":"2022-03-19",
                "time":"12:00:00Z"
            },
            "Qualifying":{
                "date":"2022-03-19",
                "time":"15:00:00Z"
            }
        }]

        location = Location(latitude=26.0325,
                            longitude=50.5106,
                            locality="Sakhir",
                            country="Bahrain")
        bahrain = Circuit(circuit_id="bahrain",
                            url="http://en.wikipedia.org/wiki/Bahrain_International_Circuit",
                            circuit_name="Bahrain International Circuit",
                            location=location)

        expected = [Race(
                season=2022, round_no=1, url="http://en.wikipedia.org/wiki/2022_Bahrain_Grand_Prix",
                race_name="Bahrain Grand Prix", circuit=bahrain,
                date=datetime.datetime(year=2022, month=3, day=20, hour=15,
                                       tzinfo=datetime.timezone.utc),
                results=[],
                first_practice=datetime.datetime(year=2022, month=3, day=18, hour=12,
                                                 tzinfo=datetime.timezone.utc),
                second_practice=datetime.datetime(year=2022, month=3, day=18, hour=15,
                                                  tzinfo=datetime.timezone.utc),
                third_practice=datetime.datetime(year=2022, month=3, day=19, hour=12,
                                                 tzinfo=datetime.timezone.utc),
                sprint=None, sprint_results=[],
                qualifying=datetime.datetime(year=2022, month=3, day=19, hour=15,
                                             tzinfo=datetime.timezone.utc),
                qualifying_results=[], pit_stops=[], laps=[]
        )]

        assert expected == self.t.construct_races(params)

    def test_construct_results(self):
        """ Assert construct_results function works"""
        params = [{
            "number":"16",
            "position":"1",
            "positionText":"1",
            "points":"26",
            "Driver": constants.LECLERC,
            "Constructor": constants.FERRARI,
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
        """ Assert construct_pit_stops function works"""
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
        """ Assert construct_laps function works"""
        params = [{
            "number":"1",
            "Timings":[{
                "driverId":"leclerc",
                "position":"1",
                "time":"1:39.070"
            }]
        }]

        timing = Timing(
            driver_id="leclerc",
            position=1,
            time=datetime.time(minute=1, second=39, microsecond=70000))

        expected = [Lap(number=1, timings=[timing])]

        assert expected == self.t.construct_laps(params)

    def test_construct_seasons(self):
        """ Assert construct_seasons function works"""
        params = [{
            "season":"2022",
            "url":"http://en.wikipedia.org/wiki/2022_Formula_One_World_Championship"
        }]

        expected = [Season(
            season=2022,
            url="http://en.wikipedia.org/wiki/2022_Formula_One_World_Championship"
        )]

        assert expected == self.t.construct_seasons(params)

    def test_construct_statuses(self):
        """ Assert construct_statuses function works"""
        params = [{
            "statusId":"1",
            "count":"1",
            "status":"Finished"
        }]

        expected = [Status(
            status_id=1,
            count=1,
            status="Finished"
        )]

        assert expected == self.t.construct_statuses(params)

    def test_construct_standings_lists(self):
        """ Assert construct_standings_lists function works"""
        # Check Driver Standings
        # Check constructor standings
        params = [{
            "season":"2005",
            "round":"19",
            "DriverStandings":[{
                "position":"1",
                "positionText":"1",
                "points":"133",
                "wins":"7",
                "Driver":constants.ALONSO,
                "Constructors":[constants.ALPINE]
            }],
            "ConstructorStandings":[{
                "position":"1",
                "positionText":"1",
                "points":"235",
                "wins":"5",
                "Constructor": constants.FERRARI
            }]
        }]

        alpine = Constructor(constructor_id="alpine",
                                url="http://en.wikipedia.org/wiki/Alpine_F1_Team",
                                name="Alpine F1 Team",
                                nationality="French")
        alonso = Driver(driver_id="alonso",
                           code="ALO",
                           url="http://en.wikipedia.org/wiki/Fernando_Alonso",
                           given_name="Fernando",
                           family_name="Alonso",
                           date_of_birth=datetime.date(year=1981, month=7, day=29),
                           nationality="Spanish",
                           permanent_number=14
                           )
        driver_standings = DriverStanding(
            position=1, position_text="1", points=133, wins=7, driver=alonso, constructors=[alpine]
        )
        ferrari = Constructor(constructor_id="ferrari",
                                  url="http://en.wikipedia.org/wiki/Scuderia_Ferrari",
                                  name="Ferrari", nationality="Italian")
        constructor_standings = ConstructorStanding(
            position=1, position_text="1", points=235, wins=5, constructor=ferrari
        )

        expected = [StandingsList(
            season=2005,
            round_no=19,
            driver_standings=[driver_standings],
            constructor_standings=[constructor_standings]
        )]

        assert expected == self.t.construct_standings_lists(params)

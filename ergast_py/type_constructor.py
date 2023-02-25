""" TypeConstructor class """
from ergast_py.constants.expected import Expected
from ergast_py.constants.status_type import StatusType
from ergast_py.helpers import Helpers
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


# pylint: disable=too-many-public-methods
class TypeConstructor:
    """
    Class for constructing types out of dicts
    """

    def __init__(self) -> None:
        pass

    #
    #   PRIVATE METHODS
    #

    @staticmethod
    def _populate_missing(expected: dict, actual: dict) -> dict:
        for item in expected:
            if item not in actual:
                if expected[item] == "dict":
                    actual[item] = {}
                elif expected[item] == "float":
                    actual[item] = "0.0"
                elif expected[item] == "int":
                    actual[item] = "0"
                else:
                    actual[item] = ""
        return actual

    def _populate_missing_location(self, location: dict) -> dict:
        return self._populate_missing(expected=Expected().location, actual=location)

    def _populate_missing_circuit(self, circuit: dict) -> dict:
        return self._populate_missing(expected=Expected().circuit, actual=circuit)

    def _populate_missing_constructor(self, constructor: dict) -> dict:
        return self._populate_missing(
            expected=Expected().constructor, actual=constructor
        )

    def _populate_missing_driver(self, driver: dict) -> dict:
        return self._populate_missing(expected=Expected().driver, actual=driver)

    def _populate_missing_race(self, race: dict) -> dict:
        return self._populate_missing(expected=Expected().race, actual=race)

    def _populate_missing_result(self, result: dict) -> dict:
        return self._populate_missing(expected=Expected().result, actual=result)

    def _populate_missing_fastest_lap(self, fastest_lap: dict) -> dict:
        return self._populate_missing(
            expected=Expected().fastest_lap, actual=fastest_lap
        )

    def _populate_missing_average_speed(self, average_speed: dict) -> dict:
        return self._populate_missing(
            expected=Expected().average_speed, actual=average_speed
        )

    def _populate_missing_pit_stop(self, pit_stop: dict) -> dict:
        return self._populate_missing(expected=Expected().pit_stop, actual=pit_stop)

    def _populate_missing_lap(self, lap: dict) -> dict:
        return self._populate_missing(expected=Expected().lap, actual=lap)

    def _populate_missing_timing(self, timing: dict) -> dict:
        return self._populate_missing(expected=Expected().timing, actual=timing)

    def _populate_missing_season(self, season: dict) -> dict:
        return self._populate_missing(expected=Expected().season, actual=season)

    def _populate_missing_status(self, status: dict) -> dict:
        return self._populate_missing(expected=Expected().status, actual=status)

    def _populate_missing_driver_standing(self, standing: dict) -> dict:
        return self._populate_missing(
            expected=Expected().driver_standing, actual=standing
        )

    def _populate_missing_constructor_standing(self, standing: dict) -> dict:
        return self._populate_missing(
            expected=Expected().constructor_standing, actual=standing
        )

    def _populate_missing_standings_list(self, standings_list: dict) -> dict:
        return self._populate_missing(
            expected=Expected().standings_list, actual=standings_list
        )

    #
    #   PUBLIC METHODS
    #

    def construct_location(self, location: dict) -> Location:
        """
        Construct a Location from a JSON dictionary
        """
        location = self._populate_missing_location(location=location)
        return Location(
            latitude=float(location["lat"]),
            longitude=float(location["long"]),
            locality=location["locality"],
            country=location["country"],
        )

    def construct_circuit(self, circuit: dict) -> Circuit:
        """
        Construct a Circuit from a JSON dictionary
        """
        circuit = self._populate_missing_circuit(circuit)
        return Circuit(
            circuit_id=circuit["circuitId"],
            url=circuit["url"],
            circuit_name=circuit["circuitName"],
            location=self.construct_location(circuit["Location"]),
        )

    def construct_circuits(self, circuits: dict) -> list[Circuit]:
        """
        Construct a list of Circuits from a JSON dictionary
        """
        return [self.construct_circuit(circuit) for circuit in circuits]

    def construct_constructor(self, constructor: dict) -> Constructor:
        """
        Construct a Constructor from a JSON dictionary
        """
        constructor = self._populate_missing_constructor(constructor)
        return Constructor(
            constructor_id=constructor["constructorId"],
            url=constructor["url"],
            name=constructor["name"],
            nationality=constructor["nationality"],
        )

    def construct_constructors(self, constructors: dict) -> list[Constructor]:
        """
        Construct a list of Constructors from a JSON dictionary
        """
        return [self.construct_constructor(constructor) for constructor in constructors]

    def construct_driver(self, driver: dict) -> Driver:
        """
        Construct a Driver from a JSON dictionary
        """
        driver = self._populate_missing_driver(driver)
        return Driver(
            driver_id=driver["driverId"],
            permanent_number=int(driver["permanentNumber"]),
            code=driver["code"],
            url=driver["url"],
            given_name=driver["givenName"],
            family_name=driver["familyName"],
            date_of_birth=Helpers().construct_date(driver["dateOfBirth"]),
            nationality=driver["nationality"],
        )

    def construct_drivers(self, drivers: dict) -> list[Driver]:
        """
        Construct a list of Drivers from a JSON dictionary
        """
        return [self.construct_driver(driver) for driver in drivers]

    def construct_race(self, race: dict) -> Race:
        """
        Construct a Race from a JSON dictionary
        """
        race = self._populate_missing_race(race)

        try:
            sprint = Helpers().construct_datetime_dict(race["Sprint"])
        except ValueError:
            sprint = None

        return Race(
            season=int(race["season"]),
            round_no=int(race["round"]),
            url=race["url"],
            race_name=race["raceName"],
            circuit=self.construct_circuit(race["Circuit"]),
            date=Helpers().construct_datetime_str(date=race["date"], time=race["time"]),
            results=self.construct_results(race["Results"]),
            first_practice=Helpers().construct_datetime_dict(race["FirstPractice"]),
            second_practice=Helpers().construct_datetime_dict(race["SecondPractice"]),
            third_practice=Helpers().construct_datetime_dict(race["ThirdPractice"]),
            sprint=sprint,
            sprint_results=self.construct_results(race["SprintResults"]),
            qualifying=Helpers().construct_datetime_dict(race["Qualifying"]),
            qualifying_results=self.construct_results(race["QualifyingResults"]),
            pit_stops=self.construct_pit_stops(race["PitStops"]),
            laps=self.construct_laps(race["Laps"]),
        )

    def construct_races(self, races: dict) -> list[Race]:
        """
        Construct a list of Races from a JSON dictionary
        """
        return [self.construct_race(race) for race in races]

    def construct_result(self, result: dict) -> Result:
        """
        Construct a Result from a JSON dictionary
        """
        result = self._populate_missing_result(result)

        qualifying = {"Q1": None, "Q2": None, "Q3": None}
        for key in qualifying:
            try:
                qualifying[key] = Helpers().format_lap_time(time=result[key])
            except ValueError:
                # Warn that the value isn't present
                continue

        return Result(
            number=int(result["number"]),
            position=int(result["position"]),
            position_text=result["positionText"],
            points=float(result["points"]),
            driver=self.construct_driver(result["Driver"]),
            constructor=self.construct_constructor(result["Constructor"]),
            grid=int(result["grid"]),
            laps=int(result["laps"]),
            status=int(StatusType().string_to_id[result["status"]]),
            time=Helpers().construct_lap_time_millis(millis=result["Time"]),
            fastest_lap=self.construct_fastest_lap(result["FastestLap"]),
            qual_1=qualifying["Q1"],
            qual_2=qualifying["Q2"],
            qual_3=qualifying["Q3"],
        )

    def construct_results(self, results: dict) -> list[Result]:
        """
        Construct a list of Results from a JSON dictionary
        """
        return [self.construct_result(result) for result in results]

    def construct_fastest_lap(self, fastest_lap: dict) -> FastestLap:
        """
        Construct a FastestLap from a JSON dictionary
        """
        fastest_lap = self._populate_missing_fastest_lap(fastest_lap)
        return FastestLap(
            rank=int(fastest_lap["rank"]),
            lap=int(fastest_lap["lap"]),
            time=Helpers().construct_lap_time(time=fastest_lap["Time"]),
            average_speed=self.construct_average_speed(fastest_lap["AverageSpeed"]),
        )

    def construct_average_speed(self, average_speed: dict) -> AverageSpeed:
        """
        Construct an AverageSpeed from a JSON dictionary
        """
        average_speed = self._populate_missing_average_speed(average_speed)
        return AverageSpeed(
            units=average_speed["units"], speed=float(average_speed["speed"])
        )

    def construct_pit_stop(self, pit_stop: dict) -> PitStop:
        """
        Construct a PitStop from a JSON dictionary
        """
        pit_stop = self._populate_missing_pit_stop(pit_stop)
        return PitStop(
            driver_id=pit_stop["driverId"],
            lap=int(pit_stop["lap"]),
            stop=int(pit_stop["stop"]),
            local_time=Helpers().construct_local_time(pit_stop["time"]),
            duration=Helpers().construct_pitstop_duration(pit_stop["duration"]),
        )

    def construct_pit_stops(self, pit_stops: dict) -> list[PitStop]:
        """
        Construct a list of PitStops from a JSON dictionary
        """
        return [self.construct_pit_stop(pit_stop) for pit_stop in pit_stops]

    def construct_lap(self, lap: dict) -> Lap:
        """
        Construct a Lap from a JSON dictionary
        """
        lap = self._populate_missing_lap(lap)
        return Lap(
            number=int(lap["number"]), timings=self.construct_timings(lap["Timings"])
        )

    def construct_laps(self, laps: dict) -> list[Lap]:
        """
        Construct a list of Laps from a JSON dictionary
        """
        return [self.construct_lap(lap) for lap in laps]

    def construct_timing(self, timing: dict) -> Timing:
        """
        Construct a Timing from a JSON dictionary
        """
        timing = self._populate_missing_timing(timing)
        return Timing(
            driver_id=timing["driverId"],
            position=int(timing["position"]),
            time=Helpers().format_lap_time(time=timing["time"]),
        )

    def construct_timings(self, timings: dict) -> list[Timing]:
        """
        Construct a list of Timings from a JSON dictionary
        """
        return [self.construct_timing(timing) for timing in timings]

    def construct_season(self, season: dict) -> Season:
        """
        Construct a Season from a JSON dictionary
        """
        season = self._populate_missing_season(season)
        return Season(season=int(season["season"]), url=season["url"])

    def construct_seasons(self, seasons: dict) -> list[Season]:
        """
        Construct a list of Seasons from a JSON dictionary
        """
        return [self.construct_season(season) for season in seasons]

    def construct_status(self, status: dict) -> Status:
        """
        Construct a Status from a JSON dictionary
        """
        status = self._populate_missing_status(status)
        return Status(
            status_id=int(status["statusId"]),
            count=int(status["count"]),
            status=status["status"],
        )

    def construct_statuses(self, statuses: dict) -> list[Status]:
        """
        Construct a list of Statuses from a JSON dictionary
        """
        return [self.construct_status(status) for status in statuses]

    def construct_driver_standing(self, standing: dict) -> DriverStanding:
        """
        Construct a DriverStanding from a JSON dictionary
        """
        standing = self._populate_missing_driver_standing(standing)
        return DriverStanding(
            position=int(standing["position"]),
            position_text=standing["positionText"],
            points=float(standing["points"]),
            wins=int(standing["wins"]),
            driver=self.construct_driver(standing["Driver"]),
            constructors=self.construct_constructors(standing["Constructors"]),
        )

    def construct_driver_standings(self, standings: dict) -> list[DriverStanding]:
        """
        Construct a list of DriverStandings from a JSON dictionary
        """
        return [self.construct_driver_standing(standing) for standing in standings]

    def construct_constructor_standing(self, standing: dict) -> ConstructorStanding:
        """
        Construct a ConstructorStanding from a JSON dictionary
        """
        standing = self._populate_missing_constructor_standing(standing)
        return ConstructorStanding(
            position=int(standing["position"]),
            position_text=standing["positionText"],
            points=float(standing["points"]),
            wins=int(standing["wins"]),
            constructor=self.construct_constructor(standing["Constructor"]),
        )

    def construct_constructor_standings(
        self, standings: dict
    ) -> list[ConstructorStanding]:
        """
        Construct a list of ConstructorStandings from a JSON dictionary
        """
        return [self.construct_constructor_standing(standing) for standing in standings]

    def construct_standings_list(self, standings_list: dict) -> StandingsList:
        """
        Construct a StandingsList from a JSON dictionary
        """
        standings_list = self._populate_missing_standings_list(standings_list)
        return StandingsList(
            season=int(standings_list["season"]),
            round_no=int(standings_list["round"]),
            driver_standings=self.construct_driver_standings(
                standings_list["DriverStandings"]
            ),
            constructor_standings=self.construct_constructor_standings(
                standings_list["ConstructorStandings"]
            ),
        )

    def construct_standings_lists(self, standings_lists: dict) -> list[StandingsList]:
        """
        Construct a list of StandingsLists from a JSON dictionary
        """
        return [
            self.construct_standings_list(standings_list)
            for standings_list in standings_lists
        ]

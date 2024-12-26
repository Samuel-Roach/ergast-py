""" Expected class """
import datetime


class Expected:
    """
    Representations of the types expected to be found within a model.

    Each model has a set of keys, and the types expected.

    Types are stored as one of the following strings:
        * int
        * float
        * str
        * dict"""

    @property
    def location(self):
        """
        Return the expected types of a Location
        """
        return {
            "lat": float,
            "long": float,
            "locality": str,
            "country": str,
        }

    @property
    def circuit(self):
        """
        Return the expected types of a Circuit
        """
        return {
            "circuitId": str,
            "url": str,
            "circuitName": str,
            "Location": str,
        }

    @property
    def constructor(self):
        """
        Return the expected types of a Constructor
        """
        return {
            "constructorId": str,
            "url": str,
            "name": str,
            "nationality": str,
        }

    @property
    def driver(self):
        """
        Return the expected types of a Driver
        """
        return {
            "driverId": str,
            "permanentNumber": int,
            "code": str,
            "url": str,
            "givenName": str,
            "familyName": str,
            "dateOfBirth": str,
            "nationality": str,
        }

    @property
    def race(self):
        """
        Return the expected types of a Race
        """
        return {
            "season": int,
            "round": int,
            "url": str,
            "raceName": str,
            "Circuit": dict,
            "date": str,
            "time": str,
            "Results": dict,
            "FirstPractice": dict,
            "SecondPractice": dict,
            "ThirdPractice": dict,
            "Sprint": dict,
            "SprintResults": dict,
            "Qualifying": dict,
            "QualifyingResults": dict,
            "PitStops": dict,
            "Laps": dict,
        }

    @property
    def result(self):
        """
        Return the expected types of a Result
        """
        return {
            "number": int,
            "position": int,
            "positionText": str,
            "points": float,
            "Driver": dict,
            "Constructor": dict,
            "grid": int,
            "laps": int,
            "status": str,
            "Time": dict,
            "FastestLap": dict,
            "Q1": str,
            "Q2": str,
            "Q3": str,
        }

    @property
    def fastest_lap(self):
        """
        Return the expected types of a Fastest Lap
        """
        return {
            "rank": int,
            "lap": int,
            "Time": dict,
            "AverageSpeed": dict,
        }

    @property
    def average_speed(self):
        """
        Return the expected types of a Average Speed
        """
        return {
            "units": str,
            "speed": float,
        }

    @property
    def pit_stop(self):
        """
        Return the expected types of a Pit Stop
        """
        return {
            "driverId": str,
            "lap": int,
            "stop": int,
            "time": str,
            "duration": str,
        }

    @property
    def lap(self):
        """
        Return the expected types of a Lap
        """
        return {
            "number": int,
            "Timings": dict,
        }

    @property
    def timing(self):
        """
        Return the expected types of a Timing
        """
        return {
            "driverId": str,
            "position": int,
            "time": str,
        }

    @property
    def season(self):
        """
        Return the expected types of a Season
        """
        return {
            "season": int,
            "url": str,
        }

    @property
    def status(self):
        """
        Return the expected types of a Status
        """
        return {"statusId": int, "count": int, "status": str}

    @property
    def driver_standing(self):
        """
        Return the expected types of a Driver Standing
        """
        return {
            "position": int,
            "positionText": str,
            "points": float,
            "wins": int,
            "Driver": dict,
            "Constructors": dict,
        }

    @property
    def constructor_standing(self):
        """
        Return the expected types of a Constructor Standing
        """
        return {
            "position": int,
            "positionText": str,
            "points": float,
            "wins": int,
            "Constructor": dict,
        }

    @property
    def standings_list(self):
        """
        Return the expected types of a Standings List
        """
        return {
            "season": int,
            "round": int,
            "DriverStandings": dict,
            "ConstructorStandings": dict,
        }

    @property
    def time(self):
        """
        Return the expected types of a Time
        """
        return {
            "millis": datetime.time,
            "time": str,
        }

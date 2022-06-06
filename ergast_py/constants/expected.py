""" Expected class """

class Expected():
    """
    Representations of the types expected to be found within a model.

    Each model has a set of keys, and the types expected.

    Types are stored as one of the following strings:
        * "int"
        * "float"
        * "string"
        * "dict"
"""

    @property
    def location(self):
        """
        Return the expected types of a Location
        """
        return {
            "lat": "float",
            "long": "float",
            "locality": "string",
            "country": "string",
        }

    @property
    def circuit(self):
        """
        Return the expected types of a Circuit
        """
        return {
            "circuitId": "string",
            "url": "string",
            "circuitName": "string",
            "Location": "string",
        }

    @property
    def constructor(self):
        """
        Return the expected types of a Constructor
        """
        return {
            "constructorId": "string",
            "url": "string",
            "name": "string",
            "nationality": "string",
        }

    @property
    def driver(self):
        """
        Return the expected types of a Driver
        """
        return {
            "driverId": "string",
            "permanentNumber": "int",
            "code": "string",
            "url": "string",
            "givenName": "string",
            "familyName": "string",
            "dateOfBirth": "string",
            "nationality": "string",
        }

    @property
    def race(self):
        """
        Return the expected types of a Race
        """
        return {
            "season": "int",
            "round": "int",
            "url": "string",
            "raceName": "string",
            "Circuit": "dict",
            "date": "string",
            "time": "string",
            "Results": "dict",
            "FirstPractice": "dict",
            "SecondPractice": "dict",
            "ThirdPractice": "dict",
            "Sprint": "dict",
            "SprintResults": "dict",
            "Qualifying": "dict",
            "QualifyingResults": "dict",
            "PitStops": "dict",
            "Laps": "dict",
        }

    @property
    def result(self):
        """
        Return the expected types of a Result
        """
        return {
            "number": "int",
            "position": "int",
            "positionText": "string",
            "points": "float",
            "Driver": "dict",
            "Constructor": "dict",
            "grid": "int",
            "laps": "int",
            "status": "string",
            "Time": "dict",
            "FastestLap": "dict",
            "Q1": "string",
            "Q2": "string",
            "Q3": "string",
        }

    @property
    def fastest_lap(self):
        """
        Return the expected types of a Fastest Lap
        """
        return {
            "rank": "int",
            "lap": "int",
            "Time": "dict",
            "AverageSpeed": "dict",
        }

    @property
    def average_speed(self):
        """
        Return the expected types of a Average Speed
        """
        return {
            "units": "string",
            "speed": "float",
        }

    @property
    def pit_stop(self):
        """
        Return the expected types of a Pit Stop
        """
        return {
            "driverId": "string",
            "lap": "int",
            "stop": "int",
            "time": "string",
            "duration": "string",
        }

    @property
    def lap(self):
        """
        Return the expected types of a Lap
        """
        return {
            "number": "int",
            "Timings": "dict",
        }

    @property
    def timing(self):
        """
        Return the expected types of a Timing
        """
        return {
            "driverId": "string",
            "position": "int",
            "time": "string",
        }

    @property
    def season(self):
        """
        Return the expected types of a Season
        """
        return {
            "season": "int",
            "url": "string",
        }

    @property
    def status(self):
        """
        Return the expected types of a Status
        """
        return {
            "statusId": "int",
            "count": "int",
            "status": "string"
        }

    @property
    def driver_standing(self):
        """
        Return the expected types of a Driver Standing
        """
        return {
            "position": "int",
            "positionText": "string",
            "points": "float",
            "wins": "int",
            "Driver": "dict",
            "Constructors": "dict"
        }

    @property
    def constructor_standing(self):
        """
        Return the expected types of a Constructor Standing
        """
        return {
            "position": "int",
            "positionText": "string",
            "points": "float",
            "wins": "int",
            "Constructor": "dict"
        }

    @property
    def standings_list(self):
        """
        Return the expected types of a Standings List
        """
        return {
            "season": "int",
            "round": "int",
            "DriverStandings": "dict",
            "ConstructorStandings": "dict"
        }

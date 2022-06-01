class Expected():
    """
        Storage of the expected keys returned and their types
    """

    location = {
        "lat": "float",
        "long": "float",
        "locality": "string",
        "country": "string",
    }

    circuit = {
        "circuitId": "string",
        "url": "string",
        "circuitName": "string",
        "Location": "string",
    }

    constructor = {
        "constructorId": "string",
        "url": "string",
        "name": "string",
        "nationality": "string",
    }

    driver = {
        "driverId": "string",
        "permanentNumber": "int",
        "code": "string",
        "url": "string",
        "givenName": "string",
        "familyName": "string",
        "dateOfBirth": "string",
        "nationality": "string",
    }

    race = {
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

    result = {
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
    
    fastest_lap = {
        "rank": "int",
        "lap": "int",
        "Time": "dict",
        "AverageSpeed": "dict",
    }

    average_speed = {
        "units": "string",
        "speed": "float",
    }

    pit_stop = {
        "driverId": "string",
        "lap": "int",
        "stop": "int",
        "time": "string",
        "duration": "string",
    }

    lap = {
        "number": "int",
        "Timings": "dict",
    }

    timing = {
        "driverId": "string",
        "position": "int",
        "time": "string",
    }

    season = {
        "season": "int",
        "url": "string",
    }

    status = {
        "statusId": "int",
        "count": "int",
        "status": "string"
    }

    driver_standing = {
        "position": "int",
        "positionText": "string",
        "points": "float",
        "wins": "int",
        "Driver": "dict",
        "Constructors": "dict"
    }

    constructor_standing = {
        "position": "int",
        "positionText": "string",
        "points": "float",
        "wins": "int",
        "Constructor": "dict"
    }

    standings_list = {
        "season": "int",
        "round": "int",
        "DriverStandings": "dict",
        "ConstructorStandings": "dict"
    }
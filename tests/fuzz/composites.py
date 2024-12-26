"""Composites for Fuzz testing"""
import random

from hypothesis import provisional
from hypothesis import strategies

from ergast_py.constants import status_type


@strategies.composite
def location(draw):
    return {
        "lat": draw(strategies.floats(allow_nan=False)),
        "long": draw(strategies.floats(allow_nan=False)),
        "locality": draw(strategies.text()),
        "country": draw(strategies.text()),
    }


@strategies.composite
def circuit(draw):
    return {
        "circuitId": draw(strategies.text()),
        "url": draw(provisional.urls()),
        "circuit_name": draw(strategies.text()),
        "Location": draw(location()),
    }


@strategies.composite
def constructor(draw):
    return {
        "constructorId": draw(strategies.text()),
        "url": draw(provisional.urls()),
        "name": draw(strategies.text()),
        "nationality": draw(strategies.text()),
    }


@strategies.composite
def date_string(draw):
    date = draw(strategies.dates())
    return f"{date.year}-{date.month}-{date.day}"


@strategies.composite
def time_string(draw):
    time = draw(strategies.times())
    return f"{time.hour}:{time.minute}:{time.second}Z"


@strategies.composite
def date_time(draw):
    return {"date": draw(date_string()), "time": draw(time_string())}


@strategies.composite
def driver(draw):
    return {
        "driverId": draw(strategies.text()),
        "permanentNumber": draw(strategies.integers()),
        "code": draw(strategies.text()),
        "url": draw(provisional.urls()),
        "givenName": draw(strategies.text()),
        "familyName": draw(strategies.text()),
        "dateOfBirth": draw(date_string()),
        "nationality": draw(strategies.text()),
    }


def status():
    return random.choice(list(status_type.StatusType().string_to_id.keys()))


@strategies.composite
def time(draw):
    return {
        "millis": draw(strategies.integers()),
        "time": f"{draw(strategies.integers())}:{draw(strategies.integers())}:{draw(strategies.integers())}.{draw(strategies.integers())}",
    }


@strategies.composite
def fastest_lap_time(draw):
    return {
        "time": f"{draw(strategies.integers())}:{draw(strategies.integers())}.{draw(strategies.integers())}"
    }


@strategies.composite
def average_speed(draw):
    return {
        "units": draw(strategies.text()),
        "speed": draw(strategies.floats()),
    }


@strategies.composite
def fastest_lap(draw):
    return {
        "rank": draw(strategies.integers()),
        "lap": draw(strategies.integers()),
        "Time": draw(fastest_lap_time()),
        "AverageSpeed": draw(average_speed()),
    }


@strategies.composite
def result(draw):
    return {
        "number": draw(strategies.integers()),
        "position": draw(strategies.integers()),
        "positionText": draw(strategies.text()),
        "points": draw(strategies.integers()),
        "Driver": draw(driver()),
        "Constructor": draw(constructor()),
        "grid": draw(strategies.integers()),
        "laps": draw(strategies.integers()),
        "status": status(),
        "Time": draw(time()),
        "FastestLap": draw(fastest_lap()),
    }


@strategies.composite
def pit_stops(draw):
    time = draw(fastest_lap_time())
    res = {
        "driverId": draw(strategies.text()),
        "lap": draw(strategies.integers()),
        "stop": draw(strategies.integers()),
        "duration": f"{draw(strategies.integers())}.{draw(strategies.integers())}",
    }
    res.update(time)
    return res


@strategies.composite
def timing(draw):
    time = draw(fastest_lap_time())
    res = {
        "driverId": draw(strategies.text()),
        "position": draw(strategies.integers()),
    }
    res.update(time)
    return res


@strategies.composite
def lap(draw):
    return {
        "number": draw(strategies.integers()),
        "Timings": draw(strategies.lists(timing())),
    }


@strategies.composite
def laps(draw):
    return draw(strategies.lists(lap()))


@strategies.composite
def race(draw):
    return {
        "season": draw(strategies.integers()),
        "round": draw(strategies.integers()),
        "url": draw(provisional.urls()),
        "raceName": draw(strategies.text()),
        "Circuit": draw(circuit()),
        "date": draw(date_string()),
        "time": draw(time_string()),
        "Results": draw(result()),
        "FirstPractice": draw(date_time()),
        "SecondPractice": draw(date_time()),
        "ThirdPractice": draw(date_time()),
        "Sprint": draw(date_time()),
        "SprintResults": draw(result()),
        "Qualifying": draw(date_time()),
        "QualifyingResults": draw(result()),
        "PitStops": draw(pit_stops()),
        "Laps": draw(laps()),
    }

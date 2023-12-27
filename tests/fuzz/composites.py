"""Composites for Fuzz testing"""
from hypothesis import provisional
from hypothesis import strategies


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


@strategies.composite
def race(draw):
    return {}

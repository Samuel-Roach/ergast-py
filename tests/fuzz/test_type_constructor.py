import composites
from hypothesis import given

from ergast_py.helpers import Helpers
from ergast_py.models import circuit
from ergast_py.models import constructor
from ergast_py.models import driver
from ergast_py.models import location
from ergast_py.models import race
from ergast_py.type_constructor import TypeConstructor


class TestFuzzTypeConstructor:
    t = TypeConstructor()

    @given(
        fuzz=composites.location(),
    )
    def test_construct_location(self, fuzz):
        result = self.t.construct_location(location=fuzz)

        expected = location.Location(
            latitude=fuzz["lat"],
            longitude=fuzz["long"],
            locality=fuzz["locality"],
            country=fuzz["country"],
        )

        assert result == expected

    @given(fuzz=composites.circuit())
    def test_construct_circuit(self, fuzz):
        result = self.t.construct_circuit(circuit=fuzz)

        expected = circuit.Circuit(
            circuit_id=fuzz["circuitId"],
            url=fuzz["url"],
            circuit_name=fuzz["circuitName"],
            location=self.t.construct_location(fuzz["Location"]),
        )

        assert result == expected

    @given(fuzz=composites.constructor())
    def test_construct_constructor(self, fuzz):
        result = self.t.construct_constructor(constructor=fuzz)

        expected = constructor.Constructor(
            constructor_id=fuzz["constructorId"],
            url=fuzz["url"],
            name=fuzz["name"],
            nationality=fuzz["nationality"],
        )

        assert result == expected

    @given(fuzz=composites.driver())
    def test_construct_driver(self, fuzz):
        result = self.t.construct_driver(driver=fuzz)

        expected = driver.Driver(
            driver_id=fuzz["driverId"],
            permanent_number=fuzz["permanentNumber"],
            code=fuzz["code"],
            url=fuzz["url"],
            given_name=fuzz["givenName"],
            family_name=fuzz["familyName"],
            date_of_birth=Helpers().construct_date(fuzz["dateOfBirth"]),
            nationality=fuzz["nationality"],
        )

        assert result == expected


# TODO Finish adding race fuzz set. Currently it takes too long to run.
# @given(fuzz=composites.race())
# def test_construct_race(self, fuzz):
#     result = self.t.construct_race(race=fuzz)
#     expected = race.Race(
#     )

#     assert result == expected

"""
Ergast API Python Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~

A comprehensive Python wrapper for the Ergast Formula One API

Basic usage:

    >>> import ergast_py
    >>> e = ergast_py.Ergast()
    >>> e.driver("alonso").get_driver()
    Driver(
        driverId=alonso,
        permanentNumber=14,
        code=ALO,
        url=http://en.wikipedia.org/wiki/Fernando_Alonso,
        givenName=Fernando,
        familyName=Alonso,
        dateOfBirth=1981-07-29,
        nationality=Spanish)

Full documentation can be found at https://github.com/Samuel-Roach/ergast-py.

Ergast-py extends the publicly available and free Ergast API. For more information
and a better understanding visit http://ergast.com/mrd/

"""

from ergast_py.ergast import Ergast
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

__version__ = '0.6.0'

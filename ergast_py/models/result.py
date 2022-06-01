from dataclasses import dataclass
import datetime
from ergast_py.models.constructor import Constructor

from ergast_py.models.driver import Driver
from ergast_py.models.fastest_lap import FastestLap

@dataclass
class Result:
    """
    Representation of a single Result from a Formula One race
    Results may contain:
        number: Integer
        position: Integer
        positionText: String
        points: Integer
        driver: Driver
        constructor: Constructor
        grid: Integer
        laps: Integer
        status: Integer
        time: datetime.time
        fastestLap: FastestLap
        q1: datetime.time
        q2: datetime.time
        q3: datetime.time
    """

    def __init__(self, number: int, position: int, positionText: str, points: float, driver: Driver,
                 constructor: Constructor, grid: int, laps: int, status: int, time: datetime.time,
                 fastestLap: FastestLap, q1: datetime.time, q2: datetime.time, q3: datetime.time) -> None:
        self.number = number
        self.position = position
        self.positionText = positionText
        self.points = points
        self.driver = driver
        self.constructor = constructor
        self.grid = grid
        self.laps = laps
        self.status = status
        self.time = time
        self.fastestLap = fastestLap
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        pass

    def __str__(self):
        return f"Result(number={self.number}, position={self.position}, positionText={self.positionText}, points={self.points}, driver={self.driver}, constructor={self.constructor}, grid={self.grid}, laps={self.laps}, status={self.status}, time={self.time}, fastestLap={self.fastestLap}, q1={self.q1}, q2={self.q2}, q3={self.q3})"

    def __repr__(self):
        return f"Result(number={self.number}, position={self.position}, positionText={self.positionText}, points={self.points}, driver={self.driver}, constructor={self.constructor}, grid={self.grid}, laps={self.laps}, status={self.status}, time={self.time}, fastestLap={self.fastestLap}, q1={self.q1}, q2={self.q2}, q3={self.q3})"

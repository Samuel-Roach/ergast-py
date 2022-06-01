from dataclasses import dataclass
from ergast_py.models.average_speed import AverageSpeed
import datetime

@dataclass
class FastestLap:
    """
    Representation of a Fastest Lap for a Formula One Driver
    Fastest Laps may contain:
        rank: Integer
        lap: Integer
        time: datetime.time
        averageSpeed: AverageSpeed
    """

    def __init__(self, rank: int, lap: int, time: datetime.time, averageSpeed: AverageSpeed) -> None:
        self.rank = rank
        self.lap = lap
        self.time = time
        self.averageSpeed = averageSpeed
        pass

    def __str__(self):
        return f"FastestLap(rank={self.rank}, lap={self.lap}, time={self.time}, averageSpeed={self.averageSpeed})"

    def __repr__(self):
        return f"FastestLap(rank={self.rank}, lap={self.lap}, time={self.time}, averageSpeed={self.averageSpeed})"
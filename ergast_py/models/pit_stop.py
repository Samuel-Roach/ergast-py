from dataclasses import dataclass
import datetime

@dataclass
class PitStop:
    """
    Representation of a single Pit Stop from a Formula One race
    PitStops may contain:
        driverId: String
        lap: Integer
        stop: Integer
        localTime: datetime.datetime
        duration: datetime.time
    """

    def __init__(self, driverId: str, lap: int, stop: int, localTime: datetime.datetime,
                 duration: datetime.time) -> None:
        self.driverId = driverId
        self.lap = lap
        self.stop = stop
        self.localTime = localTime
        self.duration = duration
        pass

    def __str__(self):
        return f"PitStop(driverId={self.driverId}, lap={self.lap}, stop={self.stop}, localTime={self.localTime}, duration={self.duration})"

    def __repr__(self):
        return f"PitStop(driverId={self.driverId}, lap={self.lap}, stop={self.stop}, localTime={self.localTime}, duration={self.duration})"
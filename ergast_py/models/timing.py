from dataclasses import dataclass
import datetime

@dataclass
class Timing:
    """
    Representation of a single timing from a lap in Formula One
    Timings may contain:
        driverId: String
        position: Integer
        time: datetime.time
    """

    def __init__(self, driverId: str, position: int, time: datetime.time) -> None:
        self.driverId = driverId
        self.position = position
        self.time = time
        pass

    def __str__(self):
        return f"Timing(driverId={self.driverId}, position={self.position}, time={self.time})"

    def __repr__(self):
        return f"Timing(driverId={self.driverId}, position={self.position}, time={self.time})"
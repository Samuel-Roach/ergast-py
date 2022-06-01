from dataclasses import dataclass

@dataclass
class AverageSpeed:
    """
    Representation of a Drivers Average Speed
    Average Speeds may contain:
        units: String
        speed: Float
    """

    def __init__(self, units: str, speed: float) -> None:
        self.units = units
        self.speed = speed
        pass

    def __str__(self):
        return f"AverageSpeed(units={self.units}, speed={self.speed})"

    def __repr__(self):
        return f"AverageSpeed(units={self.units}, speed={self.speed})"
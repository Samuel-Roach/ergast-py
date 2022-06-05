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

    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
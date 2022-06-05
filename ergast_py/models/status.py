from dataclasses import dataclass

@dataclass
class Status:
    """
    Representation of the finishing status of a Driver in a Race
    Statuses may contain:
        statusId: Integer
        count: Integer
        status: String
    """

    def __init__(self, statusId: int, count: int, status: str) -> None:
        self.statusId = statusId
        self.count = count
        self.status = status
        pass
    
    def __str__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"
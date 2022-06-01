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
    
    def __str__(self):
        return f"Status(statusId={self.statusId}, count={self.count}, status={self.status})"

    def __repr__(self):
        return f"Status(statusId={self.statusId}, count={self.count}, status={self.status})"
""" Status class """

from dataclasses import dataclass


@dataclass
class Status():
    """
    Representation of the finishing status of a Driver in a Race

    Statuses may contain:
        status_id: Integer
        count: Integer
        status: String
    """

    status_id: int
    count: int
    status: str

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Status) and (
            self.status_id == __o.status_id and
            self.count == __o.count and
            self.status == __o.status
        )

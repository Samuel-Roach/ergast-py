""" Season class """

from dataclasses import dataclass


@dataclass
class Season():
    """
    Representation of a single Season in Formula One

    Seasons may contain:
        season: Integer
        url: String
    """

    season: int
    url: str

    def __repr__(self) -> str:
        members = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({members})"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Season) and (
            self.season == __o.season and
            self.url == __o.url
        )

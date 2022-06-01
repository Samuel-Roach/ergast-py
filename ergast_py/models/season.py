from dataclasses import dataclass

@dataclass
class Season:
    """
    Representation of a single Season in Formula One
    Seasons may contain:
        season: Integer
        url: String
    """

    def __init__(self, season: int, url: str) -> None:
        self.season = season
        self.url = url
        pass

    def __str__(self):
        return f"Season(season={self.season}, url={self.url})"

    def __repr__(self):
        return f"Season(season={self.season}, url={self.url})"
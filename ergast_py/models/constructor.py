from dataclasses import dataclass

@dataclass
class Constructor:
    """
    Representation of a Formula One Team
    Constructors may contain:
        constructorId: String
        url: String
        name: String
        nationality: String
    """

    def __init__(self, constructorId: str, url: str, name: str, nationality: str) -> None:
        self.constructorId = constructorId
        self.url = url
        self.name = name
        self.nationality = nationality
        pass

    def __str__(self):
        return f"Constructor(constructorId={self.constructorId}, url={self.url}, name={self.name}, nationality={self.nationality})"

    def __repr__(self):
        return f"Constructor(constructorId={self.constructorId}, url={self.url}, name={self.name}, nationality={self.nationality})"
""" Constructor class """

from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class Constructor(BaseModel):
    """
    Representation of a Formula One Team

    Constructors may contain:
        constructor_id: String
        url: String
        name: String
        nationality: String
    """

    constructor_id: str
    url: str
    name: str
    nationality: str

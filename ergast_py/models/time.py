""" Time class """
import datetime
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class Time(BaseModel):
    """
    Representation of a Finishing Time in a Race for a Formula One Driver

    Time may contain:
        millis: datetime.time
        time: String
    """

    millis: datetime.time
    time: str

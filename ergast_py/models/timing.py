""" Timing class """

import datetime
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class Timing(BaseModel):
    """
    Representation of a single timing from a lap in Formula One
    Timings may contain:
        driver_id: String
        position: Integer
        time: datetime.time
    """

    driver_id: str
    position: int
    time: datetime.time

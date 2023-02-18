""" PitStop class """

import datetime
from dataclasses import dataclass

from ergast_py.models.base_model import BaseModel


@dataclass
class PitStop(BaseModel):
    """
    Representation of a single Pit Stop from a Formula One race

    PitStops may contain:
        driver_id: String
        lap: Integer
        stop: Integer
        local_time: datetime.time
        duration: datetime.time
    """

    driver_id: str
    lap: int
    stop: int
    local_time: datetime.time
    duration: datetime.time

""" Helpers class """

import datetime
import pytz


class Helpers:
    """
    Helpers for the construction of models
    """

    @staticmethod
    def construct_datetime_str(date: str, time: str) -> datetime.datetime:
        """
        Construct a datetime.datetime from the date and time strings.

        Looking for the format of ``%Y-%m-%d %H:%M:%SZ``
        """

        if not time.strip():
            time = "00:00:00Z"

        new_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%SZ")
        new_datetime = new_datetime.replace(tzinfo=datetime.timezone.utc)
        return new_datetime

    def construct_datetime_dict(self, datetime_dict: dict) -> datetime.datetime:
        """
        Construct a datetime.datetime from a dictionary.

        Dictionary should contain the keys "date" and "time"
        """
        if "date" not in datetime_dict or "time" not in datetime_dict:
            raise ValueError("Dictionary must contain keys 'date' and 'time'")
        return self.construct_datetime_str(datetime_dict["date"], datetime_dict["time"])

    @staticmethod
    def construct_date(date: str) -> datetime.date:
        """
        Construct a datetime.date from a date string
        """
        elements = date.split("-")
        return datetime.date(
            year=int(elements[0]), month=int(elements[1]), day=int(elements[2])
        )

    @staticmethod
    def construct_lap_time_millis(millis: dict) -> datetime.time:
        """
        Construct a datetime.time (lap time) from a dict containing the millis
        """
        if "millis" in millis:
            value = int(millis["millis"])
            return datetime.datetime.fromtimestamp(value / 1000.0).time()
        raise ValueError("Dictionary must contain key 'millis'")

    @staticmethod
    def format_lap_time(time: str) -> datetime.time:
        """
        Construct a datetime.time (lap time) from a time string
        """
        if time != "":
            return datetime.datetime.strptime(time, "%M:%S.%f").time()
        raise ValueError("Time string cannot be empty")

    def construct_lap_time(self, time: dict) -> datetime.time:
        """
        Construct a datetime.time (lap time) from a time dictionary

        The dictionary should contain the key "time"
        """
        if "time" in time:
            value = time["time"]
            return self.format_lap_time(value)
        raise ValueError("Dictionary must contain key 'time'")

    @staticmethod
    def construct_local_time(time: str) -> datetime.time:
        """
        Construct a datetime.time from a time string

        Looking for the format of ``%H:%M:%S``
        """
        if time != "":
            return datetime.datetime.strptime(f"{time}", "%H:%M:%S").time()
        raise ValueError("Time string cannot be empty")

    @staticmethod
    def construct_pitstop_duration(time: str) -> datetime.time:
        """
        Construct a datetime.time (pit stop duration) from a time string

        Looking for the format of ``%S.%f``
        """
        if time != "":
            return datetime.datetime.strptime(f"{time}", "%S.%f").time()
        raise ValueError("Time string cannot be empty")

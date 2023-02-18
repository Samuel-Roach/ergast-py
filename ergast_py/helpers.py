""" Helpers class """

import datetime


class Helpers:
    """
    Helpers for the construction of models
    """

    def construct_datetime_str(self, date: str, time: str) -> datetime.datetime:
        """
        Construct a datetime.datetime from the date and time strings.

        Looking for the format of ``%Y-%m-%d %H:%M:%SZ``
        """
        new_datetime = datetime.datetime.strptime(
            f"{date} {time}", "%Y-%m-%d %H:%M:%SZ"
        )
        new_datetime = new_datetime.replace(tzinfo=datetime.timezone.utc)
        return new_datetime

    def construct_datetime_dict(self, datetime_dict: dict) -> datetime.datetime:
        """
        Construct a datetime.datetime from a dictionary.

        Dictionary should contain the keys "date" and "time"
        """
        if "date" not in datetime_dict or "time" not in datetime_dict:
            return None
        return self.construct_datetime_str(datetime_dict["date"], datetime_dict["time"])

    def construct_date(self, date: str) -> datetime.date:
        """
        Construct a datetime.date from a date string
        """
        elements = date.split("-")
        return datetime.date(
            year=int(elements[0]), month=int(elements[1]), day=int(elements[2])
        )

    def construct_lap_time_millis(self, millis: dict) -> datetime.time:
        """
        Construct a datetime.time (lap time) from a dict containing the millis
        """
        if "millis" in millis:
            value = int(millis["millis"])
            return datetime.datetime.fromtimestamp(value / 1000.0).time()
        return None

    def format_lap_time(self, time: str) -> datetime.time:
        """
        Construct a datetime.time (lap time) from a time string
        """
        if time != "":
            return datetime.datetime.strptime(time, "%M:%S.%f").time()
        return None

    def construct_lap_time(self, time: dict) -> datetime.time:
        """
        Construct a datetime.time (lap time) from a time dictionary

        The dictionary should contain the key "time"
        """
        if "time" in time:
            value = time["time"]
            return self.format_lap_time(value)
        return None

    def construct_local_time(self, time: str) -> datetime.time:
        """
        Construct a datetime.time from a time string

        Looking for the format of ``%H:%M:%S``
        """
        if time != "":
            return datetime.datetime.strptime(f"{time}", "%H:%M:%S").time()
        return None

    def construct_pitstop_duration(self, time: str) -> datetime.time:
        """
        Construct a datetime.time (pit stop duration) from a time string

        Looking for the format of ``%S.%f``
        """
        if time != "":
            return datetime.datetime.strptime(f"{time}", "%S.%f").time()
        return None

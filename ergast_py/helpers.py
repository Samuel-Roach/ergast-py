import datetime


class Helpers:
    def construct_datetime_str(self, date: str, time: str) -> datetime.datetime:
        new_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%SZ")
        new_datetime = new_datetime.replace(tzinfo=datetime.timezone.utc)
        return new_datetime

    def construct_datetime_dict(self, dict: dict) -> datetime.datetime:
        if "date" not in dict or "time" not in dict:
            return None
        return self.construct_datetime_str(dict["date"], dict["time"])

    def construct_date(self, date: str) -> datetime.date:
        elements = date.split("-")
        return datetime.date(year=int(elements[0]), month=int(elements[1]), day=int(elements[2]))

    def construct_lap_time_millis(self, millis: dict) -> datetime.time:
        if "millis" in millis:
            value = int(millis["millis"])
            return datetime.datetime.fromtimestamp(value/1000.0).time()
        return None

    def format_lap_time(self, time: str) -> datetime.time:
        if time != "":
            return datetime.datetime.strptime(time, "%M:%S.%f").time()
        return None

    def construct_lap_time(self, time: dict) -> datetime.time:
        if "time" in time:
            value = time["time"]
            return self.format_lap_time(value)
        return None

    def construct_local_time(self, time: str) -> datetime.time:
        if "time" != "":
            return datetime.datetime.strptime(f"{time}", "%H:%M:%S").time()
        return None

    def construct_pitstop_duration(self, time: str) -> datetime.time:
        if "time" != "":
            return datetime.datetime.strptime(f"{time}", "%S.%f").time()
        return None

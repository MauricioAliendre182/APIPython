from datetime import datetime, timezone


class DateGenerator:
    _date = None

    @staticmethod
    def generateDateInIso8601Format():
        _date = datetime.now(timezone.utc)
        iso_format = _date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        date_str = str(iso_format)
        return date_str

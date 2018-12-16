import datetime as _datetime
from .date import date
from .time_only import time_only


def datetime(input_datetime):

    # Return if the type isn't correct
    if type(input_datetime) is not _datetime.datetime:
        raise TypeError("Argument is not of type datetime.datetime")

    result = date(input_datetime)
    result += time_only(input_datetime)

    return result

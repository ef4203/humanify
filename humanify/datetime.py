import datetime as _datetime
from .date import date
from .time_only import time_only


def datetime(input_datetime):
    """Returns human readable string of both date and time.

    Parameters:
                input_datetime (datetime.datetime object): datetime object from standare datetime module

    Returns:
            result (str): human readable date and time.
    """

    if type(input_datetime) is not _datetime.datetime:
        raise TypeError("Argument is not of type datetime.datetime")

    result = date(input_datetime)
    result += time_only(input_datetime)

    return result

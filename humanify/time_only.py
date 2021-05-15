import datetime as _datetime


def time_only(input_datetime):
    """Returns human readable string of time.

    Parameters:
                input_datetime (datetime.datetime object): datetime object from standare datetime module

    Returns:
            result (str): human readable time
    """

    if type(input_datetime) is not _datetime.datetime:
        raise TypeError("Argument is not of type datetime.datetime")

    if input_datetime.hour < 10:
        result = "0" + str(input_datetime.hour) + ":"
    else:
        result = str(input_datetime.hour) + ":"

    if input_datetime.minute < 10:
        result += "0" + str(input_datetime.minute) + ":"
    else:
        result += str(input_datetime.minute) + ":"

    if input_datetime.second < 10:
        result += "0" + str(input_datetime.second)
    else:
        result += str(input_datetime.second)

    return result

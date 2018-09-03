import datetime as _datetime


def time_only(input_datetime):

    # Return if the type isn't correct
    if type(input_datetime) is not _datetime.datetime:
        raise TypeError("Argument is not of type datetime.datetime")
        return None

    if input_datetime.hour < 10:
        result = '0' + str(input_datetime.hour) + ':'
    else:
        result = str(input_datetime.hour) + ':'

    result += str(input_datetime.minute) + ':'

    if input_datetime.second < 10:
        result += '0' + str(input_datetime.second)
    else:
        result += str(input_datetime.second)

    return result

import datetime as _datetime

WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

ORDINALS = ["st", "nd", "rd", "th"]


def date(input_datetime):
    """Returns human readable string of date.

    Parameters:
                input_datetime (datetime.datetime object): datetime object from standare datetime module

    Returns:
            result (str): human readable date
    """

    if type(input_datetime) is not _datetime.datetime:
        raise TypeError("Argument is not of type datetime.datetime")

    result = str(WEEKDAYS[input_datetime.weekday()]) + ", "

    # Determine ordinal sign for the dates day
    if input_datetime.day == 1 or input_datetime.day == 21 or input_datetime == 31:
        result += str(input_datetime.day) + ORDINALS[0]  # st-ending

    elif input_datetime.day == 2 or input_datetime.day == 22:
        result += str(input_datetime.day) + ORDINALS[1]  # nd-ending

    elif input_datetime.day == 3 or input_datetime.day == 23:
        result += str(input_datetime.day) + ORDINALS[2]  # rd-edning

    else:
        result += str(input_datetime.day) + ORDINALS[3]  # th-ending

    result += " of "
    result += MONTHS[input_datetime.month - 1] + " "
    result += str(input_datetime.year) + " "

    return result

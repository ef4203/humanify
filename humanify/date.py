import datetime as _datetime

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

ordinals = [
    'st',
    'nd',
    'rd',
    'th'
]

def date(input_datetime):

    # Return if the type isn't correct
    if type(input_datetime) is not _datetime.datetime:
        raise TypeError("Argument is not of type datetime.datetime")
        return None

    # Determine day of the week
    result = str(weekdays[input_datetime.weekday()]) + ', '

    # Determine ordinal sign for the dates day
    if input_datetime.day == 1 or input_datetime.day == 21 or input_datetime == 31:
        result += str(input_datetime.day) + ordinals[0]  # st-ending

    elif input_datetime.day == 2 or input_datetime.day == 22:
        result += str(input_datetime.day) + ordinals[1]  # nd-ending

    elif input_datetime.day == 3 or input_datetime.day == 23:
        result += str(input_datetime.day) + ordinals[2]  # rd-edning

    else:
        result += str(input_datetime.day) + ordinals[3]  # th-ending

    result += ' of '
    result += months[input_datetime.month] + ' '
    result += str(input_datetime.year) + ' '

    return result

def get_percentage(number, precision=None):
    if precision is None:
        percent = int(number * 100)
    else:
        percent = round(number * 100, precision)
    return f"{percent}%"


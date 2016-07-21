import datetime

def add_gigasecond(date):
    gigasecond = date + datetime.timedelta(seconds = 10 ** 9)
    return gigasecond

from datetime import datetime
from dateutil.relativedelta import relativedelta


def age_checker(string):
    try:
        date = datetime.strptime(string, "%Y-%m-%d")
    except:
        raise Exception("Incorrect format (yyyy-mm-dd)")
    date_now = datetime.now()
    difference = relativedelta(date_now, date)
    print("date", date)
    if difference.years >= 16:
        return "Access granted"
    else:
        return "Access denied"

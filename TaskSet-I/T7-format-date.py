import datetime


def format_date(date):
    today = datetime.date.today()

    # get the day of the month
    day, month, year = map(int, date.split("-"))

    # get ordinal suffix
    suffix = "th"
    if day == 1 or day == 21 or day == 31:
        suffix = "st"
    elif day == 2 or day == 22:
        suffix = "nd"
    elif day == 3 or day == 23:
        suffix = "rd"

    date = datetime.datetime(year, month, day)

    print("{}{} {}".format(day, suffix, date.strftime("%b %Y")))


format_date("09-10-2021")

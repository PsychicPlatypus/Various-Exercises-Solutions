from datetime import datetime


def count_days(d) -> str():
    todays_date = datetime.today()
    to_seconds = (
        ((todays_date.year * 365) + todays_date.year // 4)
        + todays_date.month * 12
        + todays_date.day
    )
    difference = (((d.year * 365) + d.year // 4) + d.month * 12 + d.day) - to_seconds
    print(difference)
    if difference > 0:
        return f"{difference} days"
    return "Today is the day!" if difference == 0 else "The day is in the past!"


print(count_days(datetime.today()))

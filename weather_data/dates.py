from datetime import datetime
from translations import weekday_convert, month_convert


def date_today():
    weekday = weekday_convert(datetime.today().isoweekday())
    the_date = str(datetime.now().date())[8:10]
    month = month_convert(datetime.today().month)
    year = datetime.today().year
    return f"{weekday}, {the_date}. {month} {year}"


print(date_today())
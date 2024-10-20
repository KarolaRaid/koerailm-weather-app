from datetime import datetime
from weather_data.translations import weekday_convert, month_convert


def date_today():
    weekday = weekday_convert(datetime.today().isoweekday())
    the_date = str(datetime.now().date())[8:10]
    month = month_convert(datetime.today().month)
    return f"{weekday}, {the_date}. {month}"

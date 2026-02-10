# __Challenge__

# Write a code to find the day of the week of a given date.

from datetime import datetime

given_date = datetime(2020, 7, 26)

day_name = datetime.strftime(given_date, "%A")

print(f"Day is {day_name}")
print(f"Day is {given_date.today().weekday()}") # print weekday as integer.

# __Method Two__

import calendar

print(calendar.day_name[given_date.weekday()])


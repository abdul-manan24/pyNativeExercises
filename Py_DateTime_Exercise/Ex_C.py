# __Challenge__

# Write a code to subtract a week (7 days) from a given date.

from datetime import datetime
from datetime import timedelta

given_date = datetime(2020, 2, 25)
date_to_minus = datetime(days=7)

timedelta = given_date - date_to_minus

print("Given Date {timedelta}")
print("New Date {new_date}")
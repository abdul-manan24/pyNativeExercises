# __Challenge__

# Write a code to subtract a week (7 days) from a given date.

from datetime import datetime
from datetime import timedelta

given_date = datetime(2020, 2, 25)

new_date = given_date - timedelta(days=7)

print(f"Given Date {given_date}")
print(f"New Date {new_date}")
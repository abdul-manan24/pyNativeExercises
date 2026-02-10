# __Challenge__

# Write a code to convert a given datetime object into a string.

from datetime import datetime

given_date = datetime(2020, 2, 25)

Date = datetime.strftime(given_date, "%Y-%m-%d %H:%M:%S")

print(Date)
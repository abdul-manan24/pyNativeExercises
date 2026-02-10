# __Challenge__

# Write a code to convert the given date in string format into a Python DateTime object.
from datetime import datetime

date_string = "Feb 25 2020 4:20PM"

datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')

print(datetime_object)

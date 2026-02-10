# __Challenge__

# Format DateTime.
from datetime import datetime

given_date = datetime(2020, 2, 25)

formated_date = datetime.strftime(given_date, "%A %d %B %Y")

print(formated_date)

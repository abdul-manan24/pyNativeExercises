# __Challenge__

# Calculate Days Between Two Dates.

from datetime import datetime

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

days = abs(date_1 - date_2)

print(days.days, "Days")
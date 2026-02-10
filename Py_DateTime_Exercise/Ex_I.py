# __Challenge__

#  Calculate the date 4 months from the current date.

from datetime import datetime
from dateutil.relativedelta import relativedelta, MO

given_date = datetime(2020, 2, 25).date()

future = given_date + relativedelta(months=4)

print(future)

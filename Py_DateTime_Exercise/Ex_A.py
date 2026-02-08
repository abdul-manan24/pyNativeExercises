# __Challenge__

# Print Current Date and Time.

# import datetime

# print(datetime.datetime.now())

from datetime import datetime, date

# Get current date and time as a datetime object
now = datetime.now()

# Extract only the date part
current_date = now.date()
print(f"Current Date: {current_date}")

# Extract only the time part
current_time = now.time()
print(f"Current Time: {current_time}")

# Alternatively, a dedicated function for today's date
today = date.today()
print(f"Today's date: {today}")

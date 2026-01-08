import time
# __Challenge__

# Write a code to create a simple countdown timer of 5 seconds using a while loop.
# Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.

i = 5
while (i > 0):
    print("Time remaining:", i, "seconds")
    time.sleep(1)
    i -= 1

print("Time's up!")
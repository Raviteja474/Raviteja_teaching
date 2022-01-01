from datetime import *
import time

# 19@@ on which date this test ran
my_date = date(2021, 9, 1)
print(f"This test developed on:{my_date}")

today = date.today()
print(f"This test ran on: {today}")
print(type(today))

print(f"This test ran on: year: {today.year} month: {today.month}, date: {today.day}")

Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))

# The timestamp is the number of seconds from 1st January 1970 at UTC to a particular date.
date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)

string = "Tue, 03 Aug 2021 10:45:08"
obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")
print(obj)

now = datetime.now()
print("Without formatting", now)

# Example 1
s = now.strftime("%A %m %-Y")
print('\nExample 1:', s)

# Example 2
s = now.strftime("%a %-m %y")
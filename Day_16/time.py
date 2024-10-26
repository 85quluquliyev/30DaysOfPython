"""
import datetime
print(dir(datetime))
"""
"""
from datetime import datetime
now = datetime.now()
print(now)  
day = now.day
print(day) 
month = now.month
print(month)
year = now.year
print(year)
hour = now.hour
print(hour)
minute = now.minute
print(minute)
second = now.second
print(second)
timestamp = now.timestamp()
print(timestamp)
print(f'{day}/{month}/{year},{hour}:{minute}')
"""

"""
from datetime import datetime
new_year = datetime(2020,1,1)
print(new_year)
"""
"""
from datetime import datetime
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time:', t)
"""
"""
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today()) 
today = date.today()
print(today.day)
"""
"""
from datetime import time
a = time()
print("a =", a)
b = time(10, 30, 50)
print("b =", b)
"""
"""
from datetime import date,datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)
"""
"""
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
"""

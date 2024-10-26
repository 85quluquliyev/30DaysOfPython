# Ex1
from datetime import datetime, date

now = datetime.now()
print(now)

day = now.day
print(day)

# Ex2
t = now.strftime('%d %b')
print(t)

# Ex3
string_time = '5 December,2019'
time = datetime.strptime(string_time, '%d %B,%Y')
print(time)

# Ex4
today = date(year=2024, month=10, day=26)
new_year = date(year=2025, month=1, day=1)
diff = new_year - today
print(diff)
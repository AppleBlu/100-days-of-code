import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
print(year)
month = now.month
print(month)
day_of_the_week = now.weekday()
print(day_of_the_week)

date_of_birth = dt.datetime(year=2001, month=12, day=23)
print(date_of_birth)

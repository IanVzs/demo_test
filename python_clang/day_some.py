import time
import datetime

today = datetime.datetime.today()

# datetime->str
today_str = today.strftime("%Y-%m-%d")

# str->datetime
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
print(f"year: {today.year}, month: {today.month}, day: {today.day}")

# unixInt->datetime
utoday = time.mktime(today.timetuple())
utoday_str = time.strftime('%Y-%m-%d',time.localtime(utoday))
print(today, today_str, utoday, utoday_str)

# datetime->unixInt
uintnnum = time.mktime(today.timetuple())
print('uintnnum:', uintnnum)

ttoday = datetime.datetime.today() + datetime.timedelta(days=1)
ttoday_str = ttoday.strftime("%Y-%m-%d")
print(ttoday, ttoday_str)

utoday_str = time.strftime('%Y-%m-%d',time.localtime(1590042205))



to_s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"nyrsfm: {to_s}")

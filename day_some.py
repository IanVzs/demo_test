import time
import datetime

today = datetime.datetime.today()
today_str = today.strftime("%Y-%m-%d")
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
utoday = time.mktime(today.timetuple())
utoday_str = time.strftime('%Y-%m-%d',time.localtime(utoday))

print(today, today_str, utoday, utoday_str)

ttoday = datetime.datetime.today() + datetime.timedelta(days=1)
ttoday_str = ttoday.strftime("%Y-%m-%d")
print(ttoday, ttoday_str)

utoday_str = time.strftime('%Y-%m-%d',time.localtime(1590042205))


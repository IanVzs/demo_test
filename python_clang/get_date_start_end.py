import datetime
start_time = datetime.datetime(2020, 1, 1)
end_time = datetime.datetime.now()

mid_time = start_time
while mid_time < end_time:
    date_str = mid_time.strftime("%Y-%m-%d")
    print(date_str)
    mid_time += datetime.timedelta(days=1)

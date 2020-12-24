"""时间处理相关"""
import datetime

def yield_get_dates(start, end, _format="%Y-%m-%d"):
    """获取起止 时间中的所有日期"""
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    while start <= end:
        yield start.strftime(_format)
        start = start + datetime.timedelta(days=1)

def yield_get_date_steps(start, end, steps=None, _format="%Y-%m-%d"):
    _start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    steps = steps or ("2038-01-18",)
    num = 0
    while _start <= end:
        if num > len(steps) - 1:
            break
        step = datetime.datetime.strptime(steps[num], "%Y-%m-%d")
        if _start >= step and start < step:
            num += 1
            yield (start.strftime(_format), step.strftime(_format))
            start = step + datetime.timedelta(days=1)
        elif _start >= step:
            num += 1
        else:
            _start = _start + datetime.timedelta(days=1)
    yield (start.strftime(_format), end.strftime(_format))

[print(i) for i in yield_get_dates("2020-04-27", "2020-05-23")]
print("#----"*12)
[print(i) for i in yield_get_date_steps("2020-04-27", "2020-05-23")]
print("#----"*12)
[print(i) for i in yield_get_date_steps("2020-04-27", "2020-05-23", ("2020-05-03","2020-05-10"))]
print("#----"*12)
[print(i) for i in yield_get_date_steps("2020-04-27", "2020-01-23", ("2020-03-01","2020-05-01"))]

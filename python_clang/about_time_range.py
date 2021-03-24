"""时间处理相关"""
import time
from datetime import datetime, timedelta

def yield_get_dates(start, end, _format="%Y-%m-%d"):
    """获取起止 时间中的所有日期"""
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    while start <= end:
        yield start.strftime(_format)
        start = start + timedelta(days=1)

def yield_get_date_steps(start, end, steps=None, _format="%Y-%m-%d"):
    _start = datetime.strptime(start, "%Y-%m-%d")
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    steps = steps or ("2038-01-18",)
    num = 0
    while _start <= end:
        if num > len(steps) - 1:
            break
        step = datetime.strptime(steps[num], "%Y-%m-%d")
        if _start >= step and start < step:
            num += 1
            yield (start.strftime(_format), step.strftime(_format))
            start = step + timedelta(days=1)
        elif _start >= step:
            num += 1
        else:
            _start = _start + timedelta(days=1)
    yield (start.strftime(_format), end.strftime(_format))





def datetime2str(data, fmt="%Y-%m-%d %H:%M:%S"):
    result = ''
    if data and isinstance(data, datetime):
        result = data.strftime(fmt)
    return result


def datetime2int(data, unit='s'):
    result = 0
    if data and isinstance(data, datetime):
        result = int(time.mktime(data.timetuple()))
    return result


def count_age(str_date: str = '', dt_date: datetime = None) -> str:
    """
    根据出生年月日计算当前年龄(年月周天)
    """
    age = ''
    if str_date and len(str_date) >= len("2020-01-01"):
        try:
            str_date = str_date[:10]
            dt_date = datetime.strptime(str_date, "%Y-%m-%d")
        except:
            dt_date = None
    if dt_date:
        now = datetime.now()
        m = (now.year * 12 + now.month) - (dt_date.year * 12 + dt_date.month)
        y = m > 12 and int(m / 12)
        if y:
            age = f"{y}岁"
        elif m:
            age = f"{m}月"
        else:
            d = now.day - dt_date.day
            w = int(d / 7)
            age = w and f"{w}周" or f"{d or 1}天"
    return age

def count_ago(str_date: str = '', dt_date: datetime = None) -> str:
    """
    ret: x(秒|分钟|小时|天|周|月|年|)之前
    """
    msg = ''
    if str_date and len(str_date) >= len("2020-01-01"):
        try:
            str_date = str_date[:10]
            dt_date = datetime.strptime(str_date, "%Y-%m-%d")
        except:
            dt_date = None
    if dt_date:
        now = datetime.now()
        interval = now - dt_date
        if interval.days > 0:
            msg = msg = count_age(dt_date=dt_date)
            msg = msg.replace('岁', '年')
        elif interval.days == 0 and interval.seconds>10:
            _s = interval.seconds
            _m = _s and int(_s/60)
            _h = _m and int(_m/60)
            _str_s = (_s and f"{_s}秒")
            _str_m = (_m and f"{_m}分钟" or _str_s)
            _str_h = (_h and f"{_h}小时" or _str_m)
            msg = _str_s and _str_m and _str_h
        else:
            msg = '刚刚'
        msg = f"{msg}之前" if "刚刚" not in msg else msg
    return msg

if "__main__" == __name__:
    # region 测试时间范围
    [print(i) for i in yield_get_dates("2020-04-27", "2020-05-23")]
    print("#----"*12)
    [print(i) for i in yield_get_date_steps("2020-04-27", "2020-05-23")]
    print("#----"*12)
    [print(i) for i in yield_get_date_steps("2020-04-27", "2020-05-23", ("2020-05-03","2020-05-10"))]
    print("#----"*12)
    [print(i) for i in yield_get_date_steps("2020-04-27", "2020-01-23", ("2020-03-01","2020-05-01"))]
    #endregion
    print("---"*21+'\n\n')

    day = "2020-12-12"
    print(f"count_age|{day}", count_age(day))
    print(f"count_ago|{day}", count_ago(day))

    tm = datetime.now() - timedelta(seconds=100)
    tm = datetime.now() - timedelta(seconds=500)
    print(f"count_age|{datetime2str(tm)}", count_age(dt_date=tm))
    print(f"count_ago|{datetime2str(tm)}", count_ago(dt_date=tm))

    tm = datetime.now() - timedelta(seconds=11)
    print(f"count_age|{datetime2str(tm)}", count_ago(dt_date=tm))

    tm = datetime.now() - timedelta(seconds=0)
    print(f"count_age|{datetime2str(tm)}", count_ago(dt_date=tm))


    tm = datetime(2021,1,8,17,20,4)
    print(f"count_age|{datetime2str(tm)}", count_ago(dt_date=tm))

    day = "2020-09-12"
    print(f"count_age|{day}", count_age(day))

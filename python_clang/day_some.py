import time
import datetime

def test():
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
    utoday_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1610620848))
    print(utoday_str, utoday_str, utoday_str, utoday_str, utoday_str, utoday_str)
    
    
    
    to_s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"nyrsfm: {to_s}")

def run():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=str, help="xxxx-xx-xx 或 xxxx-xx-xx xx:xx:xx 或 1234567890")
    args = parser.parse_args()
    t = args.t
    if t.isdecimal():
        t = int(t)
        t_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
        print(f"{t} >> str2int >> {t_str}")
    elif len(t) == len("xxxx-xx-xx"):
        t_dt = datetime.datetime.strptime(t, "%Y-%m-%d")
        t_str = time.mktime(t_dt.timetuple())
        print(f"{t} >> str2int >> {t_str}")
    elif len(t) == len("xxxx-xx-xx xx:xx:xx"):
        t_dt = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
        t_str = time.mktime(t_dt.timetuple())
        print(f"{t} >> str2int >> {t_str}")
    else:
        print("格式不大对")
    
if __name__ == "__main__":
    # test()
    run()
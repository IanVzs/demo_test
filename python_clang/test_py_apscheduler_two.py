"""
阶段轮班

2020年11月23日 (banana, o7w1PuMBxmY_SWhuLifZrL9WzuAE) 开始
隔日换 (..., o7w1PuMR9ipKjrVpK0WGg-B-zR2g)

结束与两个月后(2021年01月23日)
"""
import time
import datetime
try:
    from pytz import utc, timezone
    china_tz = timezone('Asia/Shanghai')

    from apscheduler.schedulers.background import BackgroundScheduler
    # from apscheduler.jobstores.mongodb import MongoDBJobStore
    from apscheduler.jobstores.memory import MemoryJobStore
    from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
    from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
    from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
except:
    print("需安装下述包")
    print("pip3 install sqlalchemy", "pip3 install apscheduler")

import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
logger = logging

def init_scheduler():
    jobstores = {
        "memory": MemoryJobStore(),
    }
    executors = {
        'default': ThreadPoolExecutor(10),
        'processpool': ProcessPoolExecutor(3)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }
    scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=china_tz)
    return scheduler

def assignment() -> dict:
    """分配任务"""
    today = datetime.datetime.today()
    str_today = today.strftime("%Y-%m-%d")
    _sdate = datetime.datetime(2020, 11, 23)
    _edate = datetime.datetime(2021, 1, 23)
    _date = _sdate
    list_assigt = [{"banana": "o7w1PuMBxmY_SWhuLifZrL9WzuAE"}, {"...": "o7w1PuMR9ipKjrVpK0WGg-B-zR2g"}]
    dict_assigmt = {}
    num = 0
    while _date < _edate:
        num = int(num)
        str_date = _date.strftime("%Y-%m-%d")
        dict_assigmt[str_date] = list_assigt[num]
        num = not num
        _date = _date + datetime.timedelta(days=1)
    dict_assigmt = {_k:_v for _k, _v in dict_assigmt.items() if _k > str_today}
    return dict_assigmt

def shift_man(page_assigmt: dict, _day=None, num=None):
    """
    将数据库中, 联系方式修改为对应值班人
    """
    today = datetime.datetime.today()
    str_today = today.strftime("%Y-%m-%d")
    logger.warning(f"{str_today}, shift_man({_day}): {page_assigmt}")
    pass
    # TODO
    if num:
        scheduler.remove_job(num)

def my_listener(event):
    if event.exception:
        log_job = {
            "code": event.code,
            "jobid": event.job_id,
            "jobstore": event.jobstore
        }
        logger.warning(f'The job {event.job_id} crashed :( | {log_job}')
    else:
        logger.warning(f'The job {event.job_id} worked :)')

def job_scheduler(scheduler):
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    dict_assigmt = assignment()
    num = 0
    for _day, _page_assigmt in dict_assigmt.items():
        run_date = datetime.datetime.strptime(_day, "%Y-%m-%d")
        logger.warning(f"{_day}: {_page_assigmt}")
        scheduler.add_job(shift_man, 'date', run_date=run_date, id=_day, args=[_page_assigmt, _day])
        # region test
        scheduler.add_job(shift_man, 'interval', seconds=10+num, id=str(num), args=[_page_assigmt, _day, str(num)])
        num += 3
        #endregion
    scheduler.start()
    logger.warning(f"scheduler.get_jobs: {scheduler.get_jobs()}")
    return 1

# time.sleep(6)

# scheduler.remove_job('test_job_id')
# scheduler.shutdown(wait=True)

if "__main__" == __name__:
    scheduler = init_scheduler()
    jobs = job_scheduler(scheduler)
    while jobs:
        time.sleep(3)
        if datetime.datetime.now() > datetime.datetime(2021, 1, 23):
            logging.warning("事了拂衣去,深藏身与名.")
            break

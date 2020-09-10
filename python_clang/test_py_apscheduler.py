"""
requests: 
    sqlalchemy
    apscheduler

测试`apscheduler`功能
"""
import time
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
        # 'mongo': MongoDBJobStore(),
        "memory": MemoryJobStore(),
        # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
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



def myfunc():
    logger.info("myfunc O(∩_∩)O")
    import random
    if random.random() > 0.6:
        raise "hey raise"

def my_listener(event):
    if event.exception:
        log_job = {
            "code": event.code,
            "jobid": event.job_id,
            "jobstore": event.jobstore
        }
        logger.info(f'The job {event.job_id} crashed :( | {log_job}')
    else:
        logger.info(f'The job {event.job_id} worked :)')

def job_scheduler(scheduler):
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.add_job(myfunc, 'interval', seconds=5, id='test_job_id') # minutes=1
    scheduler.start()
    logger.info(f"scheduler.get_jobs: {scheduler.get_jobs()}")
    return 1

# time.sleep(6)
# scheduler.remove_job('test_job_id')
# scheduler.shutdown(wait=True)

if "__main__" == __name__:
    scheduler = init_scheduler()
    jobs = job_scheduler(scheduler)
    while jobs:
        time.sleep(3)

"""
requests: 
    sqlalchemy
    apscheduler

测试`apscheduler`功能
"""

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




def myfunc():
    print("myfunc O(∩_∩)O")
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
        print(f'The job {event.job_id} crashed :( | {log_job}')
    else:
        print(f'The job {event.job_id} worked :)')

scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

scheduler.start()
scheduler.add_job(myfunc, 'interval', seconds=1, id='test_job_id') # minutes=1
print(f"scheduler.get_jobs: {scheduler.get_jobs()}")

import time
time.sleep(6)
scheduler.remove_job('test_job_id')
scheduler.shutdown(wait=True)
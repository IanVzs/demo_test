"""
定时任务, 根据设定时间的先后顺序进行, 也就是说一秒的先到了, 结果延迟4s那么三秒的任务也得等到4s延迟之后才会进行.
就很不并行, 很不好
"""
from gevent_tasks import TaskManager, cron
manage = TaskManager()

@manage.task(interval=cron('* * * * *'))
def every_minute(task, *args):
    import time
    time.sleep(3)
    print('hi', args, task, task.timing)

@manage.task(interval=1)
def every_minute1(task, *args):
    import time
    time.sleep(4)
    print('hi_1', args, task, task.timing)

@manage.task(interval=3)
def every_minute3(task, *args):
    print('hi_3', args, task, task.timing)
manage.forever()


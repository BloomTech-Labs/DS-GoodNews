from apscheduler.schedulers.blocking import BlockingScheduler
from goodnews import schedule_update

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def timed_job():
    print('This job is run every 5 minutes.')
    schedule_update()

sched.start()

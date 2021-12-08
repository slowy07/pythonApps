from apscheduler.schedulers.blocking import BlockingScheduler
from caller import search

sched = BlockingScheduler()


# set 2 hours
sched.add_job(search, "interval", hours=1)
sched.start()

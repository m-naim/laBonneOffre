from apscheduler.schedulers.blocking import BlockingScheduler
import leboncoinScraping

scheduler = BlockingScheduler()
scheduler.add_job(leboncoinScraping.run, 'interval', hours=1)

scheduler.start()
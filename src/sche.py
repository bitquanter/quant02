
# coding:utf-8

import gevent
from gevent import monkey
monkey.patch_all()

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test():
    with open("c://s.txt", "a+") as f:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        f.write('\n')

def aps_test1():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def sche():
	scheduler = BlockingScheduler()
	scheduler.add_job(func=aps_test, trigger='cron', second='*/2')
	scheduler.add_job(func=aps_test1, trigger='cron', second='*/2')
	scheduler.start()
 
def bar():
	while 1:
		print('.')
		gevent.sleep(0)
		print('#')
 
gevent.joinall([
    gevent.spawn(sche),
    gevent.spawn(bar),
])







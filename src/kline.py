import gevent
from gevent import monkey
monkey.patch_all()

import sys
from pprint import pprint
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


from engine import onbar

def source():
    print('#')
    count=0
    while 1:
        gevent.sleep(0)
        line=sys.stdin.readline().strip()
        print( "# %d " % count )
        count=count+1
#       print(line)
        try:
            obj = json.loads(line)
#           pprint(obj)
            onbar(obj)
        except Exception as  e:
            print ('str(Exception):\t', str(Exception))
            print ('str(e):\t\t', str(e))
            print ('repr(e):\t', repr(e))
            print ('e.message:\t', e.message)
            print ('traceback.print_exc(): %s', traceback.print_exc())
            print ('traceback.format_exc():\n%s' % traceback.format_exc())
            print ('########################################################')


def timer():
    with open("./timer.log", "a+") as f:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        f.write('\n')

def heatbeat():
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(".")

def sche():
	scheduler = BlockingScheduler()
	scheduler.add_job(func=heatbeat, trigger='cron', second='*/2')
	scheduler.add_job(func=timer, trigger='cron', second='*/2')
	scheduler.start()

gevent.joinall([
    gevent.spawn(sche),
    gevent.spawn(source),
])




import sys
from pprint import pprint
import json

from engine import onbar

count=0
while 1:
    previousTime = "2000-09-09 11:11:00"
    line=sys.stdin.readline().strip()
    print( "# %d " % count )
    count=count+1
#    print(line)
    try:
        obj = json.loads(line)
#        pprint(obj)
        onbar(obj) 
        
    # except:
    #    print (' error!', '*'*10)
    #    continue
    except Exception as  e:
        print ('str(Exception):\t', str(Exception))
        print ('str(e):\t\t', str(e))
        print ('repr(e):\t', repr(e))
        print ('e.message:\t', e.message)
        print ('traceback.print_exc(): %s', traceback.print_exc())
        print ('traceback.format_exc():\n%s' % traceback.format_exc())
        print ('########################################################')


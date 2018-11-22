import sys
from pprint import pprint
import json
count=0
while 1:
    line=sys.stdin.readline().strip()
    if not line:
        continue
    print( "# %d " % count )
    count=count+1
    print(line)
    try:
        obj = json.loads(line)
        pprint(obj)
    except:
        continue

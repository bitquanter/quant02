#coding: UTF-8
import sys
import inspect
from pprint import pprint
import json 
from datetime import datetime, timedelta
import pandas as pd

df = pd.DataFrame(columns=['open', 'close', 'high', 'low'])
class bband(object): 
    def __init__(self, name='bband'):
        self.name = name

    def onbar(self,obj): 
        print (self.name, "onbar>>>>>>>>>>>>>>>>before")
        timespan = timedelta(days=2)
        nowTime=datetime.now()
        obj_time = pd.to_datetime(obj['time'])
        if 1:#obj_time > nowTime - timespan:
            print("filter %s" % json.dumps(obj))
            #print( obj.open, obj.close, obj.high, obj.low)
            #print (type(obj['time']))
            #df.loc[obj['time']] = [obj.open, obj.close, obj.high, obj.low]
            df.loc[obj['time']] = [obj['open'], obj['close'], obj['high'], obj['low']]
            print (df)
        print (self.name, "onbar<<<<<<<<<<<<<<<<after")

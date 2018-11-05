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
        nowTime=datetime.now()
        #df.drop(df.index,inplace=True)
        for days in range(1, 10):
            timespan = timedelta(days=days)
            obj_time = pd.to_datetime(obj['time'])
            thresh_date = nowTime - timespan
            if obj_time > thresh_date:
                print("filter between %s and %s, obj : %s" % nowTime, njson.dumps(obj))
                df.loc[obj['time']] = [obj.open, obj.close, obj.high, obj.low]
                df.loc[obj['time']] = [obj['open'], obj['close'], obj['high'], obj['low']]
            print (df)
        print (self.name, "onbar<<<<<<<<<<<<<<<<after")

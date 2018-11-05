# -*- coding:utf-8 -*-
# @Author :songtao

import websocket
import sys
import json
import requests
import time


url ='wss://www.bitmex.com/realtime?subscribe=tradeBin1m,orderBook:XBTUSD'
def on_open(self):
    #asubscribe okcoin.com spot ticker
    print('running on_open....')
    #self.send("{'event':'addChannel','channel':'ok_sub_futureusd_btc_kline_this_week_1min'}")

def on_message(self,evt):
    evt = json.loads(evt)
    flag = evt.get('action', None)
    if flag != 'insert':
        return

    data = evt.get('data', None)
    if data == None:
        return

    data_dict = {}
    for d in data:
        #if d['symbol'] != 'XBTUSD':
        if d['symbol'] != 'XBTUSD' and d['symbol'] != 'ETHUSD':
            continue
        timestamp = d['timestamp']
        timestamp = timestamp.replace("T", " ").replace(".000Z", "")
        timeArray = time.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))

#        print(timestamp)
        #data_dict['symbol'] = 'xbt/usd'
        if d['symbol'] == 'XBTUSD':
            data_dict['symbol'] = 'xbt/usd'
        elif d['symbol'] == 'ETHUSD':
            data_dict['symbol'] = 'eth/usd'

        data_dict['source'] = 'bitmex'
        data_dict['channel'] = evt['table']
        data_dict['sample_time'] = timeStamp*1000
        data_dict['open_'] = d['open']
        data_dict['high_'] = d['high']
        data_dict['low_'] = d['low']
        data_dict['close_'] = d['close']
        data_dict['volume'] = d['volume']
        data_dict['coin_volume'] = d['homeNotional']
    
    if not data_dict:
        return
    print (data_dict)
    return 
    url = 'http://127.0.0.1:8006/api/kline1M'
    try:
        res = requests.post(url,data_dict)
        rs = res.text
        rs = json.loads(rs)
        code = rs['code']
        if code != '0':
            print(data_dict)
    except Exception as e:
        print(e)
        print(data_dict)
    
    # with pymysql.connect(host=config.mysql_param['HOST'], user=config.mysql_param['USER'],
    #                      passwd=config.mysql_param['PASSWORD'],
    #                      db=config.mysql_param['NAME'], port=config.mysql_param['PORT'], charset='utf8',
    #                      cursorclass=pymysql.cursors.DictCursor, autocommit=True,
    #                      ).cursor() as cursor:
    #     sql_str = f'insert into '
    #     cursor.execute("select * from fund_index_raw_static_data")

def on_error(self,evt):
    print ('running on_error....')

    websocket.enableTrace(False)
    host = url
    ws = websocket.WebSocketApp(host,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=30,ping_timeout=15)

def on_close(self,evt):
    print ('DISCONNECT')

if __name__ == "__main__":
    websocket.enableTrace(False)
    host = url
    ws = websocket.WebSocketApp(host,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=30,ping_timeout=15)


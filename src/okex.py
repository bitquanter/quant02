# -*- coding:utf-8 -*-
# @Author :songtao

import websocket
import sys
import json
import requests
import zlib 

url = "wss://real.okex.com:10440/websocket/okexapi"
def on_open(self):
    # subscribe okcoin.com spot ticker
    #self.send('{ "event": "subscribe",  "channel": "candles",  "key": "trade:1m:tBTCUSD" }')
    self.send("{'event':'addChannel','channel':'ok_sub_futureusd_btc_kline_this_week_1min'}")

def on_message(self, evt):
    decompress = zlib.decompressobj(
            -zlib.MAX_WBITS  # see above
    )
    evt = decompress.decompress(evt)
    evt += decompress.flush()
    evt = json.loads(evt)
    print (evt)
    return 
    data = json.loads(evt)
    print (data)
    return 
    if isinstance(data, dict):
        return
    if not isinstance(data[1][0], int):
        return

    data_dict = {}
    data_dict['symbol'] = 'btc/usdt'
    data_dict['source'] = 'bitfinex'
    data_dict['channel'] = 'trade1m'
    data_dict['sample_time'] = data[1][0]
    data_dict['open_'] = data[1][1]
    data_dict['high_'] = data[1][3]
    data_dict['low_'] = data[1][4]
    data_dict['close_'] = data[1][2]
    data_dict['volume'] = 0
    data_dict['coin_volume'] = data[1][5]
    print(data_dict['sample_time'])
    url = 'http://127.0.0.1:8007/api/kline1M'
    try:
        res = requests.post(url, data_dict)
        rs = res.text
        rs = json.loads(rs)
        code = rs['code']
        if code != '0':
            print(data_dict)
    except Exception as e:
        print(e)
        print(data_dict)



def on_error(self, evt):
    print('running on_error...')

    websocket.enableTrace(False)
    host = url
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=30, ping_timeout=15)


def on_close(self, evt):
    print('running on_close....')
    websocket.enableTrace(False)
    host = url
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=30, ping_timeout=15)


if __name__ == "__main__":
    websocket.enableTrace(False)
    host = url
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(ping_interval=30, ping_timeout=15)



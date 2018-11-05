ps -eaf |grep runkline|awk '{printf "%s ",$2}'|xargs kill -9
ps -eaf |grep kline_huobip_btc.usdt.sh|awk '{printf "%s ",$2}'|xargs kill -9

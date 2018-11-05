find /data/zhangwei/1token_realtime_get/data_save_directory -name "*_zhubi_huobip_btc.usdt.json.gz" -mtime -1 -print|xargs zcat
find /data/zhangwei/1token_realtime_get/data_save_directory -name "*_zhubi_huobip_btc.usdt.json" -mtime -10 -print|xargs cat

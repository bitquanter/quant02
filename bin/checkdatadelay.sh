tail -f /datassd/baiyujie/wsdata/2018-11-02/futures/ticker/okex/csv/2018-11-02_futures_ticker_okex_btc_quarter.csv |awk -F, '{printf ("%d,", $14); system("python a.py") }' >>diff.out

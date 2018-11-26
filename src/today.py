import tushare as ts
import pandas as pd
def get_date_list(start, end):
    date_list = [d.strftime("%Y-%m-%d") for d in pd.date_range(start, end, freq="B")]
    return date_list
#print(ts.__version__)
#print(get_date_list("2018-01-01","2018-11-26"))
#print(ts.get_sina_dd('300054', date='2018-11-26'))
#print(ts.get_sina_dd('300315', date='2018-11-26'))
#ts.get_today_all()
#print(ts.get_tick_data('300054',date='2018-11-26'))
#print(ts.get_hist_data('300054',start='2018-01-01',end='2018-11-26'))
pro = ts.pro_api("3b307178a6d4bbcdb05fe98828ea64bcf5427477adc2e02db8ffc215")
#print(ts.pro_bar(pro_api=api, ts_code='300054.SZ', adj='qfq', start_date='20180101', end_date='20181011'))
data = pro.stock_basic(exchange='', list_status='L', fields='symbol')
#print(data)
#print(type(data))
#date_list=get_date_list("2018-01-01","2018-11-26")
for index, row in data.iterrows():
    print(row['symbol'])
    #print(ts.get_sina_dd(data[i]),date="2018-11-26")

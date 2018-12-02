import tushare as ts
import pandas as pd
def get_date_list(start, end):
    date_list = [d.strftime("%Y-%m-%d") for d in pd.date_range(start, end, freq="B")]
    return date_list
#print(ts.__version__)
print(ts.get_stock_basics())
#print(get_date_list("2018-01-01","2018-11-26"))
data=ts.get_sina_dd('002354', date='2018-11-27')
print(data)
buys=0
buysCount=0
sells=0
sellsCount=0
neutral=0
neutralCount=0
i=0
j=0
k=0
for index, row in data.iterrows():
    count=int(row['volume'])
    type=row['type']
    preprice=row['preprice']
    price=row['price']
    if type=="买盘":
        buys+=count
        buysCount+=count*price
        i+=1
    elif type=="卖盘":
        sells+=count
        sellsCount += count * price
        j+=1
    else:
        neutral+=count
        neutralCount += count * price
        k+=1
print("买盘:",buys,"笔数:",i,"平均价:",buysCount/buys)
print("卖盘:", sells,"笔数:",j,"平均价:",sellsCount/sells)
print("中性盘:", neutral,"笔数:",k,"平均价:",neutralCount/neutral)
#print(ts.get_sina_dd('300315', date='2018-11-26'))
#ts.get_today_all()
#print(ts.get_tick_data('300054',date='2018-11-26'))
#print(ts.get_hist_data('300054',start='2018-01-01',end='2018-11-26'))
#api = ts.pro_api("3b307178a6d4bbcdb05fe98828ea64bcf5427477adc2e02db8ffc215")
#print(ts.pro_bar(pro_api=api, ts_code='300054.SZ', adj='qfq', start_date='20180101', end_date='20181011'))
import csv
import os
import tushare as ts
def get_codelist(filename):
    return csv.reader(open(filename,'r'))

def get_daily_info(code,sd,ed):
    pro = ts.pro_api("3b307178a6d4bbcdb05fe98828ea64bcf5427477adc2e02db8ffc215")
    return pro.daily(ts_code=code, start_date=sd, end_date=ed)



def shares_bigdata_analysis(c,code):
    filename='f:/data/'+c+'/'+code+'_daily.csv'
    df=csv.reader(open(filename, 'r'))
    for row in df:
        print(row)

def read_file(folder,filename):
    return csv.reader(open(folder+filename,'r'))

def ergodic_folder_handle_data(folder,code):
    list=os.listdir(folder)
    buys_count=0
    sells_count=0
    buys_amount = 0
    sells_amount = 0
    amounts=0
    for i in range(0,len(list)):
        buys = 0
        buysCount = 0
        sells = 0
        sellsCount = 0
        neutral = 0
        neutralCount = 0
        ii = 0
        j = 0
        k = 0
        if list[i].find('2018-11-')!=-1:
            date=list[i][:10].replace('-','')
            print(date)
            for row in read_file(folder,list[i]):
                    count = int(row[4])
                    type = row[6]
                    preprice = row[5]
                    price = float(row[3])
                    if type == "买盘":
                        buys += count
                        buys_count+=count
                        buysCount += count * price
                        ii += 1
                    elif type == "卖盘":
                        sells += count
                        sells_count+=count
                        sellsCount += count * price
                        j += 1
                    else:
                        neutral += count
                        neutralCount += count * price
                        k += 1
                    average_buys=0
                    average_sells=0
                    average_neutral=0
            if buys != 0:
                average_buys = buysCount / buys
            if sells != 0:
                average_sells = sellsCount / sells
            if neutral != 0:
                average_neutral = neutralCount / neutral
            buys_amount+=average_buys*buys
            sells_amount+=average_sells*sells
            amount=get_daily_info(code,date,date)['amount']
            amounts+=amount
            print("买盘:", buys, "笔数:", ii, "买盘平均价:", round(average_buys,2),"买盘总金额:", round(average_buys*buys,2),"买盘占比:",round(average_buys*buys/(amount*1000),2))
            print("卖盘:", sells, "笔数:", j, "卖盘平均价:",  round(average_sells,2),"卖盘总金额:",  round(average_sells*sells,2),"卖盘占比:",round(average_sells*sells/(amount*1000),2))
            print("中性盘:", neutral, "笔数:", k, "中性平均价:",  round(average_neutral,2),"中性总金额:",  round(average_neutral*neutral,2),"中性盘占比:",round(average_neutral*neutral/(amount*1000),2))
    print("交易总金额：",amounts)
    print("总买盘：",buys_count,"总买盘金额：",round(buys_amount,2),"总买盘平均价：",round(buys_amount/buys_count,2),"总买盘占比：",buys_amount/(amounts*1000))
    print("总卖盘：",sells_count,"总卖盘金额：",round(sells_amount,2),"总卖盘平均价：",round(sells_amount/sells_count,2),"总卖盘占比：",sells_amount/(amounts*1000))
    print("买卖金额差：",round(buys_amount-sells_amount,2))
# for row in get_codelist('f:/data/code.csv'):
#     print(row[1])
#     try:
#         shares_bigdata_analysis(row[1])
#     except:
#         pass
#     continue

# shares_bigdata_analysis('000001','000001.SZ')
ergodic_folder_handle_data('F:/data/600518/','600518.SH')

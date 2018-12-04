import os
import tushare as ts
import pandas as pd
import csv
def get_date_list(start, end):
    date_list = [d.strftime("%Y-%m-%d") for d in pd.date_range(start, end, freq="B")]
    return date_list

def get_bigdata_intofile_for_code_and_date(c,d):
    path="f:/data/"+c
    if not os.path.exists(path):
        os.makedirs(path)
        print("make dir:",path)

    out = open(path+'/'+d+'.csv', 'w', newline='')
    csv_write = csv.writer(out, dialect='excel')

    data = ts.get_sina_dd(c, date=d)
    # print(data)
    # if data==None:
    #     pass
    # else:
    for index, row in data.iterrows():
        csv_write.writerow(row)

def get_allcode_intofile(path,filename):
    pro = ts.pro_api("3b307178a6d4bbcdb05fe98828ea64bcf5427477adc2e02db8ffc215")
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    if path=="":
        path = "f:/data/"
    if not os.path.exists(path):
        os.makedirs(path)
        print("make dir:", path)
    if filename =="":
        filename="code.csv"
    out = open(path+filename, 'w', newline='')
    csv_write = csv.writer(out, dialect='excel')
    for index, row in data.iterrows():
        csv_write.writerow(row)

def get_codelist(filename):
    return csv.reader(open(filename,'r'))

def get_bigdata_for_date(c):
    datelist=get_date_list('2018-11-14','2018-12-04')

    for date in datelist:
        print(date)
        try:
            get_bigdata_intofile_for_code_and_date(c,date)
        except:
            pass
        continue
# for row in get_codelist('f:/data/code.csv'):
#     print(row[1])
#     try:
#         get_bigdata_for_date(row[1])
#     except :
#         pass
#     continue

get_bigdata_for_date('000004')
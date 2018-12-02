import tushare as ts
import pandas as pd
import os
import csv
def get_daily_info(c,code,sd,ed):
    path = "f:/data/" + c
    if not os.path.exists(path):
        os.makedirs(path)
        print("make dir:",path)
    out = open(path + '/' + code + '_daily.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    pro = ts.pro_api("3b307178a6d4bbcdb05fe98828ea64bcf5427477adc2e02db8ffc215")
    df = pro.daily(ts_code=code, start_date=sd, end_date=ed)
    for index, row in df.iterrows():
        csv_write.writerow(row)

def get_codelist(filename):
    return csv.reader(open(filename,'r'))

for row in get_codelist('f:/data/code.csv'):
    print(row[0])
    try:
        get_daily_info(row[1],row[0],'20180101','20181130')
    except :
        pass
    continue
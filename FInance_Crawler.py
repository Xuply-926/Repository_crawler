#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf-8
"""
Created on Fri Jan 28 21:22:53 2022

@author: wxp
"""
from bs4 import BeautifulSoup
import requests
import re
import csv
import datetime
      
        

def finance_crawler(date):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

    for page in range(1,244):
        url = f'http://33.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124045658381001129467_1643375031942&pn={page}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1643375031943'
        response = requests.get(url = url,headers = headers)
        data = response.text
        data2 = re.findall('\[(.*?)\]',data)[0]
        data_eval = eval(data2)
        result_all = []
        for i in range(20):
            result = []
            for j in data_eval[i].keys():
                result.append(str(data_eval[i][j]))
            result_all.append(result)
    
        with open('stock_{}.csv'.format(date),mode = 'a',encoding = 'utf-8',newline = '')as f:
            csv_write = csv.writer(f)
            for i in range(20):
                csv_write.writerow(result_all[i])
    url = 'http://33.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124045658381001129467_1643375031942&pn=244&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1643375031943'
    response = requests.get(url = url,headers = headers)
    data = response.text
    data2 = re.findall('\[(.*?)\]',data)[0]
    data_eval = eval(data2)
    result_all = []
    for i in range(16):
        result = []
        for j in data_eval[i].keys():
            result.append(str(data_eval[i][j]))
        result_all.append(result)
    
    with open('stock_{}.csv'.format(date),mode = 'a',encoding = 'utf-8',newline = '')as f:
        csv_write = csv.writer(f)
        for i in range(16):
            csv_write.writerow(result_all[i])
            
if __name__ == '__main__':
    x = datetime.datetime.now()
    d = x.date()
    finance_crawler(d)
    
        


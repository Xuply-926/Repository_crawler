#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 11:57:58 2022

@author: wxp
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime


def list_stock(date):
    stock = pd.read_csv('stock_{}.csv'.format(date),encoding = 'utf-8',names = ['a','最新价','涨跌幅','涨跌额','成交量','成交额','振幅','换手率', '市盈率', '量比', 'b', '代码', 'c','名称', '最高', '最低', '今开', '昨收','d','e','f','市净率','g','h','i','j','k','l','m','n','o'])
    stock['代码'] = stock['代码'].apply(lambda x : str(x).zfill(6))
    stock = stock.iloc[:,[1,2,3,4,5,6,7,8,9,11,13,14,15,16,17,21]]
    stock_code = stock.iloc[:,9]
    return stock_code

def history_record(code):
    #df = pd.DataFrame()
    url = 'http://quotes.money.163.com/trade/lsjysj_{}.html#01b07'.format(code)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    tables = soup.findAll('table')
    df_list = []
    df_list.append(pd.concat(pd.read_html(tables[3].prettify())))
    df = pd.concat(df_list)
    return df 


if __name__ == '__main__':
    print('Please enter the stock code.')
    code = str(input())
    x = datetime.datetime.now()
    d = x.date()
    stock_code = list_stock(d)
    while True:
        if code not in list(stock_code):
            print('Wrong stock code!')
            code = str(input())
        else:
            print('Right stock code!')
            
            break
    history_record(code).to_excel('{}.xlsx'.format(code))
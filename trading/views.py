import json

from django.shortcuts import render
import numpy as np
import hashlib
import time
from urllib.parse import urlencode
import jwt
import ccxt
import pandas as pd
from datetime import datetime
import pyupbit
import requests
import uuid
SECRET_KEY = 'ho8x3KLz3QRUxqeJCknqxixdZMPGl94GmK2W7Iwy'
ACCESS_KEY = 'LCyFJl7rVzIGiKl74xQ4i1CcEJxJovCsMS6D9Qxx'

url = "https://api.upbit.com/v1/candles/days"

"""querystring = {"market": "KRW-BTC", "count": "1"}
response = requests.request("GET", url, params=querystring)

print(response.json()[0]['trade_price'])"""

def TradingHome(request):
    TH_200_u = TradeHistory_200_u("KRW-BTC", 15, 33)
    status_u = TH_200_u.values[-1]
    status_u[1] = format(round(status_u[1]), ',')
    color_u = "blue";
    if status_u[0] == "SELL":
        color_u = "red";
    TradeHistory_u = TH_200_u.values
    ROE_u = round(ROE_200_u(TH_200_u), 2)

    TH_200_b = TradeHistory_200_b("BTC/USDT", 15, 33)
    status_b = TH_200_b.values[-1]
    status_b[1] = format(round(status_b[1]), ',')
    color_b = "blue";
    if status_b[0] == "SELL":
        color_b = "red";
    TradeHistory_b = TH_200_b.values
    ROE_b = round(ROE_200_b(TH_200_b), 2)

    return render(request, "trading/trading_main.html", {
        'TradeHistory_u': TradeHistory_u,
        'status_u' : status_u,
        'color_u' : color_u,
        'ROE_u' : ROE_u,

        'TradeHistory_b': TradeHistory_b,
        'status_b': status_b,
        'color_b': color_b,
        'ROE_b': ROE_b,
    })

def get_TradePrice(ticker):

    """ 현재가 추출 함수 """

    TradePrice = pyupbit.get_current_price(ticker)
    return int(TradePrice)


def get_ClosePrice(ticker):

    """ 종가 추출 함수 """

    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    ClosePrice = df['close'].iloc[-1]
    return int(ClosePrice)


def get_MA(ticker, ma1, ma2):

    """ 이평선(close) 추출 함수 """

    df = pyupbit.get_ohlcv(ticker, interval="day", count=ma2)
    ma15 = df['close'].rolling(window=ma1).mean().iloc[-1]
    ma33 = df['close'].rolling(window=ma2).mean().iloc[-1]

    if ma15 >= ma33:
        return int(ma15)
    elif ma15 < ma33:
        return int(ma33)

def TradeHistory_200_u(ticker, ma1, ma2):

    """ 최근 200일 매매내역 """

    df = pyupbit.get_ohlcv(ticker, interval="day", count=200).iloc[:-1]
    df['MA15'] = df['close'].rolling(window=ma1).mean()
    df['MA33'] = df['close'].rolling(window=ma2).mean()
    df = df.dropna()

    status = ""
    if df.iloc[0]['close'] > df.iloc[0]['MA15'] and df.iloc[0]['close'] > df.iloc[0]['MA33']:
        status = "BUY"
    else:
        status = "SELL"

    position = {'status': [], 'price': [], 'date': []}
    for i in df.index:
        if df.loc[i, 'close'] > df.loc[i, 'MA15'] and df.loc[i, 'close'] > df.loc[i, 'MA33']:
            if status == "SELL":
                status = "BUY"
                position['status'].append(status)
                position['price'].append(df.loc[i, 'close'])
                position['date'].append(i.strftime('%Y-%m-%d'))
        else:
            if status == "BUY":
                status = "SELL"
                position['status'].append(status)
                position['price'].append(df.loc[i, 'close'])
                position['date'].append(i.strftime('%Y-%m-%d'))

    df_TradeHistory200 = pd.DataFrame(position)#.iloc[:-1]

    return df_TradeHistory200


def ROE_200_u(df_TradeHistory200):

    df = df_TradeHistory200
    SeedMoney = 1000000
    buy_price = 0
    sell_price = 0

    for i in df.index:
        status = df.loc[i, 'status']
        if status == "BUY":
            buy_price = df.loc[i, 'price']
        elif status == "SELL" and buy_price != 0:
            sell_price = df.loc[i, 'price']
            SeedMoney *= (sell_price / buy_price)

    return SeedMoney / 1000000 * 100


def KRW_Market():

    url = "https://api.upbit.com/v1/ticker?markets="
    market = str(pyupbit.get_tickers(fiat="KRW")).replace("[", "").replace("]", "")
    market = market.replace("'", "")
    url = url + market

    response = requests.get(url)
    market_list = response.json()

    """for dic in market_list:
        del dic['trade_date', 'trade_time', 'trade_date_kst', 'trade_time_kst',
                'trade_timestamp', 'opening_price', 'high_price', 'low_price', 'change_price', 'change_rate',
                'acc_trade_price', 'acc_trade_volume', 'highest_52_week_date', 'lowest_52_week_date', 'timestamp']"""

    return market_list


def TradeHistory_200_b(ticker, ma1, ma2):

    """ 최근 200일 매매내역 """

    ohlcvs = binance.fetch_ohlcv(ticker, '1d')[-200:-1]
    for ohlc in ohlcvs:
        ohlc[0] = datetime.fromtimestamp(ohlc[0] / 1000).strftime('%Y-%m-%d')
    col_name = ['date', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(ohlcvs, columns=col_name)
    df['MA15'] = df['close'].rolling(window=ma1).mean()
    df['MA33'] = df['close'].rolling(window=ma2).mean()
    df = df.dropna()

    status = ""
    if df.iloc[0]['close'] > df.iloc[0]['MA15'] and df.iloc[0]['close'] > df.iloc[0]['MA33']:
        status = "BUY"
    else:
        status = "SELL"

    position = {'status': [], 'price': [], 'date': []}
    for i in df.index:
        if df.loc[i, 'close'] > df.loc[i, 'MA15'] and df.loc[i, 'close'] > df.loc[i, 'MA33']:
            if status == "SELL":
                status = "BUY"
                position['status'].append(status)
                position['price'].append(df.loc[i, 'close'])
                position['date'].append(df.loc[i, 'date'])
        else:
            if status == "BUY":
                status = "SELL"
                position['status'].append(status)
                position['price'].append(df.loc[i, 'close'])
                position['date'].append(df.loc[i, 'date'])

    df_TradeHistory200 = pd.DataFrame(position)

    return df_TradeHistory200


def ROE_200_b(df_TradeHistory200):

    df = df_TradeHistory200
    SeedMoney = 1000000
    buy_price = 0
    sell_price = 0

    for i in df.index:
        status = df.loc[i, 'status']
        if status == "BUY":
            buy_price = df.loc[i, 'price']
        elif status == "SELL" and buy_price != 0:
            sell_price = df.loc[i, 'price']
            SeedMoney *= (sell_price / buy_price)

    return SeedMoney / 1000000 * 100


binance = ccxt.binance()
markets = binance.fetch_tickers()

ma1 = 15  # 이평선1 기간
ma2 = 33  # 이평선2 기간

ohlcvs = binance.fetch_ohlcv("BTC/USDT", '1d')[-200:-1]

for ohlc in ohlcvs:
    ohlc[0] = datetime.fromtimestamp(ohlc[0] / 1000).strftime('%Y-%m-%d')

print(ohlcvs[-1])


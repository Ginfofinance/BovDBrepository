# coding: utf-8
import sqlite3
from pandas import DataFrame
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mpl_finance import candlestick_ohlc


#____________________________________Accessing the BovDB database and collecting data_______________________________________________
conn = sqlite3.connect('../DataBase/DataBase.db')
cursor = conn.cursor()

cursor.execute("""SELECT c.id_ticker, c.date, c.open, c.high, c.low, c.close, c.factor
                                           FROM price as c JOIN ticker as p on c.id_ticker = p.id_ticker WHERE p.id_ticker = 107""")
df = DataFrame(cursor.fetchall())
conn.close()

df.columns = ["cd_ticker", "date", "open", "high", "low", "close", "factor"]
df = df.loc[(df['date'] >= '2005-08-24') & (df['date'] <= '2005-09-10')]

#___________________________________________________________________________________________________________________________________
def daily_candlesitcks_chart(df):
    BovDB_datas = df.loc[:, ["date", "open", "high", "low", "close"]]
    BovDB_datas['date'] = pd.to_datetime(BovDB_datas['date'])
    BovDB_datas['date'] = BovDB_datas['date'].apply(mpl_dates.date2num)
    BovDB_datas = BovDB_datas.astype(float)

    # Creating Subplots
    plt.rcParams["figure.figsize"] = (7, 6)
    fig, ax = plt.subplots()
    plt.yticks((20.55, 30.00, 40.00, 50.00, 70.00, 90.00, 110.00,120.00, 130.00))
    candlestick_ohlc(ax, BovDB_datas.values, width=0.6, colorup='green', colordown='red', alpha=1)

    # Setting labels & titles
    ax.set_xlabel('Date',fontsize=22, fontfamily='serif')
    ax.set_ylabel('Price (R$)',fontsize=22, fontfamily='serif')
    ax.set_title('PETR4 (without factor)', fontsize=23, fontstyle= 'italic', fontfamily='serif')
    plt.xticks(rotation=45)
    plt.xticks(size=20)
    plt.yticks(size=20)

    # tormatting Date
    date_format = mpl_dates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()
    plt.savefig('daily_candlesitcks_chart.pdf', format='pdf')
    plt.show()


#________________________________________________________________________________________________________________________________________
def daily_candlesitcks_chart_factor(df):
    BovDB_datas_with_factor = df.loc[:, ["date", "open", "high", "low", "close", "factor"]]

    BovDB_datas_with_factor['open'] /= BovDB_datas_with_factor['factor']
    BovDB_datas_with_factor['high'] /= BovDB_datas_with_factor['factor']
    BovDB_datas_with_factor['low'] /= BovDB_datas_with_factor['factor']
    BovDB_datas_with_factor['close'] /= BovDB_datas_with_factor['factor']

    BovDB_datas_with_factor['date'] = pd.to_datetime(BovDB_datas_with_factor['date'])
    BovDB_datas_with_factor['date'] = BovDB_datas_with_factor['date'].apply(mpl_dates.date2num)
    BovDB_datas_with_factor = BovDB_datas_with_factor.astype(float)

    # Creating Subplots

    plt.rcParams["figure.figsize"] = (7, 6)
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, BovDB_datas_with_factor.values, width=0.6, colorup='green', colordown='red', alpha=1)

    # Setting labels & titles
    ax.set_xlabel('Date \n',fontsize=22, fontfamily='serif')
    ax.set_ylabel('Price (R$)',fontsize=22, fontfamily='serif')
    ax.set_title('PETR4 (with factor)', fontsize=23, fontstyle= 'italic', fontfamily='serif')
    plt.xticks(rotation=45)
    plt.xticks(size=20)
    plt.yticks(size=20)

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()
    plt.savefig('daily_candlesitcks_chart_factor.pdf', format='pdf')
    plt.show()


#_____________________________________________________________________________________________________________________________________

keep = True
print("\nThis program generates daily candlestick charts, it is possible to understand how to access the database and the difference in values with and without a factor.")
   
while (keep):
    print("_______________________________________________________________\n\n")
    print("What do you want to see?")
    print("Daily candlesticks chart without factor [Press 1]")
    print("Daily candlesticks chart with factor [Press 2]")
    print("Exit the program [Press 0]")
    Input = int(input())
    if(Input == 1):
        daily_candlesitcks_chart(df)
    elif(Input == 2):
        daily_candlesitcks_chart_factor(df)
    elif(Input == 0):
        keep = False

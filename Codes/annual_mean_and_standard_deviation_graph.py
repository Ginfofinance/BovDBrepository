import sqlite3
from pandas import DataFrame
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


#------------------------------------------------------------------------------------------------------------------------------------
conn = sqlite3.connect('../DataBase/DataBase.db')
cursor = conn.cursor()

cursor.execute("""SELECT c.id_ticker, c.date, c.open, c.high, c.low, c.close, c.factor
                                           FROM price as c JOIN ticker as p on c.id_ticker = p.id_ticker WHERE p.id_ticker = 107""")
df = DataFrame(cursor.fetchall())
conn.close()

df.columns = ["cd_ticker", "date", "open", "high", "low", "close", "factor"]
df['date'] =  pd.to_datetime(df['date'], format='%Y-%m-%d')
df["date"] = df["date"].dt.year

#------------------------------------------------------------------------------------------------------------------------------------
sumfactor = []
Sum = []
WorkingDays = []
Period = []

Average_Factor = []
Average = []
StandardDeviation_Factor = []
StandardDeviation = []
Year = 1995

while (Year<=2020):
    currentdata = df.loc[(df['date'] == Year)].copy()
    currentdata_factor = df.loc[(df['date'] == Year)].copy()
    currentdata_factor['close'] /= currentdata_factor['factor']
    sumdays = len(currentdata)

    currentdata = currentdata['close'].sum()
    currentdata_factor = currentdata_factor['close'].sum()

    average_factor= currentdata_factor/sumdays
    average = currentdata/sumdays

    sumfactor.append(currentdata_factor)
    Sum.append(currentdata)
    WorkingDays.append(sumdays)
    Period.append(Year)

    Average_Factor.append(average_factor)
    Average.append(average)

    #________________________standard_deviation_______________________________
    standard_deviation = df.loc[(df['date'] == Year)].copy()
    standard_deviation['close'] = (standard_deviation['close']-average)*(standard_deviation['close']-average)
    standard_deviation = standard_deviation['close'].sum()


    standard_deviation_factor = df.loc[(df['date'] == Year)].copy()
    standard_deviation_factor['close'] /= standard_deviation_factor['factor']
    standard_deviation_factor['close'] = (standard_deviation_factor['close']-average_factor)**2
    standard_deviation_factor = standard_deviation_factor['close'].sum()
    
    #____________________________________________________________________
    StandardDeviation_Factor.append(math.sqrt(standard_deviation_factor/sumdays))
    StandardDeviation.append(math.sqrt(standard_deviation/sumdays))

    average = 0
    average_factor = 0 
    standard_deviation = 0
    standard_deviation_factor = 0
    currentdata_factor = 0
    currentdata = 0
    sumdays = 0
    Year += 1


    
width = 0.4  # the width of the bars
plt.rcParams["figure.figsize"] = (16, 6)
fig, ax = plt.subplots()
ax.bar([(i-width/2) for i in Period], Average, width,
       yerr=StandardDeviation,
       align='center',
       ecolor='black',
       capsize=4,  label='without Factor')

ax.bar([(i+width/2) for i in Period], Average_Factor, width,
       yerr=StandardDeviation_Factor,
       align='center',
       ecolor='black',
       capsize=4,  label='with Factor')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Date',fontsize=22, fontfamily='serif' )
ax.set_ylabel('Average Price',fontsize=22, fontfamily='serif' )
ax.set_title('VALE3 (all period)',fontsize=24, fontstyle= 'italic', fontfamily='serif')
ax.set_xticks(Period)
plt.xticks(rotation=45)
plt.xticks(size=22)
plt.yticks(size=22)
ax.set_xticklabels(Period)
ax.legend()

plt.tight_layout()
plt.legend(fontsize=22, frameon=True)

#plt.subplots_adjust(left=0, bottom=0, right=2.0, top=1.0, wspace=0, hspace=0)
plt.savefig('annual_mean_and_standard_deviation_graph.pdf', format='pdf')
plt.show()

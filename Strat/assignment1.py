# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:02:17 2017

@author: saurabh agarwal
"""

#Assignment 1
import pandas_datareader.data as web
import datetime
sdate = datetime.datetime(2011,1,1)
edate = datetime.datetime(2013,1,1)

ibm_data = web.DataReader("IBM","google",sdate,edate)

#With Yahoo API not provoding historical quotes I couldn't test the output.
import matplotlib.finance as matfin
ibm_data2 = matfin.quotes_historical_yahoo_ochl("IBM",sdate,edate)



#Assignment 2
#pandas.core.frame.DataFrame
type(ibm_data)


type(ibm_data2)

IBM_dataframe = web.DataReader("IBM","google",sdate,edate)

             


#Assignment 3
a = 60
b = 200
IBM_dataframe['SMA'] = pd.ewma(IBM_dataframe['Close'], span = a, min_periods = a - 1)
IBM_dataframe['LMA'] = pd.ewma(IBM_dataframe['Close'], span = b, min_periods = b - 1)            


#Assignemnt 4
import datetime
sdate = datetime.datetime(2010,1,1)
edate = datetime.datetime(2015,1,1)
df  = web.DataReader("IBM","google",sdate,edate)

def ma_strategy(df,lma,sma):
    df['LMA'] = pd.ewma(df['Close'], span = lma, min_periods = lma - 1)
    df['SMA'] = pd.ewma(df['Close'], span = sma, min_periods = sma - 1)
    #df.to_csv("Inputs.csv")
    maWealth = 1.0
    cash=1
    stock=0
    rows = len(df['Close'])
    closePrices = df['Close']
    buy_data=[]
    sell_data=[]
    trade_price=[]
    wealth=[]
    for i in range(lma+1,rows):
        
        if(df['SMA'][i] > df['LMA'][i] and cash == 1):
            buyPrice = closePrices[i]
            buy_data.append(buyPrice)
            trade_price.append(buyPrice)
            cash = 0
            stock=1
        
        if(df['SMA'][i] < df['LMA'][i] and stock == 1):
          sellPrice = closePrices[i]
          cash = 1
          stock=0
          sell_data.append(sellPrice)
          trade_price.append(sellPrice)
          maWealth = maWealth * (sellPrice / buyPrice)
          wealth.append(maWealth)
          
    w=pd.DataFrame(wealth)
    print trade_price
    
    
    return(maWealth,w)
    
(maWealth,w) = ma_strategy(df,200,50)
plt.plot(w)


#Assignment 5
# Write a function that calculates daily Var at apple. Assume 95% confidence interval.
start = datetime.datetime(2013,12,1)
end   = datetime.datetime(2014,12, 1)
appl = web.DataReader("AAPL", "google", start, end)
portfolio = 1000000
daily_returns = appl["Close"].pct_change().dropna()*portfolio
var = daily_returns.quantile(0.05)
            
        
        
import yfinance as yf
import streamlit as st
from get_all_tickers import get_tickers as gt

#st.write("""
# Simple Stock Price App

#Shown are the stock closing price and volume of Google
#""")

tickers = gt.get_tickers()
print(tickers[:5])

# tickers from NYSE and NASDAQ only
#tickers = gt.get_tickers(AMEX=False)

#top_5 = gt.get_biggest_n_tickers(5)
#print(top_5)

#option = st.sidebar.selectbox(
 #    'How would you like to be contacted?',
  #   top_5)

#st.sidebar.header('User Input Parameters')
#ticker_symbol = st.sidebar.text_input('Ticker code', 'GOOGL')
#st.write('The ticker is', ticker_symbol)


#get data on this ticker
#ticker_data = yf.Ticker(ticker_symbol)

#get the historical prices for this ticker
#ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')
#Open High Low Close Volume Dividends Stock Splits

#st.line_chart(ticker_df.Close)
#st.line_chart(ticker_df.Volume)
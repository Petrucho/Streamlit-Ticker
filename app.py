import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google
""")

#define the ticker symbol
ticker_symbol = 'GOOGL'

#get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

#get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')
#Open High Low Close Volume Dividends Stock Splits

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
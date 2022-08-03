import yfinance as yf
import streamlit as st


#st.write("""
# Simple Stock Price App

#Shown are the stock closing price and volume of Google
#""")

st.sidebar.header('User Input Parameters')

#user should know ticker code
ticker_symbol = st.sidebar.text_input('Ticker code', 'GOOGL')
st.write('The ticker is', ticker_symbol)

#checkboxes to show charts
chart_open = st.sidebar.checkbox('Open')
chart_high = st.sidebar.checkbox('High')
chart_low = st.sidebar.checkbox('Low')
chart_close = st.sidebar.checkbox('Close')
chart_volume = st.sidebar.checkbox('Volume')
chart_dividends = st.sidebar.checkbox('Dividends')
chart_stock = st.sidebar.checkbox('Stock Splits')


#get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

#get the historical prices for this ticker
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')
#Open High Low Close Volume Dividends Stock Splits

if chart_open:
  st.write("""
  ## Open price
  """)
  st.line_chart(ticker_df.Open)

if chart_high:
  st.write("""
  ## High price
  """)
  st.line_chart(ticker_df.High)

if chart_low:
  st.write("""
  ## Low price
  """)
  st.line_chart(ticker_df.Low)  

if chart_close:
  st.write("""
  ## Close price
  """)
  st.line_chart(ticker_df.Close)

if chart_volume:  
  st.write("""
  ## Volume price
  """)
  st.line_chart(ticker_df.Volume)

if chart_dividends:  
  st.write("""
  ## Dividends
  """)
  st.line_chart(ticker_df.Dividends)

if chart_stock:  
  st.write("""
  ## Stock Splits
  """)
  st.line_chart(ticker_df[('Stock Splits')])

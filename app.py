import streamlit as st
import pandas as pd


import yfinance as yf
import datetime

import graphs
import stock_symbol

st.header('My Stockmarket')

search_stock = st.sidebar.text_input("Enter the stock symbol")
button_clicked = st.sidebar.button("Search")
chart_choices = ['Plotly','Bollinger', 'Moving Avg', 'RSI']

today = datetime.date.today()
month_ago = today - datetime.timedelta(days=30)
start_date = st.sidebar.date_input('Start date', month_ago)
end_date = st.sidebar.date_input('End date', today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')


if search_stock is not None and len(str(search_stock)) > 0:
    df = yf.download(search_stock, start = start_date, end = end_date, progress = False)
    full_name = stock_symbol.getCompany(search_stock)
    st.write('Trends for Stocks belonging to '+ ",".join(full_name)  )
    select_choice = st.selectbox("Select Your Visualisation", chart_choices)
    if select_choice == 'Bollinger':
        graphs.bollinger_chart(df)
    elif select_choice == 'Moving Avg':
        graphs.moving_average_chart(df)
    elif select_choice == 'RSI':
        graphs.rsi_chart(df)
    elif select_choice == 'Plotly':
        graphs.area_chart(df)

else:
    st.write("Please enter correct symbol")



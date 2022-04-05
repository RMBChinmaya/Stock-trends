import streamlit as st
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator
import pandas as pd

import plotly.express as px

def bollinger_chart(df,search_stock):
    # Bollinger Bands
    li = list(search_stock.split(" "))
    if len(li) < 2:
        indicator_bb = BollingerBands(df['Close'])
        bb = df
        bb['bb_h'] = indicator_bb.bollinger_hband()
        bb['bb_l'] = indicator_bb.bollinger_lband()
        bb = bb[['Close','bb_h','bb_l']]
        st.write('Stock Bollinger Bands')
        st.line_chart(bb)
    else:
        st.write("This graph only works with one Stock at a time")

def moving_average_chart(df, search_stock):
    # Moving Average Convergence Divergence
    li = list(search_stock.split(" "))
    if len(li) < 2:
        macd = MACD(df['Close']).macd()
        st.write('Stock Moving Average Convergence Divergence (MACD)')
        st.area_chart(macd)
    else:
        st.write("This graph only works with one Stock at a time")

def rsi_chart(df, search_stock):
    # Resistence Strength Indicator
    li = list(search_stock.split(" "))
    if len(li) < 2:
        rsi = RSIIndicator(df['Close']).rsi()
        st.write('Resistence Strength Indicator of the Stock')
        st.line_chart(rsi)
    else:
        st.write("This graph only works with one Stock at a time")

def area_chart(df):
    stock_area = px.area(df['Close'])
    stock_area.update_xaxes(
        title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 7, label = '1W', step = 'day', stepmode = 'backward'),
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')]))
    )
    stock_area.update_yaxes(title_text = 'Close Price', tickprefix = '$')
    st.write('Stock Plotly')
    st.plotly_chart(stock_area, use_container_width=True)


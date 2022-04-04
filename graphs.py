import streamlit as st
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

import plotly.express as px


def bollinger_chart(df):
    # Bollinger Bands
    indicator_bb = BollingerBands(df['Close'])
    bb = df
    bb['bb_h'] = indicator_bb.bollinger_hband()
    bb['bb_l'] = indicator_bb.bollinger_lband()
    bb = bb[['Close','bb_h','bb_l']]
    st.write('Stock Bollinger Bands')
    st.line_chart(bb)

def moving_average_chart(df):
    # Moving Average Convergence Divergence
    macd = MACD(df['Close']).macd()
    st.write('Stock Moving Average Convergence Divergence (MACD)')
    st.area_chart(macd)

def rsi_chart(df):
    # Resistence Strength Indicator
    rsi = RSIIndicator(df['Close']).rsi()
    st.write('Stock RSI')
    st.line_chart(rsi)

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


#!/usr/bin/env python3

""" Author ArunSK(@arun7pulse) """

import streamlit as st
import pandas as pd

import requests

# url = "https://raw.githubusercontent.com/arun7pulse/askIndex/master/NIFTY%2050.csv"
# df = pd.read_csv(url)
# df.set_index('date', inplace=True)

# st.write("""
# # Thinking of investing in NIFTY 50 
# ### You'll find below the stock closing price and volume of NIFTY. 
# """)

# st.line_chart(df.close)
# st.line_chart(df.volume)

# url = "https://raw.githubusercontent.com/arun7pulse/askIndex/master/NIFTY%20BANK.csv"
# bf = pd.read_csv(url)
# bf.set_index('date', inplace=True)

# st.write("""
# # Thinking of investing in NIFTY BANK 
# ### You'll find below the stock closing price and volume of NIFTY. 
# """)

# st.line_chart(bf.close)
# st.line_chart(bf.volume)


import streamlit as st
import pandas as pd
import altair as alt

from urllib.error import URLError

@st.cache
def get_index_data():
  
    url = "https://raw.githubusercontent.com/arun7pulse/askIndex/master/NIFTY%2050.csv"
    nf = pd.read_csv(url)
    nf.set_index('date', inplace=True)
    
    url = "https://raw.githubusercontent.com/arun7pulse/askIndex/master/NIFTY%20BANK.csv"
    bf = pd.read_csv(url)
    bf.set_index('date', inplace=True)
    df = nf.append(bf)
    df.index = pd.to_datetime(df.index)
    return df

df = get_index_data()
symbol = st.radio("INdex you want to check ", ('NIFTY 50', 'NIFTY BANK'))
if not symbol:
    st.error("Please select at least one symbol.")
else:
    data = df[df['symbol'] == symbol]
    del data['symbol']  
    st.write("### NSE Index Data ", data.tail(100).sort_index(ascending=False))
    st.line_chart(data[['close']])

        

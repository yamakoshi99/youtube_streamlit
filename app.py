import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

st.title('米国株価可視化アプリ')

st.sidebar.write("""
    #GAFA株価
    こちらは株価可視化アプリです。
""")

st.sidebar.write("""
##日数指定
""")

days = st.sidebar.slider('日数',1 ,50,20)
st.write(f"""
### 過去 **{days}日間**のGAFAの株価
""")

@st.cache
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        #company = 'facebook'
            tkr = yf.Ticker(tickers[compny])
            hist = tkr.history(period=f'{days}d')
            hist.index = hist.index.strftime('%d %B %Y')
            hist = hist[['close']]
            hist = hist,T
            hist.index.name = 'Name'
            df = pd.concat([df,hidt])
{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import yfinance as yf\
import pandas as pd\
from sklearn.tree import DecisionTreeRegressor\
\
st.set_page_config(page_title="Gold/USD AI Signal", page_icon="\uc0\u55357 \u56520 ")\
\
st.title("\uc0\u55357 \u56522  AI Trading Signal for Gold (XAU/USD)")\
\
# Download Gold price data\
data = yf.download('XAUUSD=X', period='60d', interval='1h')\
data['Target'] = data['Close'].shift(-1)\
data = data.dropna()\
\
# AI model\
X = data[['Open', 'High', 'Low', 'Close']]\
y = data['Target']\
model = DecisionTreeRegressor(max_depth=5)\
model.fit(X, y)\
\
# Prediction\
latest = X.iloc[-1].values.reshape(1, -1)\
prediction = model.predict(latest)\
current_price = data['Close'].iloc[-1]\
\
# TP/SL setup\
profit_target = 5.0\
stop_loss_amount = 3.0\
\
# Signal logic\
if prediction[0] > current_price:\
    signal = "BUY"\
    take_profit = current_price + profit_target\
    stop_loss = current_price - stop_loss_amount\
    st.success(f"\uc0\u9989  Suggested Action: BUY")\
else:\
    signal = "SELL"\
    take_profit = current_price - profit_target\
    stop_loss = current_price + stop_loss_amount\
    st.error(f"\uc0\u10060  Suggested Action: SELL")\
\
# Display results\
st.write(f"**Current Price:** \{current_price:.2f\}")\
st.write(f"**Predicted Next Price:** \{prediction[0]:.2f\}")\
st.write(f"**Take Profit:** \{take_profit:.2f\}")\
st.write(f"**Stop Loss:** \{stop_loss:.2f\}")\
}
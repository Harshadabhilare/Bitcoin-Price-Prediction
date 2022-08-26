import streamlit as st
import pickle

st.set_page_config(page_title="Bitcoin Price Prediction",layout="centered")

st.title("Bitcoin Price Prediction ")


pickle_in = open('bitcoin_market_price.pkl', 'rb')
lr = pickle.load(open("bitcoin_market_price.pkl","rb"))

number1 = st.number_input('btc_market_cap')
number2 = st.number_input('btc_hash_rate')
number3 = st.number_input('btc_difficulty')
number4 = st.number_input('btc_trade_volume')
number5 = st.number_input('btc_cost_per_transaction')


if st.button("Predict"):
    pred = lr.predict([[number1, number2, number3, number4, number5]])[0]
    st.write("Price_prediction : ", pred)
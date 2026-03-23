# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Car Price Predictor", layout="wide")

st.title("🚗 Car Price Prediction")

st.sidebar.header("Enter Car Details")

# Inputs
vehicle_age = st.sidebar.slider("Vehicle Age", 0, 20, 5)
km_driven = st.sidebar.number_input("KM Driven", 0, 300000, 50000)

df = pd.read_csv("clean_data.csv")

brand = st.selectbox("Brand", sorted(df['brand'].unique()))
seller_type = st.selectbox("Seller Type", sorted(df['seller_type'].unique()))
fuel_type = st.selectbox("Fuel Type", sorted(df['fuel_type'].unique()))
transmission_type = st.selectbox("Transmission", sorted(df['transmission_type'].unique()))

mileage = st.sidebar.number_input("Mileage", 0.0, 40.0, 18.0)
engine = st.sidebar.number_input("Engine (CC)", 500, 5000, 1200)
max_power = st.sidebar.number_input("Max Power", 20.0, 300.0, 80.0)
seats = st.sidebar.slider("Seats", 2, 10, 5)

# Input DataFrame
input_data = pd.DataFrame({
    'vehicle_age': [vehicle_age],
    'km_driven': [km_driven],
    'brand': [brand],
    'seller_type': [seller_type],
    'fuel_type': [fuel_type],
    'transmission_type': [transmission_type],
    'mileage': [mileage],
    'engine': [engine],
    'max_power': [max_power],
    'seats': [seats]
})

# Prediction
if st.button("Predict Price"):
    try:
        pred = model.predict(input_data)[0]
        st.success(f"Estimated Price: ₹{pred:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
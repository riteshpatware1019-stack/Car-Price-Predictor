import streamlit as st
import pandas as pd
import pickle

# Load dataset
car = pd.read_csv('./datasets/cleaned_car.csv')

# Load trained model
model = pickle.load(open('CarPredicaitonModel.pkl', 'rb'))

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Car Price Prediction")
st.write("Enter the car details to predict its price")

# Dropdown options
car_name = sorted(car['name'].unique())
companies = sorted(car['company'].unique())
fuel_types = sorted(car['fuel_type'].unique())

# User Inputs
car_name = st.selectbox(
    "Select Car Name",
    sorted(car['name'].unique())
)
company = st.selectbox("Select Company", companies)

year = st.number_input(
    "Manufacturing Year",
    min_value=2000,
    max_value=2025,
    value=2018
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=20000
)

fuel_type = st.selectbox(
    "Fuel Type",
    fuel_types
)

# Predict Button
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "name": [car_name],
        "company": [company],
        "year": [year],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type]
    })
    prediction = model.predict(input_df)

    st.success(
        f"Estimated Car Price: ₹ {int(prediction[0]):,}"
    )

st.markdown("---")
st.write("Thank You")
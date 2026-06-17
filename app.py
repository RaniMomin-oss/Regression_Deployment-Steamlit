import numpy as np
import pandas as pd
import pickle
import streamlit as st

model= pickle.load(open("regression.pickle", "rb"))

st.title("Health Insurance Price Prediction App")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120)

sex = st.selectbox("Sex", options=["Female", "Male"])

bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, step=0.1)

children = st.number_input("Number of Children", min_value=0, max_value=10)

smoker = st.selectbox("Smoker", options=["No", "Yes"])

region = st.selectbox("Region", options=["Southeast", "Southwest", "Northeast", "Northwest"])

# Encoding categorical variables
sex= 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0    

# Region is one hot encoded

region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0

# Prepare the input data for prediction

if st.button("Predict"):
    features = np.array([[age, sex, bmi, children, smoker, region_northwest, region_southeast, region_southwest]])
    prediction = model.predict(features)
    st.success(f"Predicted Insurance Cost: ${prediction[0]}")   
    

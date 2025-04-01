import streamlit as st  # type: ignore
import pickle
import numpy as np  # type: ignore

# Load the trained model
with open("house_sales.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("\U0001F3E1 House Price Prediction App")
st.write("Enter the details below to predict the house price:")

# Input Fields
sqft_living = st.number_input("Living Area (sq ft)", min_value=500, max_value=10000, value=2000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
floors = st.number_input("Number of Floors", min_value=1, max_value=3, value=1)
waterfront = st.selectbox("Waterfront View", [0, 1])  # 1 = Yes, 0 = No
view = st.slider("View (0-4)", 0, 4, 0)
condition = st.slider("Condition of House (1-5)", 1, 5, 3)
grade = st.slider("Grade (1-13)", 1, 13, 7)
sqft_lot = st.number_input("Lot Size (sq ft)", min_value=500, max_value=50000, value=5000)
sqft_above = st.number_input("Above Ground Living Area (sq ft)", min_value=500, max_value=10000, value=1500)
sqft_basement = st.number_input("Basement Area (sq ft)", min_value=0, max_value=5000, value=500)
yr_built = st.number_input("Year Built", min_value=1900, max_value=2023, value=2000)
yr_renovated = st.number_input("Year Renovated", min_value=0, max_value=2023, value=0)
zipcode = st.number_input("Zipcode", min_value=98000, max_value=98200, value=98178)
lat = st.number_input("Latitude", min_value=47.0, max_value=48.0, value=47.5112)
long = st.number_input("Longitude", min_value=-123.0, max_value=-121.0, value=-122.257)
sqft_living15 = st.number_input("Living Area of 15 Nearest Neighbors (sq ft)", min_value=500, max_value=10000, value=2000)
sqft_lot15 = st.number_input("Lot Size of 15 Nearest Neighbors (sq ft)", min_value=500, max_value=50000, value=5000)

# Compute missing feature: House Age
house_age = 2023 - (yr_renovated if yr_renovated > 0 else yr_built)

# Make prediction
if st.button("Predict Price"):
    input_data = np.array([[
        sqft_living, bedrooms, bathrooms, floors, waterfront, view, condition, grade, sqft_lot,
        sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, sqft_living15, sqft_lot15, house_age
    ]])
    predicted_price = model.predict(input_data)[0]
    
    st.success(f"\U0001F3E0 Estimated House Price: **${predicted_price:,.2f}**")

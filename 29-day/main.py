import numpy as np
import pickle
import streamlit as st

# Load model once at startup
@st.cache_resource
def load_model():
    return pickle.load(open('pipe.pkl', 'rb'))

pipe = load_model()

st.title("Titanic Death Predictor")

col1, col2 = st.columns(2)

with col1:
    pclass = st.number_input("Select the Passenger class", min_value=1, max_value=3, value=1)
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    age = st.number_input("What's the Age?", min_value=0, max_value=120, value=25)

with col2:
    sbs = st.number_input("Siblings or Spouse traveling with?", min_value=0, value=0)
    chpr = st.number_input("Children or Parents traveling with?", min_value=0, value=0)
    fare = st.number_input("Enter the fare", min_value=0.0, value=50.0)
    embark = st.selectbox("Select the embark port", ["S", "C", "Q"])

if st.button("Predict", type="primary"):
    test_input = np.array([pclass, gender, age, sbs, chpr, fare, embark], dtype=object).reshape(1, 7)
    prediction = pipe.predict(test_input)[0]
    result = "Not Survived" if prediction == 0 else "Survived"
    st.success(f"Prediction: **{result}**")
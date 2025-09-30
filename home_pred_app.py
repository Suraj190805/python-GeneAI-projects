import streamlit as st

#load my predictive model
import pickle
model = pickle.load(open("model.pkl","rb"))

st.title("Home Price Prediction Application")

myarea = st.text_input("Enter area in square feet:")

bedrooms = st.text_input("Enter total bedrooms:")

Age = st.text_input("Enter age of the home:")

if st.button("Predict"):
    if myarea and bedrooms and Age :
        pred = model.predict([[int(myarea),int(bedrooms),int(Age)]])
        st.write(pred)

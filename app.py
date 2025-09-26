import streamlit as st
import PIL.Image
import os
import google.generativeai as genai

#setup api
os.environ['GOOGLE_API_KEY'] = "AIzaSyCcLBRARVE2y7Gxu6A-irRxaknvTti1XJE"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

#load our pretrained moddel 
model = genai.GenerativeModel("models/gemini-2.5-pro")

#app creation
def fetch_details(img,query):
    response = model.generate_content([query,img]).text
    return response


st.title("Fetching Image details using GEN AI")
uploaded_image=  st.file_uploader("upload an image to fetch detail")
query = st.text_input("What details do u want from the uploaded image: ")
if st.button ("Generate"):
    if uploaded_image and query:
        img = PIL.Image.open(uploaded_image)
        result = fetch_details(img,query)
        st.write(result)
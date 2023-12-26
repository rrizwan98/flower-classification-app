import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from PIL import Image
import os
from dotenv import load_dotenv, find_dotenv
# import textwrap

load_dotenv()

genai.configure(api_key="AIzaSyCGEUherYJud9qvqRZ9EWW_tvbOJla5mjM")

st.set_page_config(page_title="FR" ,page_icon="📸", layout="centered", initial_sidebar_state='collapsed')

st.header("FLOWER RECOGNITION APP (FR)")

st.write("""This app can help's you FLOWER RECOGNITION WORLDWIDE. 
         this model will gives you the name of the flower and its family name.""")

uploaded_file = st.file_uploader("Choose an Image file", accept_multiple_files=False, type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    bytes_data = uploaded_file.getvalue()

generate = st.button("Tell me about the image!")
bot_instructions = """if Flower is present in thine image: (your responsibility is to Identify the flower and its family name in the image.)  
                        If the flower isn't found in the image: (Please insert only flower image because this model is trained to identify only flowers.))""" 
if generate:

    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(
        glm.Content(
            parts = [
                glm.Part(text=bot_instructions),
                glm.Part(
                    inline_data=glm.Blob(
                        mime_type='image/jpeg',
                        data = bytes_data
                    )
                ),
            ],
        ),
        stream=True)
    
    response.resolve()
    st.write(response.text)
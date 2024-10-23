# Q&A Chatbot
#from langchain.llms import OpenAI

import os
from dotenv import load_dotenv
import streamlit as st
import textwrap
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Function to handle image upload and setup for the model
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the uploaded file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get MIME type of the file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("End to End Multi Language Inovice Extractor Project using Gemini Pro LLM Model")

# Input prompt and file upload
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "Webp"])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button
submit = st.button("Tell me about the Inovoice")

# Input prompt for the AI model
input_prompt = textwrap.dedent("""
    You are an expert in understanding invoices.
    You will receive input images as invoices &
    you will have to answer questions based on the input image.
""")

# If submit button is clicked
if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please upload an image before submitting.")

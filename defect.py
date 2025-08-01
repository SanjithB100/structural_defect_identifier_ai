import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai 
from PIL import Image

st.set_page_config(page_title="Defect Detection", page_icon="֎🇦🇮", layout="wide")

st.title(":blue[AI Aissistant :red[ for Structural Defect Detection and Analysis]]")
st.subheader(":blue[This the prototype of an AI assistant that can detect and analyze structural defects in images.]")

with st.expander("About the Application"):
    st.markdown("""
    This project aims to develop an AI assistant that can assist in the detection and analysis of structural defects in images.
    The assistant uses Google Generative AI to analyze images and provide insights on potential defects.
    - **Defect Detection AI** - Automatically detects and analyzes structural defects in images using AI.
    - **Image Analysis** - Provides detailed analysis of structural defects in images.
    - **Recommendations** - Offers recommendations for addressing detected defects.
    - **Report Generation** - Generates reports based on the analysis of structural defects.
    - **User-Friendly Interface** - Easy-to-use interface for uploading images and viewing analysis results.
    """)
    
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)

input_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if input_image :
    img = Image.open(input_image)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
if st.button('Analyze Image'):
    with st.spinner('Analyzing...'):
        try:
            prompt=f'''Does the crack as shown in the image above have any structural defects?
            Also, provide recommendations for addressing the detected defects.Does it have uneven surface, or any other structural defects?
            will it has the water leakage or any other issues? is that the Gap and damage in the structure? 
            1.What is the specific defect you are observing?
            2.Where is the defect located?
            3.When did you first notice it, and has it changed over time?
            4.What is the size and pattern of the defect?
            5.Are there any associated signs (e.g., sounds, water stains, sticking doors)
            6. What is the impact on non-structural elements (e.g., doors, windows)'''
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content([prompt,img])
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
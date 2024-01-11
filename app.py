from dotenv import load_dotenv
import streamlit as st
from utils import get_text_response, get_image_response
from PIL import Image

load_dotenv()

def main():
    st.set_page_config(page_title="Gemini Application")
    st.header("Gemini Application")
    st.write("env loaded successfully")

    model_type = st.selectbox("Select Model Type", ["Text", "Image"])

    if model_type == "Text":
        gemini_text_app()
    elif model_type == "Image":
        gemini_vision_app()

def gemini_text_app():
    st.subheader("Text Model")
    input_text = st.text_input("Input", key='input')
    submit = st.button("Ask me the question")

    if submit:
        response = get_text_response(input_text)
        st.subheader("The response is ")
        st.write(response)

def gemini_vision_app():
    st.subheader("Image Model")
    uploaded_file = st.file_uploader("Choose an Image: ", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    input_text = st.text_input("Input Prompt: ", key='input')
    submit = st.button("Tell me about the image")

    if submit:
        response = get_image_response(input_text, image)
        st.subheader("The response is ")
        st.write(response)

if __name__ == "__main__":
    main()

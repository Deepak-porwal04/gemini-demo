# gemini_models.py
import os
import google.generativeai as gai
from PIL import Image
from dotenv import load_dotenv

# class GeminiTextModel:
#     def __init__(self):
#         self.api_key = os.environ.get("API_KEY")
#         gai.configure(api_key=self.api_key)
#         self.model = gai.GenerativeModel('gemini-pro')
def load_api_key():
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    return api_key


def get_text_response(prompt):
    gai.configure(api_key=load_api_key())
    model = gai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# class GeminiVisionModel:
#     def __init__(self):
#         self.api_key = os.environ.get("API_KEY")
#         gai.configure(api_key=self.api_key)
#         self.model = gai.GenerativeModel('gemini-pro-vision')

def get_image_response(input_text, img):
    gai.configure(api_key=load_api_key())
    model = gai.GenerativeModel('gemini-pro-vision')
    if input_text != "":
        response = model.generate_content([input_text, img])
    else:
        response = model.generate_content(img)
    return response.text

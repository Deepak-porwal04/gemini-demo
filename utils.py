import os
import google.generativeai as gai
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    return api_key


def get_text_response(prompt):
    gai.configure(api_key=load_api_key())
    model = gai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def get_image_response(input_text, img):
    gai.configure(api_key=load_api_key())
    model = gai.GenerativeModel('gemini-pro-vision')
    if input_text != "":
        response = model.generate_content([input_text, img])
    else:
        response = model.generate_content(img)
    return response.text

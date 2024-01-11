# Gemini Demo App

**Explore the power of text and image generation with Gemini models!**


This Streamlit app allows you to interact with both text and image models from Google AI's Gemini family, enabling you to generate text, translate languages, write different creative text formats, and answer your questions in an informative way.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)

## Features

- **Flexible Model Selection:** Choose between text and image models based on your needs.
- **Text Generation:** Generate text responses to your prompts.
- **Image Generation:** Generate text descriptions of images you upload.
- **Combined Input:** Generate text responses based on both text prompts and images.

## Installation

1. Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```
2. Set up the environment variables:

 - Create a `.env` file in the project root directory.

- Add your Gemini API key to the `.env` file:
```bash
API_KEY=your_gemini_api_key
  ```
3. Run the Streamlit application:
  ```
  streamlit run app.py
  ```

## Prerequisites

- `streamlit`: Streamlit library for building web applications.
- `google.generativeai`: Gemini API for generative models.
- `PIL`: Python Imaging Library for handling images.
- `python-dotenv`: To store the environment variables secretly

## Usage

1. Upon running the application, you will see a Streamlit interface.

2. Choose the model type (Text or Image) from the dropdown menu.

3. For the Text model:

- Enter your text input in the provided text box.
- Click the "Ask me the question" button to get a response.
4. For the Image model:

- Upload an image using the file uploader.
- Enter a text prompt in the provided text box.
- Click the "Tell me about the image" button to get a response.




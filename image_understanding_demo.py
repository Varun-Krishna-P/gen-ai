#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:23:27 2025

@author: garuda
"""
import os
from google import genai
from google.genai.types import HttpOptions, Part


# authenticating to gcp environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = input('Enter the path of the service account key: ')
PROJECT_ID = input("Enter the project id: ")
LOCATION = input('Enter the location: ')
os.environ['GOOGLE_CLOUD_PROJECT'] = PROJECT_ID
os.environ['GOOGLE_CLOUD_LOCATION'] = LOCATION
os.environ['GOOGLE_GENAI_USE_VERTEXAI'] = 'True'
text_prompt = input("Enter the text prompt: ")


client = genai.Client(http_options=HttpOptions(api_version="v1"))

# Read content from a local file
with open("images/image1.jpeg", "rb") as f:
    local_file_img_bytes = f.read()
    
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=[
        text_prompt,
        Part.from_bytes(data=local_file_img_bytes, mime_type="image/jpeg")
    ])

print(response.text)

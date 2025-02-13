#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 07:40:21 2025

@author: garuda
"""

from google.auth import default
import google.auth.transport.requests
import openai
import os

# authenticating to gcp environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = input('Enter the path of the service account key: ')
PROJECT_ID = input("Enter the project id: ")
LOCATION = input('Enter the location: ')

# Programmatically get an access token
credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
credentials.refresh(google.auth.transport.requests.Request())


# OpenAI Client
client = openai.OpenAI(
    base_url=f"https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/openapi",
    api_key=credentials.token,
)

# client = openai.OpenAI()

text_prompt = input('Enter the text to generate: ')
response = client.chat.completions.create(
    model="google/gemini-1.5-flash-002",
    messages=[{"role": "user", "content": text_prompt}],
)

print(response)
print(response.choices[0].message.content)
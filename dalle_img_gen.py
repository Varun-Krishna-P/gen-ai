#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:42:04 2025

@author: garuda
"""

from utils import authenticate
import base64
import time


project_id = input("Please enter the project id: ")
location = input("Please enter the location: ")
client = authenticate(location, project_id)
text_prompt = input('Enter the text to genereate image: ')
response = client.images.generate(
    model="dall-e-3",
    prompt=text_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)

# img_bytes = base64.b64decode(response.data[0])
# with open(f"./output/{time.time()}.png", "wb") as f:
#     f.write(img_bytes)
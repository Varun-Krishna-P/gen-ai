#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 21:29:10 2025

@author: garuda
Azure open ai completion demo
"""

from utils.azure_openai_auth import authenticate
import os

client = authenticate()

text_prompt = input("please enter the text prompt: ")
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are an AI assistant that helps people find information."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": text_prompt
            }
        ]
    }
]

messages = chat_prompt
deployment =  os.getenv("DEPLOYMENT_NAME", "gpt-4o") 
response = client.chat.completions.create(  
    model=deployment,  
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False  
)  

responseText = response.choices[0].message.content
print("prompt: " + text_prompt + "\nresponse: "+responseText)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 20:46:49 2025

@author: garuda
"""

import base64
from utils.azure_openai_auth import authenticate
import time

client = authenticate(api_version="2024-12-01-preview")

completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "user",
            #"content": "Is a golden retriever a good family dog?"
            "content": input("enter the text prompt to generate audio: ")
        }
    ]
)

#print(completion.choices[0]. message.audio.transcript)

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open(f"./output/audio/{time.time()}.wav", "wb") as f:
    f.write(wav_bytes)
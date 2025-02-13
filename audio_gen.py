#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:18:35 2025

@author: garuda
"""

from utils import authenticate
import base64
import time

project_id = input("Please enter the project id: ")
location = input("Please enter the location: ")
audio_format = "mp3"
client = authenticate(location, project_id)

text_prompt = input('Enter the text to genereate audio: ')

#ash, ballad, coral, sage, and verse - alloy, echo, and shimmer;
completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "ash", "format": audio_format},
    messages=[
        {
            "role": "user",
            "content": text_prompt
        }
    ]
)

print(completion.choices[0])

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open(f"./output/audio/{time.time()}.{audio_format}", "wb") as f:
    f.write(wav_bytes)
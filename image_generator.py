#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:52:13 2025

@author: garuda
"""
# from openai import OpenAI


# prmpt = input("Please provide a text to generate an image:  ")
# client = OpenAI(
#   api_key=os.environ['API_KEY']
# )




# completion = client.chat.completions.create(
#     model="gpt-4o-mini-2024-07-18",
#     messages=[
        
#         {
#             "role": "user",
#             "content": prmpt
#         }
#     ]
# )

# print(completion.choices[0].message)

# from google import genai
# from google.genai import types
# from PIL import Image
# from io import BytesIO

# client = genai.Client(api_key=os.environ['API_KEY'])
# response = client.models.generate_images(
#     model='imagen-3.0-generate-002',
#     prompt=prmpt,
#     config=types.GenerateImagesConfig(
#         number_of_images= 1,
#     )
# )
# for generated_image in response.generated_images:
#   image = Image.open(BytesIO(generated_image.image.image_bytes))
#   image.show()
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import time

# import os
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']=input("Please provide the path to the service accoung key json file: ")

PROJECT_ID = input("Enter the project id: ")
output_file = f'{PROJECT_ID}_{time.time()}.png'
prmpt = input("Please provide a text to generate an image:  ")
vertexai.init(project=PROJECT_ID, location="us-west1")
model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
images = model.generate_images(
    prompt=prmpt,
    # Optional parameters
    number_of_images=4,
    language="en",
    # You can't use a seed value and watermark at the same time.
    # add_watermark=False,
    # seed=100,
    aspect_ratio="1:1",
    safety_filter_level="block_some",
    person_generation="dont_allow",
)


if images:
    images[0].save(location=output_file, include_generation_parameters=False)

    # Optional. View the generated image in a notebook.
    for img in images:
        img.show()
        #images[0].show()

    print(f"Created output image using {len(images[0]._image_bytes)} bytes")
else:
    print("Try a different prompt. No image generated")



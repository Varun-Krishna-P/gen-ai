#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 13:17:38 2025

@author: garuda
"""

from utils.azure_openai_auth import authenticate

client = authenticate("2024-02-01")
model_name = "text-embedding-3-small"
deployment = "text-embedding-3-small"


response = client.embeddings.create(
    input=input('Enter the string to convert to embeddings: '),
    model=deployment
)

print(response.data[0].embedding)


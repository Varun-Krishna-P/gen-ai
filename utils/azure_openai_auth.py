#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 21:37:07 2025

@author: garuda
"""
import os
from openai import AzureOpenAI



def authenticate():
    client = AzureOpenAI(
            azure_endpoint=os.getenv("AOAI_ENDPOINT", input("please enter the azure open api endpoint: ")),
            api_version="2024-05-01-preview",
            api_key=os.getenv("AOAI_KEY", input("please enter the api key: "))
        )
    return client
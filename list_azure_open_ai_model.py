#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 20:58:12 2025

@author: garuda
"""

"""
Displays the list of models deployed in Azure open API
"""

import os
import json
from openai import AzureOpenAI

client = AzureOpenAI(
        azure_endpoint=os.getenv("AOAI_ENDPOINT", input("please enter the azure open api endpoint: ")),
        api_version="2024-05-01-preview",
        api_key=os.getenv("AOAI_KEY", input("please enter the api key: "))
    )

# call the models api to retreive the list

models = client.models.list()

# save to file

with open('azure-oai-models.json', 'w') as file:
    models_dict = [model.__dict__ for model in models]
    json.dump(models_dict, file)
    

# print out the names of all the available models, and their capabilities

for model in models:
    print("ID: ", model.id)
    print("Current status: ", model.lifecycle_status)
    print("Model capabilities: ", model.capabilities)
    print("----------------------------")
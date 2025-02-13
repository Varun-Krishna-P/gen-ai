#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:59:45 2025

@author: garuda
"""

import os
import openai
from google.auth import default
import google.auth.transport.requests


def authenticate(location, project_id):
    # authenticating to gcp environment
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = input('Enter the path of the service account key: ')    
    
    # Programmatically get an access token
    credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    credentials.refresh(google.auth.transport.requests.Request())


    # OpenAI Client
    client = openai.OpenAI(
        base_url=f"https://{location}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{location}/endpoints/openapi",
        api_key=credentials.token,
    )
    
    return client
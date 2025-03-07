#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 20:15:50 2025

@author: garuda
"""

from utils.azure_openai_auth import authenticate
import PyPDF2


client = authenticate()



# Step 1: Extract text from PDF
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        # Loop through all pages of the PDF
        for page in reader.pages:
            text += page.extract_text()
    return text

# Step 2: Query GPT-3 with the extracted text
def chat_with_pdf(pdf_text, user_query):
    """
    Takes the extracted PDF text and a user query, then returns a response based on the PDF content.
    """
        
    # Create a prompt combining the extracted PDF text and the user's question
    prompt = f"Answer the following question based on the content of this document: \n{pdf_text}\n\nQuestion: {user_query}\nAnswer:"
    
    #Prepare the chat prompt 
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
                    "text": prompt
                }
            ]
        }
    ] 
    
    # Include speech result if speech is enabled  
    messages = chat_prompt  
    # Generate a response from GPT-3
    response = client.chat.completions.create(
        model="gpt-4o",  # Or any other model you'd like
        messages=messages,
        max_tokens=150,
        temperature=0.7,
        stream=False
    )
    
    # Return the model's answer
    #print(response.to_json)
    return response.choices[0].message.content.strip()

# Step 3: Interact with the chatbot
def main():
    # Extract text from the PDF
    pdf_path = input('your_pdf_file.pdf')  # Replace with the path to your PDF file
    pdf_text = extract_text_from_pdf(pdf_path)

    print("Chatbot is ready! Ask a question based on the PDF content.")
    print("Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_query = input("You: ")
        
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get response from the chatbot
        answer = chat_with_pdf(pdf_text, user_query)
        
        # Output the answer
        print(f"Chatbot: {answer}")

# Start the chatbot
if __name__ == "__main__":
    main()

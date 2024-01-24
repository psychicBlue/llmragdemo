import os
import requests

class llm_class:
    def __init__(self, name):
        self.name = name

    def query(self, prompt, API_URL, headers):
        payload = {
            "inputs": prompt,
            "parameters": { #Try and experiment with the parameters
                "max_new_tokens": 250,
                "temperature": 0.6,
                "top_p": 0.9,
                "do_sample": False,
                "return_full_text": False
            }
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()[0]['generated_text']

    def insert_rag(self, user_file_path):
        # Read txt for RAG
        file_path = user_file_path #"rag_txt.txt"

        # Check if the file exists
        if os.path.isfile(file_path):
            # Open the file in read mode
            with open(file_path, 'r') as file:
                # Read the contents of the file
                contents = file.read()
        return contents
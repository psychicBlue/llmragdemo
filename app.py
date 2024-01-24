import os
import requests
import tkinter as tk
from tkinter import Entry, Label, Button, scrolledtext
from tkinter import messagebox
from llm_class import llm_class

os.environ["API_TOKEN"] = ""

API_TOKEN = os.environ["API_TOKEN"] #Set a API_TOKEN environment variable before running
API_URL = "https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0" #Add a URL for a model of your choosing
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_response():
    question = entry_question.get()
    context = llm_instance.insert_rag('rag_txt.txt')
    prompt = f"""Use the following context to answer the question at the end.

    {context}

    Question: {question}
    """

    response = llm_instance.query(prompt, API_URL, headers)
    text_response.config(state=tk.NORMAL)
    text_response.delete(1.0, tk.END)
    text_response.insert(tk.END, response)
    text_response.config(state=tk.DISABLED)

# Create instance of LLM class
llm_instance = llm_class("llm_example_1")

# Sample question
#question = "What kind of creatures would survivers face in a post-apocalyptic world?"

# Create the main window
window = tk.Tk()
window.title("LLM Question Generator")

# Create and pack GUI elements
label_question = Label(window, text="Enter your question:")
label_question.pack(pady=10)

entry_question = Entry(window, width=50)
entry_question.pack(pady=10)

button_generate = Button(window, text="Generate Response", command=generate_response)
button_generate.pack(pady=10)

text_response = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=10, state=tk.DISABLED)
text_response.pack(pady=10)

window.mainloop()




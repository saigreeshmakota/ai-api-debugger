import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# 🔥 THIS LINE IS THE FIX
API_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

def call_llm(prompt):
    if not API_KEY:
        raise ValueError("API key not found")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    return response
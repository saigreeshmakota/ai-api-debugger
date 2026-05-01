import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    try:
        return st.secrets["OPENAI_API_KEY"]   # deployed
    except Exception:
        return os.getenv("OPENAI_API_KEY")    # local

def call_llm(prompt):
    API_KEY = get_api_key()

    if not API_KEY:
        raise ValueError("API key not found")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        # 🔥 REQUIRED for OpenRouter
        "HTTP-Referer": "https://naqe6v4bshlcjkgoksacu8.streamlit.app",
        "X-Title": "AI API Debugger"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    return response
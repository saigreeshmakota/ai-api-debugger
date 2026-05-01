import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    try:
        return st.secrets["OPENAI_API_KEY"]   # for deployed app
    except:
        return os.getenv("OPENAI_API_KEY")    # for local

def call_llm(prompt):
    API_KEY = get_api_key()

    if not API_KEY:
        raise ValueError("API key not found")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }

    return requests.post(url, headers=headers, json=data)
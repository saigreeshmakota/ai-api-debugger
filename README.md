# 🚀 AI API Playground & Debugger

An interactive web application to test, analyze, and debug API responses in real time.  
Built using Python and Streamlit, this tool helps developers understand API behavior, measure latency, and troubleshoot errors effectively.

---

## 🔗 Live Demo
👉 https://naqe6v4bshlcjkgoksacu8.streamlit.app/

---

## 🔍 Overview

Working with APIs can be challenging when requests fail or responses behave unexpectedly.  
This project provides a simple interface to:

- Send prompts to AI APIs  
- View responses instantly  
- Analyze latency and status codes  
- Debug errors in a clear and structured way  

---

## ⚙️ Features

- 💬 Send prompts to LLM APIs  
- ⚡ Measure response latency  
- 📊 Display status codes  
- ❌ Clear error handling and debugging  
- 🧪 API testing playground  
- 🔁 Supports multiple test scenarios  

---

## 🧰 Tech Stack

**Frontend / UI**
- Streamlit

**Backend**
- Python

**Libraries**
- requests  
- python-dotenv  

**API Integration**
- OpenRouter (Free LLM models – Mistral / LLaMA)

---

## 📁 Project Structure
ai-api-debugger/
│
├── app.py # Streamlit UI
├── api_client.py # API request logic
├── utils.py # Helper functions (latency, error parsing)
├── requirements.txt
└── README.md

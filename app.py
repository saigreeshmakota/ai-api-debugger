import streamlit as st
from api_client import call_llm
from utils import measure_latency, parse_error

st.set_page_config(page_title="AI API Debugger")

st.title("🚀 AI API Playground + Debugger")

prompt = st.text_area("Enter your prompt:")

if st.button("Send Request"):
    if not prompt:
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Calling API..."):
            response, latency = measure_latency(call_llm, prompt)

        st.subheader("📊 Response Info")
        st.write(f"Status Code: {response.status_code}")
        st.write(f"Latency: {latency} sec")

        if response.status_code == 200:
            data = response.json()
            output = data["choices"][0]["message"]["content"]
            st.success("✅ Success")
            st.write(output)
        else:
            error_msg = parse_error(response)
            st.error(f"❌ Error: {error_msg}")
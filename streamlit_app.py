import streamlit as st
from openai import OpenAI

OPENAI_API_KEY = st.sidebar.text_input("OpenAI API Key", type="password")
client = OpenAI(
    api_key=OPENAI_API_KEY
)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

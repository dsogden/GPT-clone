import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
# from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.title("ChatGPT-like Clone")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv('LANGSMITH_PROJECT')
os.environ["LANGSMITH_ENDPOINT"] = os.getenv('LANGSMITH_ENDPOINT')

model = ChatOpenAI(model='gpt-3.5-turbo')

messages = [
    SystemMessage('Translate the following form English to German'),
    HumanMessage('What is the date?')
]

st.write(
    model.invoke(messages).content
)
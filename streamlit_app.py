import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like Clone")
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

def generate_response(input_text: str, client: any) -> None:
        response = client.responses.create(
            model=st.session_state['openai_model'],
            instructions="Talk like a pirate.",
            input=input_text,
        )
        return response.output_text

if OPENAI_API_KEY.startswith('sk-'):
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )

    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"
    
    input_text = 'What happens when you walk the plank?'
    response = generate_response(input_text, client)
    st.write(response)

else:
    st.write('Please enter your OpenAI key!')
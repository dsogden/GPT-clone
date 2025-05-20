import streamlit as st
from openai import OpenAI

OPENAI_API_KEY = st.sidebar.text_input("OpenAI API Key", type="password")
st.write(OPENAI_API_KEY)
if OPENAI_API_KEY is not None:
    st.write('accepted the key')
    # client = OpenAI(
    #     api_key=OPENAI_API_KEY
    # )

    # # Set a default model
    # if "openai_model" not in st.session_state:
    #     st.session_state["openai_model"] = "gpt-3.5-turbo"


    #     response = client.responses.create(
    #         model=st.session_state['openai_model'],
    #         instructions="Talk like a pirate.",
    #         input="Are semicolons optional in JavaScript?",
    #     )

    #     st.write(response.output_text)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

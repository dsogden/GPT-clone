import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like Clone")
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

# def generate_response(input_text: str, client: any) -> None:
#         response = client.responses.create(
#             model=st.session_state['openai_model'],
#             instructions="Talk like a pirate.",
#             input=input_text,
#         )
#         return response.output_text

if OPENAI_API_KEY is not None:
    client = OpenAI(
        api_key=OPENAI_API_KEY
    )

    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    # st.write('Hello, what I can you help you with?')
    if prompt := st.chat_input('Ask anything'):
        st.session_state.messages.append(
            {
                'role': 'user',
                'content': prompt
            }
        )
        with st.chat_message('user'):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )
else:
    st.write('Please enter your OpenAI key!')
import streamlit as st
import requests

st.title("Chatbot GPT-Clone")
if "messages" not in st.session_state:
    st.session_state.messages = []
chatbot_url = "http://127.0.0.1:8000/chatbot"

def main():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask anything"):
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )
        with st.chat_message('user'):
            st.markdown(prompt)

        with st.chat_message('assistant'):
            data = {"query": prompt}
            output = requests.post(chatbot_url, json=data)
            response = output.json()['response']
            
            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

if __name__ == "__main__":
    main()
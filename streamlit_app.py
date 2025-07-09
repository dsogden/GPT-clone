# import streamlit as st
# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage
# from langgraph.checkpoint.memory import MemorySaver
# from langgraph.graph import START, MessagesState, StateGraph
# import os
# from dotenv import load_dotenv
# import time

# st.title("ChatGPT-like Clone")

# load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
# os.environ["LANGSMITH_PROJECT"] = os.getenv('LANGSMITH_PROJECT')
# os.environ["LANGSMITH_ENDPOINT"] = os.getenv('LANGSMITH_ENDPOINT')

# model = ChatOpenAI(model='gpt-3.5-turbo')

# # Define the function that calls the model
# def call_model(state: MessagesState):
#     response = model.invoke(state["messages"])
#     return {"messages": response}

# # Define a new graph
# workflow = StateGraph(state_schema=MessagesState)

# # Define the (single) node in the graph
# workflow.add_edge(START, "model")
# workflow.add_node("model", call_model)

# # Add memory
# memory = MemorySaver()
# app = workflow.compile(checkpointer=memory)
# config = {"configurable": {"thread_id": "abc123"}}

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# def stream_data(input_text):
#     for word in input_text.split(' '):
#         yield word + ' '
#         time.sleep(0.02)

# def main():
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     if prompt := st.chat_input("Ask anything"):
#         st.session_state.messages.append(
#             {"role": "user", "content": prompt}
#         )
#         with st.chat_message('user'):
#             st.markdown(prompt)
#             input_message = [HumanMessage(prompt)]

#         with st.chat_message('assistant'):
#             output = app.invoke({"messages": input_message}, config)
#             response = output['messages'][-1].content
            
#             st.markdown(response)

#         st.session_state.messages.append(
#             {"role": "assistant", "content": response}
#         )

# if __name__ == '__main__':
#     main()
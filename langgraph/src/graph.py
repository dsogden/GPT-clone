from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict
from langchain_core.runnables import RunnableConfig
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")
LLM_MODEL = os.environ.get("LLM_MODEL")

MODELS = {
    'openai': init_chat_model(model=LLM_MODEL, api_key=API_KEY)
}

class Configuration(TypedDict):
    model_name: str

@dataclass
class State(MessagesState):
    """Input state for the agent."""
    messages: list[str]

def call_model(state: State, config: RunnableConfig) -> Dict[str, Any]:
    """Process input and returns output."""
    model_name = config["configurable"].get("model_name")
    model = MODELS[model_name]
    response = model.invoke(state["messages"])
    return {"messages": [response]}

graph = (
    StateGraph(State, config_schema=Configuration)
    .add_node(call_model)
    .add_edge("__start__", "call_model")
    .compile(name="Graph")
)

input_message = {"role": "user", "content": "What is 3 + 3"}
config = Configuration(model_name="openai")
result = graph.invoke({"messages": [input_message]}, config=config)
print(result["messages"][-1].content)

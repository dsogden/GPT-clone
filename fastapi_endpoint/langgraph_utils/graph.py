from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict
from langchain_core.runnables import RunnableConfig
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver

import os
from dotenv import load_dotenv

load_dotenv()

# api key and llm model name
API_KEY = os.environ.get("OPENAI_API_KEY")
LLM_MODEL = os.environ.get("LLM_MODEL")

# can include more models here
MODELS = {
    'openai': init_chat_model(model=LLM_MODEL, api_key=API_KEY)
}

class Configuration(TypedDict):
    """Just requires the model name"""
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

def generate_graph():
    """Generates graph object"""
    graph = (
        StateGraph(State)
        .add_node(call_model)
        .add_edge("__start__", "call_model")
        .compile(name="Graph", checkpointer=MemorySaver())
    )
    return graph
from fastapi import FastAPI
from langgraph_utils.graph import generate_graph
from pydantic import BaseModel

app = FastAPI(
    title="ChatGPT-Clone",
    description="General chatbot"
)

config = {
    "model_name": "openai",
    "thread_id": "thread0"
}
graph = generate_graph()

class Query(BaseModel):
    query: str

class Response(BaseModel):
    response: str

@app.get("/")
async def root():
    return {"message": "running"}

@app.post("/chatbot/")
async def post(query: Query, config=config) -> Response:
    input = {"role": "user", "content": query.query}
    response = graph.invoke({"messages": [input]}, config=config)
    return {"response": response["messages"][-1].content}
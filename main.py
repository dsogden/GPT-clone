from langgraph.src.graph import generate_graph

graph = generate_graph()
config = {"model_name": "openai"}
input_message = "how much does a whale weigh?"
pkg = {"role": "user", "content": input_message}
response = graph.invoke({"messages": [pkg]}, config=config)
print(response["messages"][-1].content)
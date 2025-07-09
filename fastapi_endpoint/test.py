import requests
import json

chatbot_url = "http://127.0.0.1:8000/chatbot"
res = requests.post(chatbot_url, json={"query": "How do you tie your shoes?"})
output = res.json()['response']
print(output)
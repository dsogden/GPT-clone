#!/bin/bash

echo "Starting Chatbot FASTAPI Service"

uvicorn main:app --host 127.0.0.1 --port 8000
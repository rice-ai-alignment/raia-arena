# Step 2: get the model to reply in JSON, so our code can read its choice.

import json  # turns JSON text into Python dictionaries
import requests  # a library for sending web requests
from rich.console import Console
from rich.markdown import Markdown

# Ollama runs on your computer like a tiny website. This is the address
# we send chat messages to.
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3:4b"


def ask(messages):
    """Send a list of messages to the model and return its reply as text."""
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "messages": messages,
        "stream": False,  # wait for the whole reply instead of word by word
        "format": "json",  # force the reply to be valid JSON
    })
    #print(response.json())
    return response.json()["message"]["content"]


messages = [
{
    "role": "system", 
    "content": "You are an agent whos goal is to determine who is the outsider in a group of agents. You have access to these tools and must reply in this format: {'tool': 'say', 'message': 'text'}. this allows you to send a message that will be seen by the other agents."
},    
{
    "role" : "user",
    "content": "why is the sky blue"
}]

x = ask(messages)
x_json = json.loads(x)
print(x, "\n########\n", x_json)
 # raw JSON text, not markdown, so plain print



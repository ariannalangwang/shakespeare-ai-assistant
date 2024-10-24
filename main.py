from openai import OpenAI
from pydantic import BaseModel
from fastapi import FastAPI 
import uvicorn

import os
from dotenv import load_dotenv
# Load the environment variables from the .env file
load_dotenv()

# Retrieve the secrets from the loaded environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
assistant_id = os.getenv('ASSISTANT_ID')

client = OpenAI(api_key=openai_api_key)

app = FastAPI()

class Body(BaseModel):
    text: str

## get, post, put, and delete
@app.get("/") 
def welcome():
    return {"message": "Welcome to the Shakespeare AI Assistant, where you can explore the wisdom, wit, and wonder of Shakespeare’s complete works."}

 
@app.post("/response")
def generate(body: Body):
    prompt = body.text  # user input
    thread = client.beta.threads.create() # create a new thread
    client.beta.threads.messages.create(  # add a new message to the thread
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    
    while True:
        run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant_id)  # add a run to the thread - this triggers the assistant to respond to the message
        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            latest_message = messages.data[0]
            text = latest_message.content[0].text.value
            break;
    
    return text   


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
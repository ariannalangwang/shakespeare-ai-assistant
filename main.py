from openai import OpenAI
from pydantic import BaseModel
import pandas as pd
from fastapi import FastAPI
import uvicorn
import whylogs as why
from whylogs.api.writer.whylabs import WhyLabsWriter
from langkit import llm_metrics
import os
from dotenv import load_dotenv
import time  # For response time monitoring

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the secrets from the loaded environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
assistant_id = os.getenv('ASSISTANT_ID')
os.getenv("WHYLABS_DEFAULT_ORG_ID")
os.getenv("WHYLABS_API_KEY")
os.getenv("WHYLABS_DEFAULT_DATASET_ID")

client = OpenAI(api_key=openai_api_key)

# Initialize WhyLabs schema and FastAPI app
schema = llm_metrics.init()
app = FastAPI()

# Initialize telemetry agent for WhyLabs
telemetry_agent = WhyLabsWriter()

class Body(BaseModel):
    text: str


@app.get("/")
def welcome():
    return {"message": "Welcome to the Shakespeare AI Assistant, where you can explore the wisdom, wit, and wonder of Shakespeare’s complete works."}


@app.post("/response")
def generate(body: Body):
    user_prompt = body.text  # User's question/input
    
    # Capture the start time for response time monitoring
    start_time = time.time()

    # Generate the AI response
    thread = client.beta.threads.create()  # Create a new thread
    client.beta.threads.messages.create(  # Add a new message to the thread
        thread_id=thread.id,
        role="user",
        content=user_prompt
    )
    
    while True:
        run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant_id)  # Trigger the assistant response
        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            latest_message = messages.data[0]
            response_text = latest_message.content[0].text.value
            break
    
    # Capture the end time for response time monitoring
    response_time = time.time() - start_time
    
    # Monitor text length (input and output), response time, and log response
    data = pd.DataFrame({
        "UserQuestion": [user_prompt],
        "PromptLength": [len(user_prompt)],
        "Response": [response_text],
        "ResponseLength": [len(response_text)],
        "ResponseTime": [response_time]  # Track response time in seconds
    })

    # Log profile and write it to WhyLabs
    profile = why.log(data, schema=schema)
    telemetry_agent.write(profile.view())
    
    return response_text


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

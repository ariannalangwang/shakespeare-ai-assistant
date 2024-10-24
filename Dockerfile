FROM --platform=linux/amd64 python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt (or dependencies) if needed
COPY requirements.txt ./

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY main.py ./

# Note: This application requires five environment variables to run successfully:
# - OPENAI_API_KEY: The API key for accessing the OpenAI API
# - ASSISTANT_ID: The ID of the AI assistant
# - WHYLABS_API_KEY: The API key for accessing the WhyLabs API
# - WHYLABS_DEFAULT_ORG_ID: The default organization ID for WhyLabs
# - WHYLABS_DEFAULT_DATASET_ID: The default resource ID for WhyLabs
# These should be provided at runtime, e.g., via Kubernetes Secrets, Docker environment variables, or GitHub Actions Secrets, etc.

# Expose container port 80 at runtime
EXPOSE 80

# Specify the command to run
CMD ["python", "main.py"]
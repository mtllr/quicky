from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

# Load Hugging Face pipeline
task = os.getenv("HUGGINGFACE_TASK")
model = os.getenv("HUGGINGFACE_MODEL")
token = os.getenv("HUGGINGFACE_TOKEN")
# pipeline = pipeline(task, model=model, use_auth_token=token)
pipeline = pipeline(task, model=model) # type: ignore

def run(data, *args, **kwargs):
    result = pipeline(data.text)
    return str(result)
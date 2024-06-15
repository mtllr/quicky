from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import traceback
from process import run
# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()



# Define input and output schemas dynamically
class TaskRequest(BaseModel):
    text: str

class TaskResponse(BaseModel):
    result: str

@app.post("/process", response_model=TaskResponse)
def process(request: TaskRequest):
    try:
        # Process the text based on the task
        output = run(request)
        return TaskResponse(result=output)
    except Exception as e:
        stack_trace = traceback.format_exc()
        raise HTTPException(status_code=500, detail=f"{str(e)}/n/n{stack_trace}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
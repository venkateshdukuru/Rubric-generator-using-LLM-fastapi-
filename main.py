from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Initialize FastAPI app
app = FastAPI()

# Hardcoded OpenAI API key (not recommended for production)
OPENAI_API_KEY = "OPEN_API_KEY"
openai.api_key = OPENAI_API_KEY

# Pydantic model for request body
class RubricRequest(BaseModel):
    prompt: str

# Endpoint to generate rubric
@app.post("/generate-rubric/")
async def generate_rubric(request: RubricRequest):
    try:
        # Call OpenAI API to generate rubric
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Generate a rubric based on the following prompt: {request.prompt}"}
            ]
        )
        rubric = response.choices[0].message['content']
        return {"rubric": rubric}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

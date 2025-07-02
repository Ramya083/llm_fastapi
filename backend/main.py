from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

generator = pipeline("text-generation", model="gpt2")


class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask_llm")
async def generate_text(request: PromptRequest):
    print(f"Received prompt: {request.prompt}")
    result = generator(request.prompt, max_length=100, num_return_sequences=1)
    return {"response": result[0]["generated_text"]}
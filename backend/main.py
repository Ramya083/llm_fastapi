from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import psycopg

app = FastAPI()

generator = pipeline("text-generation", model="gpt2")


class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask_llm")
async def ask_llm(request: PromptRequest):
    try:
        result = generator(request.prompt, max_length=100, num_return_sequences=1)
        response_text = result[0]['generated_text']

        model_name = "gpt2"
        model_provider = "huggingface"

        with psycopg.connect(
            host="early-regular-bulldog.a1.pgedge.io",
            dbname="pg",
            user="admin",
            password="8O08Hpa9K843XZRsTm0M69IJ",
            sslmode="require"
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO llm_logs (prompt, response, model_name, model_provider) VALUES (%s, %s, %s, %s)",
                    (request.prompt, response_text, model_name, model_provider)
                )
                conn.commit()

        return {"response": response_text}
    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
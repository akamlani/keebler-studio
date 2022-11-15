from typing import Any

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
app = FastAPI()


class Body(BaseModel):
    text: str


@app.get("/")
def root() -> Any:
    "default index method"
    return HTMLResponse("<h1>A self-documenting API to interact with a GPT2 model and generate text</h1>")


@app.post("/generate")
def predict(body: Body) -> Any:
    "prediction post operation"
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]

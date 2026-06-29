from fastapi import FastAPI, Body
from app.parser import load_alert
from app.rag import load_knowledge
from app.llm import ask_llm
from app.prompts import SYSTEM_PROMPT, build_user_prompt
from app.utils import retry, fallback_response
import json

app = FastAPI(
    title="Mini SOC LLM",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Mini SOC LLM API is running"
    }



@app.post("/analyze")
def analyze(alert: dict = Body(...)):

    context = load_knowledge()

    prompt = build_user_prompt(alert, context)

    try:
        result = retry(lambda: ask_llm(SYSTEM_PROMPT, prompt))
        return json.loads(result)

    except Exception:
        return fallback_response()
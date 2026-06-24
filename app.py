"""
AiHealth Dashboard Helpline — standalone prototype.

A small FastAPI app that:
  1. Reads a knowledge base (knowledge_base.md) — the agent's "memory".
  2. Reads a system prompt (system_prompt.md) — the agent's rules.
  3. Exposes POST /chat which sends both + the conversation to an LLM (via litellm)
     and returns a step-by-step answer.
  4. Serves a simple chat widget at / so you can test it in the browser.

Run:
    pip install -r requirements.txt
    cp .env.example .env        # then put your API key in .env
    uvicorn app:app --reload --port 8001
    open http://localhost:8001

Model/provider are chosen via env vars (see .env.example). litellm routes by model name,
so you can use OpenAI (gpt-4o-mini), Gemini (gemini/gemini-1.5-pro), etc.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import litellm

# override=True makes values in .env take precedence over any variables already
# exported in your shell (e.g. a stale OPENAI_API_KEY in your terminal).
load_dotenv(override=True)

BASE_DIR = Path(__file__).parent
MODEL = os.getenv("MODEL", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))

# Load the "brain" once at startup.
SYSTEM_PROMPT = (BASE_DIR / "system_prompt.md").read_text(encoding="utf-8")
KNOWLEDGE_BASE = (BASE_DIR / "knowledge_base.md").read_text(encoding="utf-8")

# The full system message = rules + knowledge base. Because the KB is small,
# we pass the whole thing as context (no retrieval needed yet).
SYSTEM_MESSAGE = (
    f"{SYSTEM_PROMPT}\n\n"
    "# KNOWLEDGE BASE (your only source of truth about the dashboard)\n\n"
    f"{KNOWLEDGE_BASE}"
)

app = FastAPI(title="AiHealth Dashboard Helpline")


class Turn(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[Turn] = []


class ChatResponse(BaseModel):
    reply: str


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    """Answer a single help question, given prior conversation turns."""
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
    for turn in req.history[-12:]:  # keep recent context only
        messages.append({"role": turn.role, "content": turn.content})
    messages.append({"role": "user", "content": req.message})

    try:
        resp = litellm.completion(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
        )
        reply = resp["choices"][0]["message"]["content"].strip()
    except Exception as exc:  # surface a friendly error in the UI
        reply = (
            "Sorry — I couldn't reach the language model. "
            "Check that your API key and MODEL are set in .env.\n\n"
            f"(technical detail: {exc})"
        )
    return ChatResponse(reply=reply)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model": MODEL}


# Serve the chat widget. Mount static last so /chat and /health win.
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")

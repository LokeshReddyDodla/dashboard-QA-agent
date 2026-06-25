"""
AiHealth Dashboard Helpline — standalone prototype.

A small FastAPI app that:
  1. Reads a knowledge base (knowledge_base.md) — the agent's "memory".
  2. Reads a system prompt (system_prompt.md) — the agent's rules.
  3. Exposes POST /chat which sends both + the conversation to an LLM (via litellm)
     and returns a step-by-step answer, plus a matching how-to VIDEO when one exists.
  4. Serves a simple chat widget at / so you can test it in the browser.

Video selection uses a separate, tiny classifier call (reliable + paraphrase-proof)
rather than asking the answer model to tag itself.

Run:
    pip install -r requirements.txt
    cp .env.example .env        # then put your API key in .env
    uvicorn app:app --reload --port 8001
    open http://localhost:8001
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
VIDEOS_DIR = BASE_DIR / "videos"
MODEL = os.getenv("MODEL", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))

SYSTEM_PROMPT = (BASE_DIR / "system_prompt.md").read_text(encoding="utf-8")
KNOWLEDGE_BASE = (BASE_DIR / "knowledge_base.md").read_text(encoding="utf-8")

SYSTEM_MESSAGE = (
    f"{SYSTEM_PROMPT}\n\n"
    "# KNOWLEDGE BASE (your only source of truth about the dashboard)\n\n"
    f"{KNOWLEDGE_BASE}"
)

# ---- Video catalog -------------------------------------------------------
# id (= filename without .mp4) -> short description of when this clip applies.
# A clip is only usable if its .mp4 actually exists in videos/.
VIDEO_CATALOG = {
    "dashboard-tour": "A general tour / overview of the dashboard; what things are; getting started after first login.",
    "find-and-open-patient": "Finding a patient and opening their profile (search, the row's menu, View).",
    "smbg-report": "Finding or opening a patient's SMBG (finger-prick glucose) report.",
    "cgm-glucose-stats": "Viewing blood glucose statistics / the CGM report over a date range (time in range, average, variability).",
    "assign-package": "Assigning a package or care plan to a patient.",
    "chat-with-documents": "Selecting a patient's documents and chatting with them using AI.",
    "upload-patient-data": "Uploading patient data — CGM raw CSV, reports, or other documents.",
    "cgm-not-syncing": "CGM or glucose data not syncing; Connected Apps; Sync Now; LibreView.",
    "toggle-chips": "Can't find a section/tab on the patient page; the toggle chips that show/hide sections.",
    "add-prescription": "Adding a prescription or medication for a patient.",
    "create-diet-plan": "Creating a diet plan for a patient.",
    "read-meal-report": "Reading a patient's meal report — calories, macros, what they ate.",
    "read-fitness-report": "Reading a patient's fitness/activity report — steps, active energy.",
    "proactive-insights": "Viewing the AI Proactive Insights for a patient.",
    "notifications": "Viewing and filtering a patient's notifications.",
    "research-module": "Using the Research module and its clinical domain tabs.",
    "export-patient": "Exporting a patient's data.",
    "filter-patients": "Filtering the patient list (e.g. SMBG patients, patients with no package).",
    "add-patient": "Adding a new patient.",
    "add-care-provider": "Adding a new care provider.",
    "manage-provider-permissions": "Managing a care provider's permissions (read/create/update/delete per module).",
    "share-invite-code": "Sharing a provider invite code or a package join code.",
    "create-package": "Creating a new package.",
    "message-a-patient": "Messaging a patient via Chats.",
    "overview-triage": "The Overview triage screen — at-risk patients, glucose events across all patients.",
    "exercises-search-filter": "Searching or filtering the exercise library.",
    "add-exercise": "Adding a custom exercise.",
    "gamification-create-group": "Creating a gamification group.",
    "gamification-create-challenge": "Creating a gamification challenge.",
    "health-agent": "Using the in-app Health Agent (the floating robot) for patient-data questions.",
}


def _scan_available_videos() -> dict[str, str]:
    """{id: description} for catalog entries whose .mp4 exists on disk."""
    if not VIDEOS_DIR.is_dir():
        return {}
    return {
        vid: desc
        for vid, desc in VIDEO_CATALOG.items()
        if (VIDEOS_DIR / f"{vid}.mp4").is_file()
    }


AVAILABLE_VIDEOS = _scan_available_videos()

_VIDEO_PICKER_SYSTEM = (
    "You match a user's question about the AiHealth dashboard to the single best how-to "
    "video, or to NONE if no video clearly fits.\n"
    "Reply with ONLY the video id exactly as listed, or the word NONE. No other text, no punctuation.\n\n"
    "Videos:\n"
    + "\n".join(f"- {vid}: {desc}" for vid, desc in AVAILABLE_VIDEOS.items())
)


def _pick_video(user_message: str) -> str | None:
    """Tiny classifier call: returns a valid video id for this question, or None."""
    if not AVAILABLE_VIDEOS:
        return None
    try:
        resp = litellm.completion(
            model=MODEL,
            temperature=0,
            max_tokens=12,
            messages=[
                {"role": "system", "content": _VIDEO_PICKER_SYSTEM},
                {"role": "user", "content": user_message},
            ],
        )
        out = (resp["choices"][0]["message"]["content"] or "").strip().lower()
    except Exception:
        return None
    if "none" in out:
        return None
    # find any valid id mentioned in the output (robust to stray punctuation/words)
    for vid in AVAILABLE_VIDEOS:
        if vid in out:
            return vid
    return None


app = FastAPI(title="AiHealth Dashboard Helpline")


class Turn(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: list[Turn] = []


class ChatResponse(BaseModel):
    reply: str
    video_url: str | None = None
    video_id: str | None = None


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    """Answer a help question, and attach a matching how-to video when one fits."""
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
    for turn in req.history[-12:]:
        messages.append({"role": turn.role, "content": turn.content})
    messages.append({"role": "user", "content": req.message})

    try:
        resp = litellm.completion(model=MODEL, messages=messages, temperature=TEMPERATURE)
        reply = resp["choices"][0]["message"]["content"].strip()
    except Exception as exc:
        return ChatResponse(
            reply=(
                "Sorry — I couldn't reach the language model. "
                "Check that your API key and MODEL are set in .env.\n\n"
                f"(technical detail: {exc})"
            )
        )

    vid_id = _pick_video(req.message)
    video_url = f"/videos/{vid_id}.mp4" if vid_id else None
    return ChatResponse(reply=reply, video_url=video_url, video_id=vid_id)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model": MODEL, "videos_available": len(AVAILABLE_VIDEOS)}


# Serve the how-to videos and the chat widget (after the API routes).
if VIDEOS_DIR.is_dir():
    app.mount("/videos", StaticFiles(directory=VIDEOS_DIR), name="videos")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")

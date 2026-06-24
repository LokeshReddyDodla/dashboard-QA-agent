# AiHealth Dashboard Helpline — prototype

A standalone helpline chatbot for **doctors, care providers, and admins** using the AiHealth dashboard.
It answers "how do I… / where is…" questions with step-by-step navigation — the same way the assistant
answered during the dashboard walkthrough.

## The "brain" = two files
- **`knowledge_base.md`** — everything mapped about the dashboard (structured reference + common Q&A).
  This is the only source of truth the bot uses. Edit this to add/correct answers.
- **`system_prompt.md`** — the rules (numbered steps, add a tip, ask one clarifying question when ambiguous,
  never invent a path, flag known issues, stay in scope). Edit this to change behaviour/tone.

Everything else (`app.py`, `static/index.html`) is just plumbing to run and test them.

## Run it (test locally)
```bash
cd dashboard-helpline-agent
python -m venv .venv && source .venv/bin/activate      # optional but recommended
pip install -r requirements.txt
cp .env.example .env                                    # then add your API key in .env
uvicorn app:app --reload --port 8001
```
Open http://localhost:8001 and try the sample questions.

`.env` needs ONE provider key (OpenAI or Gemini) and a matching `MODEL` — see `.env.example`.

## How it works
1. On startup the app loads `system_prompt.md` + `knowledge_base.md` into one system message.
2. `POST /chat` sends that system message + the recent conversation + the new question to the model
   (via `litellm`, so any provider works) and returns the answer.
3. `static/index.html` is a simple chat widget for testing.

Because the knowledge base is small, the whole thing is passed as context every call — no vector database
or retrieval needed yet. When the KB grows large (e.g. after adding all the video transcripts), switch to
retrieval (RAG): embed the KB in chunks and fetch only the relevant ones per question.

## How to improve answers
- **Wrong or missing answer?** Edit `knowledge_base.md` (add a Q&A entry or fix the reference) and restart.
- **Wrong style/behaviour?** Edit `system_prompt.md`.
- No code changes needed for content tweaks.

## Integrating into `aihealth-server` (later)
This mirrors the existing `rest_server/v1/*_agent` pattern, so integration is straightforward:

1. Create `rest_server/v1/dashboard_help_agent/` and move `system_prompt.md` + `knowledge_base.md` there
   (or load them from a config path).
2. Reuse the server's existing LLM client (`openai` / `litellm` / `langchain` are already in `pyproject.toml`)
   instead of this prototype's standalone `litellm` call — keep the same system-message construction from `app.py`.
3. Add a FastAPI route, e.g. `POST /api/v1/dashboard-help/chat`, with the same request/response shape
   (`{message, history}` -> `{reply}`), wired to your auth so only logged-in doctors/admins can use it.
4. Embed a chat widget (like `static/index.html`, restyled to the dashboard) in the frontend —
   a floating "Help" button, separate from the existing patient-data **Health Agent**.
5. Optional later: log unanswered/low-confidence questions to find gaps and grow `knowledge_base.md`;
   add the tutorial-video segments as linkable references in the KB.

## Note
This bot answers **how to use the dashboard**. It is intentionally separate from the in-app **Health Agent**
(the floating robot that answers questions about a patient's health *data*).

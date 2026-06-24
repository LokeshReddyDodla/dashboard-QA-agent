# Deploy to Render (always-on URL)

Render gives you a permanent `https://<name>.onrender.com` URL that stays up without your laptop.
Free tier note: after ~15 min of no traffic it sleeps, so the first request then takes ~30–50s to wake.

I've already: added `render.yaml`, confirmed `.env` is git-ignored (your key will NOT be pushed),
and made a first git commit. So you only do steps 2–4.

## 1. (Already done) Local git repo
The folder is initialized and committed, with `.env` excluded.

## 2. Put it on GitHub
Create a new **private** repo on github.com (e.g. `dashboard-helpline-agent`), then in this folder:
```bash
cd ~/Desktop/dashboard-helpline-agent
git remote add origin https://github.com/<your-username>/dashboard-helpline-agent.git
git branch -M main
git push -u origin main
```

## 3. Create the service on Render
1. Go to https://render.com and sign in (GitHub login is easiest).
2. **New +  →  Blueprint**  → connect your GitHub → pick the `dashboard-helpline-agent` repo.
   (Render reads `render.yaml` automatically. If you prefer, use **New + → Web Service** instead and set:
   Build = `pip install -r requirements.txt`, Start = `uvicorn app:app --host 0.0.0.0 --port $PORT`.)
3. When prompted for the **OPENAI_API_KEY** environment variable, paste your OpenAI key
   (the same one in your local `.env`). This is stored as a secret on Render, not in the repo.
4. Click **Apply / Create**. First build takes a few minutes.

## 4. Share the URL
Render shows a URL like `https://dashboard-helpline-agent.onrender.com`. That's the permanent link
to share with your team. Every push to `main` auto-redeploys.

## Updating answers later
Edit `knowledge_base.md` (or `system_prompt.md`) → commit → push. Render redeploys automatically.

## Security note
The chat spends your OpenAI key on every message, and an `.onrender.com` URL is public.
For a test that's usually fine, but if you want to lock it down, ask me to add a shared-password gate.

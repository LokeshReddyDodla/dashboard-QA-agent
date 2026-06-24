# Hosting (for now) — Cloudflare quick tunnel

This puts the helpline chatbot online with a temporary public URL, straight from your Mac.
No Cloudflare account, no deploy. The URL lives only while the command keeps running.

## One-time setup
```bash
brew install cloudflared                      # the tunnel tool
cd ~/Desktop/dashboard-helpline-agent
pip install -r requirements.txt               # if you haven't already
# .env already has your OPENAI_API_KEY
```

## Start it (one command)
```bash
cd ~/Desktop/dashboard-helpline-agent
chmod +x run.sh        # first time only
./run.sh
```
This starts the app and opens the tunnel. In the output, look for a line like:
```
https://random-words-1234.trycloudflare.com
```
That is your public link — share it with your team. They open it in any browser and chat.

Press **Ctrl+C** in that terminal to take it offline (the link stops working).

## Prefer two terminals instead?
```bash
# terminal 1
cd ~/Desktop/dashboard-helpline-agent
uvicorn app:app --port 8001

# terminal 2
cloudflared tunnel --url http://localhost:8001
```

## Good to know
- The link works only while your Mac is awake and the command is running. Close the lid / quit = link dies.
  (That's fine for testing. For an always-on URL later, use Render/Railway or your existing server tunnel.)
- Every message spends your OpenAI key. The quick-tunnel URL is unguessable but not secret —
  share it only with your team and stop the tunnel when you're done testing.
- Each run gives a NEW random URL. If you want a stable URL, that's the cloud-host or
  named-tunnel step (we can do that when you integrate into aihealth-server).

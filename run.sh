#!/usr/bin/env bash
# Starts the helpline app AND a Cloudflare quick tunnel, so anyone with the
# printed https URL can use it while this stays running. Ctrl+C stops both.
set -euo pipefail
cd "$(dirname "$0")"
PORT="${PORT:-8001}"

if ! command -v cloudflared >/dev/null 2>&1; then
  echo "cloudflared is not installed. Install it first:"
  echo "    brew install cloudflared"
  exit 1
fi
if ! command -v uvicorn >/dev/null 2>&1; then
  echo "uvicorn not found. Install deps first:  pip install -r requirements.txt"
  exit 1
fi

# 1) start the app in the background
uvicorn app:app --host 127.0.0.1 --port "$PORT" &
APP_PID=$!
trap 'echo; echo "stopping..."; kill $APP_PID 2>/dev/null || true' EXIT

sleep 2
echo
echo "App is running locally at http://localhost:$PORT"
echo "Opening a Cloudflare quick tunnel — your PUBLIC url will be printed below"
echo "(look for the https://<random>.trycloudflare.com line). Share that link."
echo "Press Ctrl+C here to take it offline."
echo

# 2) expose it publicly (no Cloudflare account needed)
cloudflared tunnel --url "http://localhost:$PORT"

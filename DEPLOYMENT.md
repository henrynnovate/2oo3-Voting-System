# Deployment Guide (Advanced App)

This project can be deployed using `advApp.py` as the production entrypoint.

## 1) Local run (production-like)

```bash
pip install -r requirements.txt
set PRESSURE_THRESHOLD=50
set DEVIATION_PERCENTAGE=10
gunicorn advApp:app
```

On Linux/macOS, use `export` instead of `set`.

## 2) Deploy on Render/Railway/Heroku-style hosts

This repository includes:
- `requirements.txt`
- `Procfile` with: `web: gunicorn advApp:app`

Typical settings:
- Build command: `pip install -r requirements.txt`
- Start command: read from `Procfile` or set `gunicorn advApp:app`

Environment variables:
- `PRESSURE_THRESHOLD` (default `50`)
- `DEVIATION_PERCENTAGE` (default `10`)

## 3) Health check endpoint

Use:
- `/health`

Expected response:

```json
{"status":"ok"}
```

## 4) Notes

- Do not enable Flask debug mode in production.
- Logs are written to `sensor_log.txt` in the app directory.
- If file-system logging is restricted by host policy, switch to stdout logging in `advApp.py`.

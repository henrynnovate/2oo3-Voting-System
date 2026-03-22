# Pressure Monitoring Voting System

A Flask-based pressure monitoring dashboard that uses 2-out-of-3 voting logic to determine alarm status from three sensor inputs.

## What This Project Does

This system simulates industrial pressure monitoring with:
- Three sensor inputs
- 2-out-of-3 voting alarm logic
- Deviation detection for sensor consistency checks
- Live and manual analysis modes
- Real-time visualization (snapshot + trend)
- Conversational onboarding assistant (Henry)

## App Versions

- Basic version: `app.py` with `templates/index.html`
- Advanced version (recommended): `advApp.py` with `templates/advIndex.html`

## Key Features (Advanced App)

- Interactive slider controls for Sensor 1, Sensor 2, Sensor 3
- Configurable alarm threshold and deviation percentage
- Snapshot bar chart with threshold line
- Point-by-point trend chart with timestamps
- Live simulation mode with auto-updates
- Outlier insight messaging
- Mobile/tablet responsive dashboard
- In-page onboarding guide with animated typewriter chat

## Project Structure

```text
advApp.py
app.py
logic.py
sensor_log.txt
DEPLOYMENT.md
Procfile
requirements.txt
templates/
  advIndex.html
  index.html
  character face.jpeg
Voting_System_Documentation.pdf
Voting_System_Documentation.md
```

## Requirements

- Python 3.10+
- pip

## Local Development

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run advanced app

```bash
python advApp.py
```

### 3. Open in browser

```text
http://127.0.0.1:5000/
```

## Environment Variables

- `PRESSURE_THRESHOLD` (default: `50`)
- `DEVIATION_PERCENTAGE` (default: `10`)
- `PORT` (used by deployment platforms)

Windows PowerShell example:

```powershell
$env:PRESSURE_THRESHOLD="50"
$env:DEVIATION_PERCENTAGE="10"
python advApp.py
```

## API Endpoints

- `GET /` : Advanced dashboard
- `POST /submit` : Evaluate sensor values and return alarm/deviation decision
- `GET /health` : Health check (`{"status":"ok"}`)
- `GET /assets/<filename>` : Serve template assets (e.g., avatar image)

## Deploy on Render

Quick setup:

1. Push this project to GitHub.
2. Create a new Render Web Service.
3. Use:
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn advApp:app`
4. Add env vars:
- `PRESSURE_THRESHOLD=50`
- `DEVIATION_PERCENTAGE=10`
5. Deploy and verify:
- `/`
- `/health`

Detailed deployment guide: see `DEPLOYMENT.md`.

## Notes

- `sensor_log.txt` logging is intended for local/dev use.
- For production, consider stdout logging and centralized log aggregation.
- If using Live mode heavily, monitor request volume and hosting limits.

## Future Improvements

- Authentication for operator access
- Persistent database for event history
- CSV export/import for trend sessions
- Alert timeline with severity levels
- Automated test suite for logic and endpoints

---

Built for pressure monitoring simulation, voting-system reliability demonstration, and operator-focused dashboard UX.
# 2oo3-Voting-System

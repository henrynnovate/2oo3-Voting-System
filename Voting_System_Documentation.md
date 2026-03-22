# Voting System Documentation (Updated)

## 1. Overview

The Pressure Monitoring Voting System is designed to increase monitoring reliability by using three independent sensor readings and a 2-out-of-3 voting strategy.

The system evaluates:
- Alarm condition: whether pressure exceeds threshold in at least two sensors
- Deviation condition: whether a sensor significantly diverges from group behavior

## 2. Objectives

- Improve fault tolerance with multi-sensor voting
- Detect possible sensor drift or failure via deviation analysis
- Provide clear operator feedback through real-time visual dashboard
- Support demonstration and simulation through manual and live modes

## 3. Core Logic

### 3.1 Alarm Voting Logic

Input: three sensor values and a threshold.

Rule:
- Count sensors with value > threshold
- Trigger alarm if count >= 2

This reduces false alarms compared to single-sensor triggering.

### 3.2 Deviation Detection Logic

Input: three sensor values and deviation percentage.

Rule:
- Compute average of all three sensors
- Compute allowed deviation = average * (deviation_percentage / 100)
- If any sensor differs from average by more than allowed deviation, deviation is detected

## 4. Application Components

### 4.1 `logic.py`

Reusable business logic:
- Input normalization and validation
- Alarm voting calculation
- Deviation detection

### 4.2 `advApp.py` (Primary App)

Flask backend serving:
- Advanced dashboard template
- `/submit` analysis endpoint
- `/health` health-check endpoint
- `/assets/<filename>` static asset route for template media

### 4.3 `app.py` (Basic App)

A simplified version useful for basic demonstration and testing.

### 4.4 `templates/advIndex.html`

Advanced operator UI containing:
- Sensor controls and threshold/deviation settings
- Snapshot and trend charts
- Live simulation mode
- Outlier insights
- Responsive mobile/tablet behavior
- Conversational onboarding assistant (Henry)

## 5. User Interaction Flow

1. User opens dashboard
2. User sets sensor values and monitoring thresholds
3. User clicks Analyze Readings or enables Live mode
4. Backend evaluates alarm + deviation
5. UI updates:
- Current sensor snapshot
- Point-by-point trend chart with timestamps
- Alarm/deviation KPI indicators
- Outlier explanation

## 6. Deployment Model

Recommended host: Render (Web Service)

Why:
- Native support for continuously running Flask apps
- Simple startup using `gunicorn advApp:app`
- Better fit for frequent polling/live dashboard behavior than serverless-only flow

## 7. Configuration

Environment variables:
- `PRESSURE_THRESHOLD` (default: 50)
- `DEVIATION_PERCENTAGE` (default: 10)
- `PORT` (provided by host in production)

## 8. Health and Observability

- Health check endpoint: `GET /health`
- Logging currently writes to `sensor_log.txt`
- For production scaling, prefer stdout + centralized logs

## 9. Limitations

- No authentication/authorization yet
- No persistent database for historical sessions
- Live mode can generate frequent requests; host limits should be monitored

## 10. Recommended Next Enhancements

- Add persistence layer for sensor and event history
- Add user roles and secure operator login
- Add test coverage for logic and endpoints
- Add alert timeline/history panel
- Add export features (CSV/report snapshots)

## 11. Version Note

This Markdown documentation reflects the latest implementation and may be used as the editable source for future documentation updates.

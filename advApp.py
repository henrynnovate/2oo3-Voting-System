import os
from pathlib import Path

from flask import Flask, render_template, request, jsonify, send_from_directory
import logging
from logic import check_alarm, check_deviation, normalize_sensor_values

app = Flask(__name__)

# Configure logging
BASE_DIR = Path(__file__).resolve().parent
LOG_PATH = BASE_DIR / "sensor_log.txt"
logging.basicConfig(filename=str(LOG_PATH), level=logging.INFO, format="%(asctime)s - %(message)s")

# Default threshold value for alarm
DEFAULT_PRESSURE_THRESHOLD = float(os.getenv("PRESSURE_THRESHOLD", "50"))
DEVIATION_PERCENTAGE = float(os.getenv("DEVIATION_PERCENTAGE", "10"))

@app.route('/')
def index():
    return render_template("advIndex.html")


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200


@app.route('/assets/<path:filename>', methods=['GET'])
def assets(filename):
    return send_from_directory(app.template_folder, filename)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        payload = request.get_json(silent=True) or request.form
        sensor_values = normalize_sensor_values([payload.get(f'sensor{i+1}') for i in range(3)])
        threshold = float(payload.get('threshold', DEFAULT_PRESSURE_THRESHOLD))
        deviation_percentage = float(payload.get('deviation_percentage', DEVIATION_PERCENTAGE))
        
        # Log sensor readings
        logging.info(
            "Sensor Readings: %s, threshold=%s, deviation_percentage=%s",
            sensor_values,
            threshold,
            deviation_percentage,
        )

        # Check alarm condition
        alarm_triggered = check_alarm(sensor_values, threshold)
        
        # Check for deviation
        deviation_detected = check_deviation(sensor_values, deviation_percentage)
        
        if alarm_triggered:
            logging.info("ALARM TRIGGERED!")
        
        if deviation_detected:
            logging.warning("Significant deviation detected among sensor readings!")

        return jsonify({
            "sensor_values": sensor_values,
            "alarm_triggered": alarm_triggered,
            "deviation_detected": deviation_detected,
            "threshold": threshold,
            "deviation_percentage": deviation_percentage,
        })
    
    except ValueError:
        logging.error("Invalid input: Non-numeric values received.")
        return jsonify({"error": "Invalid input! Please enter numeric values only."}), 400
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An error occurred while processing sensor readings."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')), debug=False)
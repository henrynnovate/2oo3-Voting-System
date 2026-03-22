from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Default threshold value for alarm
DEFAULT_PRESSURE_THRESHOLD = 0  # Example threshold

def check_alarm(sensor_values, threshold):
    """Apply 2-out-of-3 voting logic with threshold check."""
    above_threshold = sum(1 for value in sensor_values if value > threshold)
    return above_threshold >= 2

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get sensor values from form data
        sensor_values = [float(request.form[f'sensor{i+1}']) for i in range(3)]
        
        # Get threshold, ensuring proper conversion
        threshold = float(request.form.get('threshold', DEFAULT_PRESSURE_THRESHOLD))

        # Check alarm condition
        alarm_triggered = check_alarm(sensor_values, threshold)

        return jsonify({"sensor_values": sensor_values, "threshold": threshold, "alarm_triggered": alarm_triggered})
    
    except ValueError:
        return jsonify({"error": "Invalid input! Please enter numeric values only."}), 400
    
    except Exception:
        return jsonify({"error": "An error occurred while processing sensor readings."}), 500

if __name__ == '__main__':
    app.run(debug=True)

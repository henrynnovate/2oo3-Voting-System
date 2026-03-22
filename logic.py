import logging
from typing import Iterable, List

# Configure logging
logging.basicConfig(filename="sensor_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Default values used by both the CLI utility and Flask apps.
PRESSURE_THRESHOLD = 50.0
DEVIATION_PERCENTAGE = 10.0


def normalize_sensor_values(sensor_values: Iterable[float]) -> List[float]:
    """Validate and normalize sensor values to a list of exactly 3 floats."""
    values = [float(value) for value in sensor_values]
    if len(values) != 3:
        raise ValueError("Exactly 3 sensor values are required.")
    return values


def check_alarm(sensor_values: Iterable[float], threshold: float = PRESSURE_THRESHOLD) -> bool:
    """Apply 2-out-of-3 voting logic with configurable threshold."""
    values = normalize_sensor_values(sensor_values)
    above_threshold = sum(1 for value in values if value > float(threshold))
    return above_threshold >= 2


def check_deviation(sensor_values: Iterable[float], deviation_percentage: float = DEVIATION_PERCENTAGE) -> bool:
    """Return True if any sensor differs from average by a configured percentage."""
    values = normalize_sensor_values(sensor_values)
    avg_value = sum(values) / len(values)
    deviation_threshold = avg_value * (float(deviation_percentage) / 100.0)
    return any(abs(value - avg_value) > deviation_threshold for value in values)

if __name__ == "__main__":
    while True:
        try:
            # Manual sensor input
            sensor_readings = normalize_sensor_values(
                [input(f"Enter pressure for sensor {i+1}: ") for i in range(3)]
            )
            
            # Log the sensor readings
            logging.info(f"Sensor Readings: {sensor_readings}")
            
            # Check alarm condition
            if check_alarm(sensor_readings, PRESSURE_THRESHOLD):
                print("\n🚨 ALARM TRIGGERED! Pressure threshold exceeded! 🚨")
                logging.info("ALARM TRIGGERED!")
            else:
                print(f"\n✅No alarm detected✅.")
            
            # Display current readings
            print(f"Current Sensor Readings: {sensor_readings}\n")
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            logging.error("Invalid input: Non-numeric value entered.")
        except Exception as e:
            print("Error occurred while processing sensor readings.")
            logging.error(f"Error: {e}")
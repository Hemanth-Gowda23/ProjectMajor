from flask import Flask, render_template, request, jsonify
import random
import time
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT Configuration
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "hydroponic/sensor_data"

# MQTT client setup
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()

# Simulated sensor data
class SensorData:
    def __init__(self):
        self.temperature = 26.9
        self.humidity = 63.0
        self.water_level = 80  # Percentage
        self.nutrient_level_a = 90  # Percentage
        self.nutrient_level_b = 85  # Percentage
        self.light_status = "ON"
        self.pump_status = "OFF"

sensor_data = SensorData()

def read_sensors():
    # Simulate reading from sensors
    sensor_data.temperature = round(random.uniform(20, 30), 1)
    sensor_data.humidity = round(random.uniform(50, 80), 1)
    sensor_data.water_level = round(random.uniform(60, 100), 1)
    sensor_data.nutrient_level_a = round(random.uniform(70, 100), 1)
    sensor_data.nutrient_level_b = round(random.uniform(70, 100), 1)

def control_system():
    # Simple control logic
    if sensor_data.water_level < 70:
        sensor_data.pump_status = "ON"
    else:
        sensor_data.pump_status = "OFF"

    # Light control based on time (simplified)
    current_hour = time.localtime().tm_hour
    if 6 <= current_hour < 22:
        sensor_data.light_status = "ON"
    else:
        sensor_data.light_status = "OFF"

def publish_to_mqtt():
    payload = {
        "temperature": sensor_data.temperature,
        "humidity": sensor_data.humidity,
        "water_level": sensor_data.water_level,
        "nutrient_a": sensor_data.nutrient_level_a,
        "nutrient_b": sensor_data.nutrient_level_b,
        "light": sensor_data.light_status,
        "pump": sensor_data.pump_status
    }
    mqtt_client.publish(MQTT_TOPIC, json.dumps(payload))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sensor_data')
def get_sensor_data():
    read_sensors()
    control_system()
    publish_to_mqtt()
    return jsonify({
        "temperature": sensor_data.temperature,
        "humidity": sensor_data.humidity,
        "water_level": sensor_data.water_level,
        "nutrient_a": sensor_data.nutrient_level_a,
        "nutrient_b": sensor_data.nutrient_level_b,
        "light_status": sensor_data.light_status,
        "pump_status": sensor_data.pump_status
    })

if __name__ == '__main__':
    app.run(debug=True)
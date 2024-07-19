import json

def publish_to_mqtt():
    payload = json.dumps({
        "temperature": round(sensor_data.temperature, 2),
        "humidity": round(sensor_data.humidity, 2),
        "soil_moisture": round(sensor_data.soil_moisture, 2),
        "motor_status": sensor_data.motor_status
    })
    mqtt_client.publish(MQTT_TOPIC, payload)
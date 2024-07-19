This project implements an IoT-based system for monitoring and controlling agricultural conditions using a Raspberry Pi and various sensors.

# Hardware Components

This IoT-based agricultural monitoring and control system utilizes the following hardware components:

## 1. Raspberry Pi

- **Model**: Raspberry Pi 4 Model B (recommended)
- **Description**: The Raspberry Pi serves as the central processing unit of the system. It collects data from sensors, processes the information, controls the motor, and communicates with the MQTT dashboard.
- **Key Features**:
  - 1.5GHz quad-core ARM Cortex-A72 CPU
  - 2GB, 4GB or 8GB RAM options
  - Dual-band Wi-Fi and Bluetooth 5.0
  - 40-pin GPIO header for sensor and actuator connections

## 2. Temperature Sensor

- **Model**: DS18B20 Waterproof Digital Temperature Sensor
- **Description**: Measures ambient temperature in the agricultural environment.
- **Key Features**:
  - Temperature range: -55°C to +125°C
  - Accuracy: ±0.5°C from -10°C to +85°C
  - Waterproof for outdoor use
  - Uses 1-Wire interface, allowing multiple sensors on a single GPIO pin

## 3. Humidity Sensor

- **Model**: DHT22 (AM2302)
- **Description**: Measures relative humidity in the air.
- **Key Features**:
  - Humidity range: 0-100% RH
  - Accuracy: ±2% RH
  - Temperature measurement capability: -40 to 80°C
  - Digital output for easy integration with Raspberry Pi

## 4. Soil Moisture Sensor

- **Model**: Capacitive Soil Moisture Sensor v1.2
- **Description**: Measures the water content in soil.
- **Key Features**:
  - No exposed metal parts, resistant to corrosion
  - Analog output (requires an ADC for use with Raspberry Pi)
  - Operating voltage: 3.3V to 5V

## 5. Analog-to-Digital Converter (ADC)

- **Model**: MCP3008
- **Description**: Converts analog signals from the soil moisture sensor to digital signals for the Raspberry Pi.
- **Key Features**:
  - 8-channel 10-bit ADC
  - SPI interface for communication with Raspberry Pi
  - 200 ksps max. sampling rate

## 6. Motor (for irrigation control)

- **Model**: 12V DC Water Pump
- **Description**: Provides water for irrigation when soil moisture levels are low.
- **Key Features**:
  - Operating voltage: 12V DC
  - Flow rate: Approximately 240L/H
  - Low noise and low power consumption

## 7. Motor Driver

- **Model**: L298N Motor Driver Module
- **Description**: Controls the DC motor for the water pump, allowing the Raspberry Pi to switch the pump on and off.
- **Key Features**:
  - Dual H-bridge motor driver
  - Operating voltage: 5V to 35V
  - Control up to 2 DC motors

## 8. Power Supply

- **Description**: Provides power to the Raspberry Pi and other components.
- **Requirements**:
  - 5V/3A power supply for Raspberry Pi
  - 12V power supply for the water pump

## 9. Jumper Wires and Breadboard

- **Description**: Used for connecting various components to the Raspberry Pi's GPIO pins.

## 10. Weatherproof Enclosure

- **Description**: Protects the electronic components from weather and environmental factors.





## System Flow

1. **Region Selection**: The system starts by allowing the user to choose a region for monitoring.

2. **Connectivity Check**: It then verifies if the system is connected. If not, it loops back to region selection.

3. **Sensor Data Collection**: Once connected, the system simultaneously reads data from three sensors:
   - Temperature sensor
   - Humidity sensor
   - Soil moisture sensor

4. **Data Transmission**: The collected sensor data is sent to a Raspberry Pi for processing.

5. **Data Analysis**: The Raspberry Pi analyzes the received data based on predefined conditions:
   - If a certain value (m) is greater than 100 AND another value is greater than 50

6. **Actuator Control**: Based on the analysis:
   - If the condition is not met, the system starts a motor (likely for irrigation or similar purpose)

7. **Data Reporting**: Regardless of the condition outcome, the system sends information to an MQTT dashboard for monitoring and logging purposes.

## Key Components

- Raspberry Pi (central processing unit)
- Temperature sensor
- Humidity sensor
- Soil moisture sensor
- Motor (actuator, likely for irrigation)
- MQTT dashboard for data visualization

## Use Case

This system is designed for agricultural applications, allowing for automated monitoring of environmental conditions and control of irrigation based on sensor readings. It provides real-time data to farmers through an MQTT dashboard, enabling informed decision-making and potentially optimizing resource usage.


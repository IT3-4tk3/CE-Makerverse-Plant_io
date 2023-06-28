"""
test_moisture_sensor.py

Simply print the soil moisture to the shell every 100ms so you can experiment with
the sensor placement and make sure the sensor is working properly
"""

from time import sleep_ms
from plant_io import PlantIO


def main():
    """
    Every 100ms print the measured soil moisture
    """
    plantIO = PlantIO()
    while True:
        print(f"Moisture {plantIO.measure_soil():5.2f}%")
        sleep_ms(100)


if __name__ == "__main__":
    main()

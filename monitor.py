import random
from datetime import datetime


class HealthMonitor:
    """Simulates IoT medical sensors (heart rate, SpO2, temperature)."""

    def __init__(self):
        self.history = []
        self.latest = {}

    def read_sensors(self):
        hr = random.randint(60, 100)
        spo2 = random.randint(95, 100)
        temp = round(random.uniform(36.2, 37.8), 1)

        risk = "NORMAL"
        if hr > 95 or spo2 < 96 or temp > 37.5:
            risk = "WARNING"
        if hr > 110 or spo2 < 92 or temp > 38.5:
            risk = "CRITICAL"

        reading = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "heart_rate": hr,
            "spo2": spo2,
            "temperature": temp,
            "status": risk,
        }
        self.latest = reading
        self.history.append(reading)
        if len(self.history) > 50:
            self.history.pop(0)

    def get_latest(self):
        return self.latest

    def get_history(self):
        return self.history
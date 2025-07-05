from fastapi import FastAPI
from random import randint
from datetime import datetime

app = FastAPI()

@app.get("/temperature")
def read_temperature(location: str = None):
    random_integer = randint(1, 100)
    return {"message": f"Temperature in {location} is {random_integer}"}

@app.get("/temperature/{sensor_id}")
def read_sensor_temperature(sensor_id: str):
    random_integer = randint(1, 100)
    return {
        "value": random_integer,
        "unit": "C",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "location": "Living Room",
        "status": "OK",
        "sensor_id": sensor_id,
        "sensor_type": "DHT22",
        "description": "Main living room temperature sensor"
    }
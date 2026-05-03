from dataclasses import dataclass

@dataclass
class IoTDevice:
    SEPARATOR = ","
    deviceId: int
    location: str
    data: float
    deviceType: str = "Generic"

    def serialize(self) -> str:
        """Converts object attributes to a CSV string[cite: 2]."""
        return f"{self.deviceId}{self.SEPARATOR}{self.location}{self.SEPARATOR}{self.data}{self.SEPARATOR}{self.deviceType}"

    @staticmethod
    def deserialize(row: str) -> 'IoTDevice':
        """Converts a CSV string back into a specific IoT device object[cite: 2]."""
        cols = row.split(IoTDevice.SEPARATOR)
        d_id, loc, val, d_type = int(cols[0]), cols[1], float(cols[2]), cols[3]
        
        if d_type == "Temperature":
            return TemperatureSensor(d_id, loc, val)
        elif d_type == "Humidity":
            return HumiditySensor(d_id, loc, val)
        elif d_type == "Motion":
            return MotionSensor(d_id, loc, val)
        return IoTDevice(d_id, loc, val)

class TemperatureSensor(IoTDevice):
    def __init__(self, deviceId, location, data):
        super().__init__(deviceId, location, data, "Temperature")

class HumiditySensor(IoTDevice):
    def __init__(self, deviceId, location, data):
        super().__init__(deviceId, location, data, "Humidity")

class MotionSensor(IoTDevice):
    def __init__(self, deviceId, location, data):
        super().__init__(deviceId, location, data, "Motion")
from dataclasses import dataclass

@dataclass
class IoTDevice:
    deviceId: int
    location: str
    data: int

class TemperatureSensor(IoTDevice):
    pass

class HumiditySensor(IoTDevice):
    pass

class MotionSensor(IoTDevice):
    pass
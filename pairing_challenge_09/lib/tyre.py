import datetime


class Tyre:
    def __init__(self, position, pressure, tread_depth) -> None:
        self.position = position
        self.pressure = pressure
        self.tread_depth = tread_depth
        self.readings = []
        self.make_reading(pressure, tread_depth)

    def make_reading(self, pressure, tread_depth):
        now = datetime.datetime.now()
        reading = {
            "pressure": pressure,
            "tread_depth": tread_depth,
            "date_taken": now.strftime("%d/%m/%Y"),
        }
        self.readings.append(reading)

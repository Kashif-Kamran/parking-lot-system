# create a class of parking spot


class ParkingSpot:
    def __init__(self, x, y, width, height, status, isBooked):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.statusFree = status
        self.isBooked = isBooked
        self.vehicle = None
        self.time = None

    def __str__(self):
        return f'ParkingSpot:  {self.x}, {self.y}, {self.width}, {self.height}, {self.statusFree}, {self.time}'

    def to_dict(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height, "statusFree": self.statusFree, "time": self.time}

    def getVehicle(self):
        return self.vehicle

    def getIsBooked(self):
        return self.isBooked

    def bookSpot(self, vehicle):
        self.isBooked = True
        self.vehicle = vehicle

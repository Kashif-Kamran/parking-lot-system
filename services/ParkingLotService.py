
import time
from model.ParkingSpot import ParkingSpot
import pickle


class ParkingLot:
    __instance = None

    def __init__(self):
        if ParkingLot.__instance is not None:
            raise Exception("Only one instance of ParkingLot is allowed.")
        else:
            ParkingLot.__instance = self
            self.parking_spot_list = []
            self.booked_spots = []
            self.read_pickle()

    @staticmethod
    def get_instance():
        if ParkingLot.__instance is None:
            ParkingLot()
        return ParkingLot.__instance
    # function to read picle file and return list of parking spots

    def read_pickle(self):
        with open('C:/Users/kashi/OneDrive/Desktop/DIP/Project/backend/static/CarParkPos', 'rb') as f:
            posList = pickle.load(f)

        width = 107
        height = 48

        for spot in posList:
            self.parking_spot_list.append(ParkingSpot(
                spot[0], spot[1], width, height, False, False))

    def add_parking_spot(self, parking_spot):
        self.parking_spot_list.append(parking_spot)

    def remove_parking_spot(self, parking_spot):
        self.parking_spot_list.remove(parking_spot)

    def get_parking_spot_list(self):
        return self.parking_spot_list

    def get_parking_spot_listDict(self):
        return [spot.to_dict() for spot in self.parking_spot_list]

    def print_parking_spot_list(self):
        for spot in self.parking_spot_list:
            print(spot.to_dict())


# init main functionality here
# if __name__ == "__main__":
#     # create instance of parking lot
#     parking_lot = ParkingLot.get_instance()
#     print(parking_lot.print_parking_spot_list())

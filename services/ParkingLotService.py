
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
            self.notification_list = [
                {
                    "id": 1,
                    "owner_name": "Kashif Kamran",
                    "owner_email": "kashifkamran.stud@gmail.com",
                    "no_plate": "ABC-123",
                    "color": "Red"
                },
                {
                    "id": 2,
                    "owner_name": "Amir Hussain",
                    "owner_email": "amirhussain@gmail.com",
                    "no_plate": "ABC-678",
                    "color": "Green"
                }
            ]

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

        for i, spot in enumerate(posList):
            tempSpot = ParkingSpot(
                i, spot[0], spot[1], width, height, False, False)
            self.parking_spot_list.append(tempSpot)

    def add_parking_spot(self, parking_spot):
        self.parking_spot_list.append(parking_spot)

    def remove_parking_spot(self, parking_spot):
        self.parking_spot_list.remove(parking_spot)

    def get_parking_spot_list(self):
        return self.parking_spot_list

    def add_new_notification(self, notification):
        # if notification with no_plate already exists return false else add notification and return true
        for notif in self.notification_list:
            if notif["no_plate"] == notification["no_plate"]:
                print("Notification with this no_plate already exists")
                return False
        notification["id"] = len(self.notification_list) + 1
        self.notification_list.append(notification)
        return True

    def get_notification_list(self):
        return self.notification_list


# init main functionality here
# if __name__ == "__main__":
#     # create instance of parking lot
#     parking_lot = ParkingLot.get_instance()
#     print(parking_lot.print_parking_spot_list())

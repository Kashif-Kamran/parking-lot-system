import cv2
import pickle


class ParkingSpotSelector:
    def __init__(self, image_path, spot_width, spot_height):
        self.image_path = image_path
        self.spot_width = spot_width
        self.spot_height = spot_height
        self.spot_list = []

        # Try to load the list of selected parking spots from file, or create a new list
        try:
            with open('CarParkPos.pkl', 'rb') as f:
                self.spot_list = pickle.load(f)
        except:
            pass

    def run(self):
        while True:
            # Load the image and display the selected parking spots on it
            img = cv2.imread(self.image_path)
            for spot in self.spot_list:
                cv2.rectangle(
                    img, spot, (spot[0] + self.spot_width, spot[1] + self.spot_height), (0, 255, 0), 2)
                print("Spot", spot)
            # Show the image and handle mouse clicks
            cv2.imshow("Car Park", img)
            cv2.setMouseCallback("Car Park", self.select_parking_spot)
            key = cv2.waitKey(1)

            # Save the updated list of selected parking spots to file and exit if 'q' is pressed
            if key == ord('q'):
                with open('CarParkPos', 'wb') as f:
                    pickle.dump(self.spot_list, f)
                break

    def select_parking_spot(self, events, x, y, flags, params):
        if events == cv2.EVENT_LBUTTONDOWN:
            # Add the clicked coordinate to the list of selected parking spots
            self.spot_list.append((x, y))
        if events == cv2.EVENT_RBUTTONDOWN:
            # If right-clicked on a selected spot, remove it from the list
            for i, pos in enumerate(self.spot_list):
                x1, y1 = pos
                if x1 < x < x1 + self.spot_width and y1 < y < y1 + self.spot_height:
                    self.spot_list.pop(i)


# Create an instance of the ParkingSpotSelector class and run it
selector = ParkingSpotSelector('carParkImg.png', 107, 48)
selector.run()

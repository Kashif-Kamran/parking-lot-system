import cv2
import pickle
import cvzone
import numpy as np
from datetime import datetime
#
import services.ParkingLotService as ParkingLotService
parkingLot = ParkingLotService.ParkingLot.get_instance()
# import ParkingLot

cap = cv2.VideoCapture(
    'C:/Users/kashi/OneDrive/Desktop/DIP/Project/backend/static/carPark.mp4')
# Open Pickle File
with open('C:/Users/kashi/OneDrive/Desktop/DIP/Project/backend/static/CarParkPos', 'rb') as f:
    posList = pickle.load(f)
# width and height of the parking space
width, height = 107, 48


def checkParkingSpace(imgPro, img):
    spaceCounter = 0
    parkingSpotList = parkingLot.get_parking_spot_list()
    for pos in parkingSpotList:
        x, y = pos.x, pos.y
        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            # this condition shows that the parking spot is free
            color = (0, 255, 0)
            thickness = 2
            spaceCounter += 1
            if (pos.statusFree == False):
                pos.time = datetime.now()
                pos.statusFree = True
            cv2.rectangle(img, (pos.x, pos.y), (pos.x + pos.width,
                          pos.y + pos.height), color, thickness)
            cvzone.putTextRect(img, str(pos.spotId), (x, y + height - 3), scale=1,
                               thickness=2, offset=0, colorR=color)

        else:
            color = (0, 0, 255)
            thickness = 2
            pos.time = datetime.now()
            pos.statusFree = False

        # cv2.rectangle(img, (pos.x, pos.y), (pos.x + pos.width,
        #               pos.y + pos.height), color, thickness)

    # cvzone.putTextRect(img, f'Available: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
    #                    thickness=5, offset=20, colorR=(0, 200, 0))


def getSpotsList():
    return parkingSpotList


def gen_frames():
    success, frame = cap.read()
    if not cap.isOpened():
        error_msg = cv2.error()
        print("Failed to open video file:")
        print("Error MSG : ", error_msg)
        return
    while True:
        success, frame = cap.read()  # read the camera frame
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            print("Restarting the Vedio")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        img = frame.copy()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
        checkParkingSpace(imgDilate, frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        pass

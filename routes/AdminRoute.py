
from flask import Blueprint, render_template, Response, jsonify, request, redirect
from services.vedio_reading import gen_frames
from services.ParkingLotService import ParkingLot
from model.Vehicle import Vehicle
adminRoute = Blueprint('admin', __name__, url_prefix='/admin')

parkingLot = ParkingLot.get_instance()
# Getting Pages Routes

adminInfo = {
    "name": "admin",
    "password": "admin"
}


@adminRoute.route('/dashboard')
def getDashboardPage():
    return render_template('admin/dashboard.html')


@adminRoute.route("/notification")
def getNotificationPage():
    notificationsList = parkingLot.get_notification_list()
    return render_template('admin/notification.html', notifications=notificationsList)


@adminRoute.route('/login')
def getLoginPage():
    return render_template('admin/login.html')


@adminRoute.route('/login', methods=['POST'])
def loginPost():
    formData = request.form.to_dict()

    if formData["username"] == adminInfo["name"] and formData["password"] == adminInfo["password"]:
        return render_template('admin/dashboard.html')
    else:
        return render_template('admin/login_error.html')


@adminRoute.route('/accept-notification/<int:id>')
def accept_notification(id):
    notificationList = parkingLot.get_notification_list()
    desired_notification = parkingLot.get_notification_by_id(id)

    availableSpots = [
        spot for spot in parkingLot.get_parking_spot_list() if spot.statusFree == True]

    data = {
        "notification": desired_notification,
        "availableSpots": availableSpots
    }
    return render_template('admin/accept_notification.html', data=data)
    pass


# Getting Routes Data


@adminRoute.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@adminRoute.route('/error')
def getErrorPage():
    return render_template('/admin/login_error.html')


@adminRoute.route('/get-states')
def get_states():
    stats = parkingLot.get_parking_spot_list()
    return jsonify(stats)


@adminRoute.route('/accept-notification/<int:id>', methods=["POST"])
def accept_notification_post(id):
    desired_notification = parkingLot.get_notification_by_id(id)
    formData = request.form.to_dict()
    if len(formData) == 0:
        return {"message": "Select Spot ID"}
    print("Desired ", desired_notification)
    parkingSpot = parkingLot.get_parking_spot_by_id(int(formData["spotId"]))
    if parkingSpot.statusFree == False:
        return {"message": "Spot is not free"}
    elif parkingSpot.isBooked == True:
        return {"message": "Spot is already booked"}
    vechicle = Vehicle(desired_notification["color"], desired_notification["no_plate"],
                       desired_notification["owner_name"], desired_notification["owner_email"])
    parkingSpot.bookSpot(vechicle)
    parkingLot.remove_notification_by_id(id)
    return {"message": "success"}

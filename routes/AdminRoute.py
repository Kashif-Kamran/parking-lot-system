
from flask import Blueprint, render_template, Response, jsonify, request
from services.vedio_reading import gen_frames
from services.ParkingLotService import ParkingLot
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


# initlize a list with two default objects

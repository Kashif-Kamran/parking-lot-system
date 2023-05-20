
from flask import Blueprint, render_template, Response, jsonify
from services.vedio_reading import gen_frames
import services.ParkingLotService as parkingSpotService
adminRoute = Blueprint('admin', __name__, url_prefix='/admin')


# Getting Pages Routes

adminInfo = {
    "name": "Admin",
    "password": "admin"
}


@adminRoute.route('/dashboard')
def getDashboardPage():
    return render_template('admin/dashboard.html')


@adminRoute.route("/notifications")
def getNotificationPage():
    return render_template('admin/notification.html')


@adminRoute.route('/login')
def getLoginPage():
    return render_template('admin/login.html')


@adminRoute.route('/login', methods=['POST'])
def loginPost():
    return render_template('admin/dashboard.html')


# Getting Routes Data

@adminRoute.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@adminRoute.route('/error')
def getErrorPage():
    print("Error")
    return render_template('/admin/login_error.html')


# @adminRoute.route('/get-states')
# def get_states():
#     stats = parkingSpotService.getStatisticalData()
#     return jsonify(stats)

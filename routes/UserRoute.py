from services.ParkingLotService import ParkingLot
from model.Vehicle import Vehicle
from flask import Blueprint, render_template, Response, jsonify, request
userRoute = Blueprint('user', __name__, url_prefix='/user')
parkingLot = ParkingLot.get_instance()
# Page Getting Routes


@userRoute.route('/request-parking')
def getLoginPage():
    response = {
        "status": True,
        "message": ""
    }
    return render_template('user/request_spot.html', response=response)


@userRoute.route("/request-parking", methods=['POST'])
def registerPost():
    data = request.form.to_dict()
    result = parkingLot.add_new_notification(data)
    if result:
        response = {
            "status": True,
            "message": "Notification added successfully"
        }
        return render_template('user/request_spot.html', response=response)
    else:
        response = {
            "status": False,
            "message": "Notification with this no_plate already exists"
        }
        return render_template('user/request_spot.html', response=response)


@userRoute.route('/dashboard')
def getDashboardPage():
    spots = parkingLot.get_booked_spots()
    print("Here")
    [print(x.to_dict()) for x in spots]
    return render_template('user/dashboard.html', spots=spots)
    pass


from flask import Blueprint, render_template, Response, request, jsonify
import services.ParkingLotService as parkingSpotService
from services.vedio_reading import gen_frames, getSpotsList
spot = Blueprint('spot', __name__, url_prefix='/spot')


@spot.route('/getSpots')
def getSpots():
    parkingSpots = getSpotsList()
    return jsonify([x.to_dict() for x in parkingSpots if x.statusFree == True])

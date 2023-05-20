from flask import Blueprint, render_template, Response, jsonify
userRoute = Blueprint('user', __name__, url_prefix='/user')


# Page Getting Routes
@userRoute.route('/request-parking')
def getLoginPage():
    return render_template('user/register.html')

# import routes from routes folder
from routes.AdminRoute import adminRoute
from routes.UserRoute import userRoute

from flask import Flask, render_template
app = Flask(__name__)
app.register_blueprint(adminRoute)
app.register_blueprint(userRoute)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/error")
def getErrorPage():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)

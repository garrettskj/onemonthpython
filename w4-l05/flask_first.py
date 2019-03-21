from flask import Flask, render_template

import darkskyapi

application = Flask(__name__)



@application.route("/")
def hello():
    greetingpy = "well hello there!"
    return render_template("index.html", greetingjinja=greetingpy)

@application.route("/weather")
def weather():
    return render_template("weather.html", get_weather=darkskyapi.get_weather('45.585709', '-122.590981'))

if __name__ == "__main__":
    application.run(host='0.0.0.0', port='80')

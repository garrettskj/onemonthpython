from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    greetingpy = "well hello there!"
    return render_template("index.html", greetingjinja=greetingpy)

@application.route("/weather")
def weather():
    get_weather = "the weather is..."
    return render_template("weather.html", get_weather=get_weather)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port='80')

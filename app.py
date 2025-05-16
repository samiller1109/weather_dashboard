import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash
import requests

load_dotenv()
API_KEY = os.getenv("OWM_API_KEY")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "you-should-set-this")

OWM_URL = "https://api.openweathermap.org/data/2.5/weather"
ONECALL_URL = "https://api.openweathermap.org/data/2.5/onecall"

def get_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    resp = requests.get(OWM_URL, params=params)
    if resp.status_code != 200:
        return None, resp.json().get("message", "Error fetching data.")
    data = resp.json()
    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["icon"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"],
    }
    return weather, None

def get_forecast(lat: float, lon: float):
    params = {
        "lat": lat,
        "lon": lon,
        "exclude": "current,minutely,hourly,alerts",
        "units": "metric",
        "appid": API_KEY,
    }
    resp = requests.get(ONECALL_URL, params=params).json()
    forecast = []
    for day in resp["daily"][1:6]:
        forecast.append({
            "date": datetime.utcfromtimestamp(day["dt"]).strftime("%a %b %d"),
            "icon": day["weather"][0]["icon"],
            "min": day["temp"]["min"],
            "max": day["temp"]["max"],
            "desc": day["weather"][0]["description"].title(),
        })
    return forecast

@app.route("/", methods=["GET", "POST"])
def dashboard():
    weather = None
    forecast = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if not city:
            flash("Please enter a city name.", "warning")
        else:
            weather, error = get_weather(city)
            if error:
                flash(f"Could not get weather for '{city}': {error}", "danger")
            else:
                forecast = get_forecast(weather["lat"], weather["lon"])

    return render_template("dashboard.html", weather=weather, forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import requests
import sqlite3

app = Flask(__name__)


def get_db():
    db = sqlite3.connect("mausam.db")
    db.row_factory = sqlite3.Row
    return db


def get_weather(city):

    # Find city
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    if "results" not in geo_data:
        return None

    location = geo_data["results"][0]

    # Get weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "forecast_days": 5,
        "timezone": "auto"
    }

    response = requests.get(weather_url, params=weather_params)

    if response.status_code != 200:
        return None

    data = response.json()

    forecast = []

    for i in range(5):
        forecast.append({
            "date": data["daily"]["time"][i],
            "max": data["daily"]["temperature_2m_max"][i],
            "min": data["daily"]["temperature_2m_min"][i],
            "rain": data["daily"]["precipitation_probability_max"][i]
        })

    return {
        "city": location["name"],
        "temperature": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "wind": data["current"]["wind_speed_10m"],
        "forecast": forecast
    }


@app.route("/", methods=["GET", "POST"])
def index():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form["city"]

        weather = get_weather(city)

        if weather is None:
            error = "City not found."

    elif request.method == "GET" and request.args.get("city"):

        city = request.args.get("city")

        weather = get_weather(city)

        if weather is None:
            error = "City not found."

    db = get_db()

    cities = db.execute(
        "SELECT * FROM cities"
    ).fetchall()

    db.close()

    return render_template(
        "index.html",
        weather=weather,
        cities=cities,
        error=error
    )



@app.route("/save", methods=["POST"])
def save():

    city = request.form["city"]

    db = get_db()

    existing = db.execute(
        "SELECT * FROM cities WHERE name = ?",
        (city,)
    ).fetchone()

    if not existing:

        db.execute(
            "INSERT INTO cities (name) VALUES (?)",
            (city,)
        )

        db.commit()

    db.close()

    return redirect("/")


@app.route("/delete/<int:city_id>")
def delete(city_id):

    db = get_db()

    db.execute(
        "DELETE FROM cities WHERE id = ?",
        (city_id,)
    )

    db.commit()
    db.close()

    return redirect("/")


if __name__ == "__main__":

    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    db.commit()
    db.close()

    app.run(debug=True)
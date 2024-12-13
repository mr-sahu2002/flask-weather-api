from flask import Flask, jsonify, request
from fetch_data import fetch_weather_data
from database import save_to_database, get_all_weather_data, get_weather_data_by_city
from database import init_db

app = Flask(__name__)

# List of cities for which weather data is fetched
CITIES = ["New York", "London", "Paris", "Tokyo", "Mumbai"]

# Initialize the database before starting the app
init_db()

# POST /fetch-weather: Fetches weather data for the cities and saves it to the database
@app.route("/fetch-weather", methods=["POST"])
def fetch_weather():
    weather_data = fetch_weather_data(CITIES)
    save_to_database(weather_data)
    return jsonify({"message": "Weather data fetched and saved successfully."}), 201

# GET /weather-data: Returns all stored weather data in JSON format
@app.route("/weather-data", methods=["GET"])
def get_all_weather_data_endpoint():
    data = get_all_weather_data()
    weather_data = [
        {"city": row[0], "temperature": row[1], "humidity": row[2], "weather": row[3], "timestamp": row[4]}
        for row in data
    ]
    return jsonify(weather_data)

# GET /weather-data/<city>: Returns the weather data for a specific city
@app.route("/weather-data/<city>", methods=["GET"])
def get_city_weather(city):
    row = get_weather_data_by_city(city)
    if row:
        weather_data = {"city": row[0], "temperature": row[1], "humidity": row[2], "weather": row[3], "timestamp": row[4]}
        return jsonify(weather_data)
    return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

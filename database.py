import sqlite3
from datetime import datetime

# Initialize the database
def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                    (id INTEGER PRIMARY KEY,
                    city TEXT,
                    temperature REAL,
                    humidity INTEGER,
                    weather_description TEXT,
                    timestamp TEXT)''')
    conn.commit()
    conn.close()

# Save the weather data to the database
def save_to_database(weather_data):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    for data in weather_data:
        cursor.execute('''
            INSERT INTO weather (city, temperature, humidity, weather_description, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['city'], data['temperature'], data['humidity'], data['weather'], datetime.fromtimestamp(data['timestamp'])))
    
    conn.commit()
    conn.close()

# Retrieve all weather data from the database
def get_all_weather_data():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT city, temperature, humidity, weather_description, timestamp FROM weather")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Retrieve weather data for a specific city
def get_weather_data_by_city(city):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT city, temperature, humidity, weather_description, timestamp FROM weather WHERE city=?", (city,))
    row = cursor.fetchone()
    conn.close()
    return row

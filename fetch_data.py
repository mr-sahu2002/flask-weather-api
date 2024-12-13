import requests

def fetch_weather_data(cities):
    api_key = 'your_api_key' 
    weather_data = []

    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data.append({
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["description"],
                "timestamp": data["dt"]  # UNIX timestamp of the weather data
            })
        else:
            print(f"Failed to fetch data for {city}: {data.get('message', 'Unknown error')}")

    return weather_data

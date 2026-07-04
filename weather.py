import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"{temp}°C with {weather}"

    return "City not found"

import requests

API_KEY = 'your_api_key_here'

def fetch_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    return response.json()

def get_location_from_user():
    city = input("Enter the city name to get its current weather: ")
    return city


def display_weather(data):
    if data["cod"] != 200:
        print("Failed to retrieve weather data.")
        return

    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"Weather: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")

def main():
    city = get_location_from_user()
    weather_data = fetch_weather_data(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()

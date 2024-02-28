import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'YOUR_API_KEY'
city_name = 'London'  # Example city
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Extract temperature and weather description
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    print(f"Current weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Weather Description: {weather_description}")
else:
    print("Failed to retrieve data from OpenWeatherMap API.")

import requests

# OpenWeatherMap API Key
api_key = "YOUR_API_KEY_HERE"

# Base URL for OpenWeatherMap API
weather_url = "http://api.openweathermap.org/data/2.5/weather"

# Fetch the list of users from JSONPlaceholder
users_url = "https://jsonplaceholder.typicode.com/users"
users_response = requests.get(users_url)
users = users_response.json()

# Assign each user a fictional set of latitude and longitude coordinates
coordinates = [
    (40.7128, -74.0060),  # New York
    (34.0522, -118.2437), # Los Angeles
    (41.8781, -87.6298),  # Chicago
    (29.7604, -95.3698),  # Houston
    (33.4484, -112.0740), # Phoenix
]

# Loop through each user and fetch the current weather for their location
for user, coord in zip(users, coordinates):
    lat, lon = coord
    full_weather_url = f"{weather_url}?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    weather_response = requests.get(full_weather_url)
    weather_data = weather_response.json()

    # Extract the temperature and weather description
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']

    # Construct and print a personalized weather alert message
    message = f"Hello {user['name']}, the current weather at your location is {weather_description} with a temperature of {temperature}°C."
    print(message)

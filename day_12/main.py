from datafetcher import fetch_weather_data
from dataanalyzer import calculate_average_temperature
from presenter import present_weather_summary

API_URL = 'http://api.openweathermap.org/data/2.5/forecast'
API_KEY = 'your_api_key_here'  # Replace with your actual API key

city = 'London'
weather_data = fetch_weather_data(API_URL, API_KEY, city)
average_temp = calculate_average_temperature(weather_data)
present_weather_summary(city, average_temp)

import requests

def fetch_weather_data(api_url, api_key, city):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(api_url, params=params)
    return response.json()

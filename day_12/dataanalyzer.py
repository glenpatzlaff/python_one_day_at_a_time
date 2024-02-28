def calculate_average_temperature(weather_data):
    temps = [forecast['main']['temp'] for forecast in weather_data['list']]
    return sum(temps) / len(temps)

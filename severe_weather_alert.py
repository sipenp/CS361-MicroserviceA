# Author: Nathan Sipe
# GitHub username: sipenp
# Date: 02/15/2025
# Description: 
# Microservice for getting severe weather alert

# Import:
import requests
from flask import Flask, request, jsonify
app = Flask(__name__)

with open('key.env', 'r') as file:
    api_key = file.readline()

city_check = f"http://api.openweathermap.org/geo/1.0/" #URL to get latitude and longitude for city
open_weather_url = "https://api.openweathermap.org/data/3.0/onecall" #URL to check for severe weather alerts


@app.route('/get_severe_weather')
def get_severe_weather (city_name = None):
    # Check if city name is omitted
    if city_name is None:
        city_name = request.args.get('city_name')

    if city_name is None:
        return jsonify('Error:', "City name required"), 500

    # Create city url to get gps coordinates
    city_name_url = f"{city_check}direct?q={city_name}&limit=1&appid={api_key}"
    city_coord = requests.get(city_name_url)
    # return error if city doesn't exist
    if city_coord.status_code != 200 or not city_coord.json():
        return jsonify({"Error": "City not found"}), 404

    city_coord_data = city_coord.json()[0]

    lat, lon = city_coord_data['lat'], city_coord_data['lon']

    # Create URL to query weather data
    check_alert_url = f'{open_weather_url}?lat={lat}&lon={lon}&appid={api_key}'
    weather = requests.get(check_alert_url)
    # Check for data fetch failure
    if weather.status_code != 200:
        return jsonify('Error:', 'Weather alert fetch failed'), 500

    # Filter for severe weather alerts and return data
    alerts_data = weather.json().get('alerts')
    if not alerts_data:
        return {'Status': "No severe weather alerts."}

    alerts_summary = []

    for alert in alerts_data:
        alerts_summary.append(
            {'type': alert.get('event', 'Unknown event'),
             'severity': alert.get('severity', 'Unknown severity'),
             'description': alert.get('description', 'No description available')})

    return jsonify({'alerts': alerts_summary})

# Main:


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

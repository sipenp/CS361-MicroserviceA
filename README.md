# CS361-MicroserviceA
## Microservice A for Farad's Severe Weather Alert
### Description
Checks for severe weather alerts for a given city. 
Inputs: 
- City name
Outputs:
- Severe weather alerts
- - No severe weather alerts
- Errors:
  - No city name provided
  - Invalid city provided
  - Weather fetch failed
### Communication Contract
Communications will be handled via RESTful API requests.  The microservice will run as a Flask application with the address of 
[http://127.0.0.1:5001](http://127.0.0.1:5001).
To call the microservice the following can be used:
\'\'\'python
city_name = 'some_city'
call_url = 'http://127.0.0.1:5001/severe_weather_check?city_name = {city_name}'
alerts = request.get(city_url).json 
\'\'\'
Alerts data will be returned in json format with the city name and a list of alerts as dictionaries.

The keys for the alert infomration are:
- Type
- Severity
- Description



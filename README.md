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
To call the microservice generate the url that contains the local host, port, route for the microservice, and the query with the city name.  The route is 
[/get_severe_weather](/get_severe_weather). The city name parameter is 'city_name'.

See example below for constructing the call and receiving the data via python's request function.  
```python
city_name = 'some_city'
call_url = 'http://127.0.0.1:5001/severe_weather_check?city_name = {city_name}'
alerts = request.get(city_url).json # requesting and receiving data
```
Alerts data will be returned in json format with the city name and a list of alerts as dictionaries.

The keys for the alert infomration are:
- Type
- Severity
- Description



### Running the Microservice
To run the microservice open a terminal to the folder where sever_weather_alert.py is located and enter the following command:

```
python severe_weather_alert.py
```

### Using the Microservice
To use the microservice simply construct the URL and perform an HTTP GET operation as appropriate for the programming languate being used.


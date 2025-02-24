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
[http://127.0.0.1:5001](http://127.0.0.1:5001)

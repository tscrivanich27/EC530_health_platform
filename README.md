# EC 530 Project #2: Health Platform

Project Description: This project is a platform that can be used to monitor patients at home or in a hospital.

## Branching Strategy

Branches are defined by the required modules for this project. Currently, the branches in this project include:

* device-module branch
* chat-module branch
* voice-transcriber branch

Strategy:

* Each branch will be added to the main branch when testing (unit/integration) is complete and the phase for the module has ended.
* Continuous Integration will occur in a branch during its respective phase in the project. 

## Device Module

Utilized the Flask module in Python to create a REST API that will handle all devices on the health platform.

Dependencies: 

* flask
* flask_restful 
* requests
* json

Using the requests module, the API recieves a json file from http://127.0.0.1:5000/devices/"file_name". The API will check to ensure that it includes the following parameters:

1) Device ID (string): Used to assign/match the device with a patient
2) Device Serial Number (int): Used to check the type of device. The type of device will indicate the data that should come in  
3) Data (dict): Information for the patient and medical professional. Includes blood pressure, temperature, pulse, weight, glucose levels, and oxygen levels

Unit Tests:

1) JSON file with no Device ID -> Program should abort with an error message
2) JSON file with invalid Device ID type -> Program should abort with an error message
3) JSON file with no Device Serial Number -> Program should abort with an error message
4) JSON file with invalid Device Serial Number type -> Program should abort with an error message
5) JSON file with no Device Data -> Program should abort with an error message
6) JSON file with invalid Device Data type -> Program should abort with an error message

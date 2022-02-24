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

## Database:

For this project, I am using MongoDB as the database which will contain all patient, medical professional, and administrator data. 

Dependencies:

* pymongo

Here is the schema for documents in the device module:

![#1](https://user-images.githubusercontent.com/73702777/155610109-038f8918-134e-44d1-a68f-8c0521517fca.JPG)

Here is an image of the contents of the cluster in MongoDB, titled "Health-Platform":

![#2](https://user-images.githubusercontent.com/73702777/155610575-7377659c-c8ef-42f6-8355-44f054ac33eb.JPG)

## User Instructions

1) Download or clone the repository to local machine
2) Navigate to EC530_Health_Platform directory from terminal

Example (Windows OS):

![#1](https://user-images.githubusercontent.com/73702777/153893406-f3009d27-fac4-4fc3-a04e-40606111765a.JPG)

3) Type the command "Python device_module.py" 

Example (Windows OS):

![#2](https://user-images.githubusercontent.com/73702777/153893753-365aa0ab-ab1f-4c5b-a779-ffbdc23c3c08.JPG)

4) Open a new terminal. Repeat Step 2

Example (Windows OS):

![#3](https://user-images.githubusercontent.com/73702777/153894200-1792c23a-e620-45a9-9c95-89aeea9b4739.JPG)

5) Type the command "Python test.py" in the new terminal.

Example (Windows OS):

![#4](https://user-images.githubusercontent.com/73702777/153894480-eba5a377-37f1-44e3-b92f-57bdf7a0be16.JPG)

6) Type the command "example.log" in the new terminal to open the log file.

Example (Windows OS):

![#5](https://user-images.githubusercontent.com/73702777/153895258-7abab278-1bd2-4bb5-8c0a-16f1c7a4b2f1.JPG)

![#6](https://user-images.githubusercontent.com/73702777/153895364-452dc01e-0cee-47d4-b5ad-4ba85943d7c8.JPG)

## References

* Briggs, James. "The Right Way to Build an API with Python." _Towards Data Science_, 11 September 2020, https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f. Accessed 12 February 2022.

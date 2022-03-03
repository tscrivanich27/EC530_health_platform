#!/usr/bin/env python

# Modules for device_module.py
from datetime import datetime
import json
from flask import Flask
from flask_restful import Resource, Api, abort
from bson import json_util
from mongoDB import get_database

# Initialize the Flask REST API
def create_app():
    myapp = Flask(__name__)
    return myapp 

app = create_app()
api = Api(app)

# Initialize the MongoDB database
db = get_database()
collection_name = db["device_data"]

# Function to check for Device ID
def abort_if_device_id_not_valid(data):
    key = "device_ID"
    # If Device ID not present or wrong type...abort with 404 error code
    if (key not in data["device"][0]) or (type(data["device"][0]["device_ID"]) != str):
        abort(404, message="The device ID is not present or has an invalid type")

# Function to check for Device Serial Number
def abort_if_device_serial_number_not_valid(data):
    key = "serial_number"
    # If Device Serial Number not present or wrong type...abort with 404 error code
    if (key not in data["device"][0]) or (type(data["device"][0]["serial_number"]) != int):
        abort(404, message="The serial number is not present or has an invalid type")

# Function to check for Data
def abort_if_data_not_valid(data):
    key = "data"
    # If Device Data not present or wrong type...abort with 404 error code
    if (key not in data["device"][0]) or (type(data["device"][0]["data"]) != dict):
        abort(404, message="The data is not present or has an invalid type")

class Devices(Resource):
    # Get function 
    def get(self, file_name):
        # Open the json input file
        f = open(file_name)
        # Format the contents as a Python dictionary
        data = json.load(f)
        # Check the structure of the dictionary
        # If any contents are missing...abort with message
        abort_if_device_id_not_valid(data)
        abort_if_device_serial_number_not_valid(data)
        abort_if_data_not_valid(data)
        # If all contents are present...send data to device_data collection in MongoDB
        json_data = json.loads(json_util.dumps(data))
        collection_name.insert_one(json_data)
        # If all contents are present...return the data with 200 status code
        current_date = str(datetime.today())
        data["device"][0].update({'date':current_date})
        return data, 200

class Chat(Resource):
    def get(self, file_name):
        f = open(file_name)

# Add resource to the API
# Parameter: json file
api.add_resource(Devices, '/devices/<string:file_name>')

# Main function 
if __name__ == '__main__':
    app.run(debug=True)
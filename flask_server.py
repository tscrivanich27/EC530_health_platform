#!/usr/bin/env python

# Modules for flask_server.py
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
device_collection = db["device"]
chat_collection = db["chat"]

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

# Function to check for sender ID
def abort_if_sender_id_not_valid(data):
    key = "sender_ID"
    if (key not in data["chat"][0]) or (type(data["chat"][0]["sender_ID"]) != str):
        abort(404, message="The sender ID is not present or has an invalid type")

# Function to check for sender name
def abort_if_user_sender_not_valid(data):
    key = "sender"
    if (key not in data["chat"][0]) or (type(data["chat"][0]["sender"]) != str):
        abort(404, message="The user sender is not present or has an invalid type")

# Function to check for receiver ID
def abort_if_reciever_id_not_valid(data):
    key = "receiver_ID"
    if (key not in data["chat"][0]) or (type(data["chat"][0]["receiver_ID"]) != str):
        abort(404, message="The receiver ID is not present or has an invalid type")

# Function to check for receiver name
def abort_if_user_reciever_not_valid(data):
    key = "receiver"
    if (key not in data["chat"][0]) or (type(data["chat"][0]["receiver"]) != str):
        abort(404, message="The user receiver is not present or has an invalid type")

# Function to check for the message 
def abort_if_message_not_valid(data):
    key = "message"
    if (key not in data["chat"][0]) or (type(data["chat"][0]["message"]) != str):
        abort(404, message="The message is not present or has an invalid type")

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
        # Add timestamp to json object
        current_date = str(datetime.today())
        data["device"][0].update({'date':current_date})
        # If all contents are present...send data to device_data collection in MongoDB
        json_data = json.loads(json_util.dumps(data))
        device_collection.insert_one(json_data)
        # If all contents are present...return the data with 200 status code
        return data, 200

class Chat(Resource):
    # Get function
    def get(self, file_name):
        # Open the json input file
        f = open(file_name)
        # Format the contents as a Python dictionary
        data = json.load(f)
        # Check the structure of the dictionary
        # If any contents are missing...abort with message
        abort_if_sender_id_not_valid(data)
        abort_if_user_sender_not_valid(data)
        abort_if_reciever_id_not_valid(data)
        abort_if_user_reciever_not_valid(data)
        abort_if_message_not_valid(data)
        # Add timestamp to json object
        current_date = str(datetime.today())
        data["chat"][0].update({'date':current_date})
        # If all contents are present...send data to device_data collection in MongoDB
        json_data = json.loads(json_util.dumps(data))
        chat_collection.insert_one(json_data)
        # If all contents are present...return the data with 200 status code
        return data, 200

# Add resource to the API
# Parameter: json file
api.add_resource(Devices, '/devices/<string:file_name>')
api.add_resource(Chat, '/chat/<string:file_name>' )

# Main function 
if __name__ == '__main__':
    app.run(debug=True)
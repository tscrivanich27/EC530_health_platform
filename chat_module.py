#!/usr/bin/env python

# Modules for chat_module.py
import json
from flask import Flask
from flask_restful import Resource, Api, abort

# Initialize the Flask REST API
def create_app():
    myapp = Flask(__name__)
    return myapp 

app = create_app()
api = Api(app)

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

class Chat(Resource):
    # Get Function 
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
        # If all contents are present...return the data with 200 status code
        return data, 200

# Add resource to the API
# Parameter: json file
api.add_resource(Chat, '/chat/<string:file_name>')

# Main function 
if __name__ == '__main__':
    app.run(debug=True)
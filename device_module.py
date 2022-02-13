#!/usr/bin/env python

import json
from flask import Flask
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

def abort_if_device_id_not_valid(data):
    key = "device_ID"
    if (key not in data["device"][0]) or (type(data["device"][0]["device_ID"]) != str):
        abort(404, message="The device ID is not present or has an invalid type")

def abort_if_device_serial_number_not_valid(data):
    key = "serial_number"
    if (key not in data["device"][0]) or (type(data["device"][0]["serial_number"]) != int):
        abort(404, message="The serial number is not present or has an invalid type")

def abort_if_data_not_valid(data):
    key = "data"
    if (key not in data["device"][0]) or (type(data["device"][0]["data"]) != dict):
        abort(404, message="The data is not present or has an invalid type")

class Devices(Resource):
    def get(self, file_name):
        f = open(file_name)
        data = json.load(f)
        abort_if_device_id_not_valid(data)
        abort_if_device_serial_number_not_valid(data)
        abort_if_data_not_valid(data)
        return {"data": data}, 200

api.add_resource(Devices, '/devices/<string:file_name>')

if __name__ == '__main__':
    app.run(debug=True)
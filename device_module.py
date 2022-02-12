#!/usr/bin/env python

import json
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
class Devices(Resource):
    def get(self):
        user = ""
        f = open("data.json")
        data = json.load(f)
        if data['device'][0]["device_ID"] == "F5hgu479fn2":
            user = "Jim"
            return {user: data["device"][0]["data"]}, 200
        else:
            return {}, 200

api.add_resource(Devices, '/devices')

if __name__ == '__main__':
    app.run()
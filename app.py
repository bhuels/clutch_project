# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 2020

@author: Bryan Huelsbeck (bhuels@gmail.com)
"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
import psycopg2

app = Flask(__name__)
api = Api(app)

API_KEY = '<PLACE YOUR GOOGLE MAP API KEY HERE>' # Replace with your Google Maps API key

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?' # Google Map API URL to retreive map data
hostname = 'app_db_1' # Connect to Docker Container ip
username = 'docker' # Postgresql database admin user
password = 'docker' # Replace with your Postgresql database password
database = 'gis' # Postgresql database name where geometry data is stored
port = 5000 # port the app runs on

parser = reqparse.RequestParser()

class StateInfo(Resource):
    def get(self):
        # Identify address and build params with API key and address
        parser.add_argument('address', required=True)
        args = parser.parse_args()
        address = args['address']
        params = {
            'key': API_KEY,
            'address': address
        }

        # Request information from Google Maps API
        response = requests.get(base_url, params=params).json()
        response.keys()

        # Check response status and extract longitude and latitude
        if response['status'] == 'OK':
            geometry = response['results'][0]['geometry']
            lng = geometry['location']['lng']
            lat = geometry['location']['lat']

        # Connect to PostGIS enabled database and pull state name
        conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        cur = conn.cursor()
        sql = """SELECT stusps,
                    name
                 FROM cb_2018_us_state_20m
                 WHERE st_contains(geom, st_geometryfromtext('POINT(%s %s)', 0));"""
        cur.execute(sql, (lng, lat))
        states = cur.fetchall()

        return states

api.add_resource(StateInfo, '/findstate')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

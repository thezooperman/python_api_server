import os
from json import dumps

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///data/chinook.db', echo=True)
app = Flask(__name__)
api = Api(app)
app.config['DEBUG'] = os.environ.get('DEBUG', False)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        # This line performs query and returns json result
        query = conn.execute("select * from employees")
        # Fetches first column that is Employee ID
        return {'employees': [i[0] for i in query.cursor.fetchall()]}


class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(
            "select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute(
            "select * from employees where EmployeeId =%d " % int(employee_id))
        result = {'data': [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        return jsonify(result)


class Genres(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from genres;")
        result = {'data': [dict(zip(tuple(query.keys()), i))
                           for i in query.cursor]}
        return jsonify(result)


api.add_resource(Employees, '/employees')  # Route_1
api.add_resource(Tracks, '/tracks')  # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3
api.add_resource(Genres, '/genres')  # Route 4


if __name__ == '__main__':
    app.run(port='5002')

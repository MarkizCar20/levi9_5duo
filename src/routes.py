from flask import Flask
from flask_restful import Resource, Api
import csv

with open('L9HomeworkChallengePlayersInput.csv', newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return { 'hello':'world' }

api.add_resource(HelloWorld, '/')
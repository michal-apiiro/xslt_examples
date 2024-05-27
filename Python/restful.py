from flask import Flask, request
from flask_restful import Resource, Api, req

app = Flask(__name__)
api = Api(app)


class TodoSimple(Resource):
    def get(self):
        return 'Hi'
    
    def post(self):
        return 'Hi'

class Index(Resource):
    def get(self):
        return 'Hi'
    
    def post(self):
        return 'Hi'
    
api.add_resource(TodoSimple, '/todos/<string:todo_id>')
api.add_resource(Index, '/index/<string:index_id>')

if __name__ == '__main__':
    app.run(debug=True)

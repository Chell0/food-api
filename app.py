from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Order(Resource):
    def get(self, order_id):
        return {'order': order_id}


api.add_resource(Order, '/v1/order/<string:order_id>')

app.run(port=5000)

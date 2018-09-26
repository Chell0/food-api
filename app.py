from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

orders = []

class Order(Resource):
    def get(self, order_id):
        for order in orders:
            if order['order_id'] == order_id:
                return order
        return {'order': None}, 404

    def post(self, order_id):
        order = {'id': order_id, 'title': "Cheese Burger", 'price': 250}
        orders.append(order)
        return order, 201


api.add_resource(Order, '/v1/orders/<string:order_id>')

app.run(port=5000)

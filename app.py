from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'thisismysecretkey'
api = Api(app)

orders = []

class Order(Resource):
    def get(self, order_id):
        for order in orders:
            if order['order_id'] == order_id:
                return order
        return {'order': None}, 200 if order else 404

    def post(self, order_id):
        data = request.get_json()
        order = {'id': order_id, 'title': data['title'], 'price': data['price']}
        orders.append(order)
        return order, 201


class OrderList(Resource):
    def get(self):
        return {'orders': orders}

api.add_resource(Order, '/v1/orders/<string:order_id>')
api.add_resource(OrderList, '/v1/orders')

app.run(port=5000, debug=True)

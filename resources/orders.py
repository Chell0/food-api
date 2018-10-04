from flask_restful import Resource, reqparse


orders = []


class Order(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="Please fill in this field!"
                        )

    def get(name):
        # Look through all orders looking for a specific order using the name requested
        order = next(filter(lambda x: x['name'] == name, orders), None)
        return {'order': order}, 200 if order else 404

    def post(self, name):
        # Deal with the errors first
        if next(filter(lambda x: x['name'] == name, orders), None):
            return {'message': "An order with the name '{}' already exists.".format(name)}, 400

        # load data
        data = Order.parser.parse_args()

        order = {'name': name, 'price': data['price']}
        orders.append(order)
        return order, 201

    def delete(self, name):
        global orders
        orders = list(filter(lambda x: x['name'] != name, orders))
        return {'message': 'Order deleted'}

    def put(self, name):
        # load data
        data = Order.parser.parse_args()

        order = next(filter(lambda x: x['name'] == name, orders), None)
        if order is None:
            order = {'name': name, 'price': data['price']}
            orders.append(order)
        else:
            order.update(data)
        return order


class OrderList(Resource):
    def get(self):
        return {'orders': orders}

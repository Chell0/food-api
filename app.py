from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)


mac = api.model('Order',
                {
                    'order': fields.String('The order.')
                })

orders = []
beef_burger = {
    'order': 'Beef-burger',
    'status': 'pending'
}
orders.append(beef_burger)


@api.route('/v1/orders')
class Order(Resource):
    """The parent class"""
    # Let's request for all orders

    def get(self):
        """Get all orders"""
        return orders

    # Let's place an new order
    @api.expect(mac)
    def post(self):
        """Post a new order"""
        create_order = api.payload
        create_order['id'] = len(orders) + 1
        orders.append(create_order)
        return {'result': 'Order successfully created'}, 201

    # Let's retrieve an order by it's id
    @api.expect(mac)
    def get_by_id(self):
        """Get order by Id"""
        for order in self.orders:
            if order['id'] == id:
                return order
        api.abort(404, "Order {} doesn't exist".format(id))


if __name__ == '__main__':
    app.run(debug=True)

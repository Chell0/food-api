import flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

app = flask.Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Fast-Food-Fast API',
          description='A simple Food API',
          )

mac = api.namespace('orders', description='Order operations')

order = api.model('Order', {
    "id": fields.Integer(readOnly=True),
    "name": fields.String(required=True, description='Order name'),
    "status": fields.String(required=True, description='The order status')
})

status = api.model('Status', {
    "status": fields.String(required=True, description='The order status')
})


class OrderDAO(object):
    def __init__(self):
        self.count = 0
        self.orders = []

    # Get order by id
    def get(self, id):
        for order in self.orders:
            if order['id'] == id:
                return order
            api.abort(404, "Order {} doesn't exist".format(id))

    # Create an Order
    def create(self, data):
        order = data
        order['id'] = self.count = self.count + 1
        self.orders.append(order)
        return order

    # Update an order
    def update_order(self, id, status):
        order = self.get(id)
        order.update(status)
        return order

    # Delete an order by id
    def delete_order(self, id):
        order = self.get(id)
        self.orders.remove(order)


DAO = OrderDAO()


# GET all, POST
@api.route('/v1/orders')
class OrderList(Resource):
    """Shows a list of all orders, and lets you POST to add new orders"""
    @mac.doc('list_orders')
    @mac.marshal_list_with(order)
    def get(self):
        """List all orders"""
        return DAO.orders

    @mac.doc('create_order')
    @mac.expect(order)
    @mac.marshal_with(order, code=201)
    def post(self):
        """Create a new order"""
        return DAO.create(api.payload), 201


# GET by id, POST, PUT
@api.route('/v1/orders/<int:id>')
@mac.response(404, 'Order not found')
@mac.param('id', 'The order id')
class Order(Resource):
    """Show a single order item and lets you delete them"""
    @mac.doc('get_order')
    @mac.marshal_with(order)
    def get(self, id):
        """Fetch a given order id"""
        return DAO.get(id)

    @mac.doc('delete_order')
    @mac.response(204, 'Order deleted')
    def delete(self, id):
        """Delete an order by it's id"""
        DAO.delete_order(id)
        return '', 204

    @mac.expect(status)
    @mac.marshal_with(order)
    def put(self, id):
        """Update an order given its id"""
        return DAO.update_order(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)
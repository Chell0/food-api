from flask import Flask
from flask_restful import Api

# Local imports
from resources.orders import Order, OrderList

# Our App
app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = True

# GET, PUT
api.add_resource(Order, '/v1/orders/<int:orderId>')
# GET all, POST
api.add_resource(OrderList, '/v1/orders')

if __name__ == '__main__':
    # runs the application on a localhost
    app.run(debug=True)

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Orders = []

class Order(Resource):
    def get(self, order_id):
        return {'orders': order_id}


api.add_resource(Order, '/v1/orders/<string:order_id>')


if __name__ == '__main__':
    app.run(debug=True)


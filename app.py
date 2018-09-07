from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for


app = Flask(__name__)



"""
Orders stored in data structures
"""
orders = [
	{
		'id': 1,
		'title': 'Chicken Burger',
		'description': 'Lemon basted chicken patty, Mayo shredded lettuce, Tomato slice, Sesame seed bun',
		'done': False
	},
	{
		'id': 2,
		'title': 'Chicken Salad',
		'description': 'Chicken breast strips, Cucumber, Lettuce, Carrots, Tomato wedges, 1000 island dressing',
		'done': False
	},
	{
		'id': 3,
		'title': 'Veggie Burger',
		'description': 'Veggie patty, Shredded lettuce, Tomato slice, Dills, Relish sauce, Sesame seed bun',
		'done': False
	},
	{
		'id': 4,
		'title': 'Green Salad',
		'description': 'Cucumber, Lettuce, Red onion, Tomato wedges, Green pepper',
		'done': False
	}
]



def make_public_order(order):
    new_order = {}
    for food in order:
        if food == 'id':
            new_order['uri'] = url_for('get_order', order_id = order['id'], _external = True)
        else:
            new_order[food] = order[food]
    return new_order



"""REST Endpoints for Resources (CRUD)"""

"""
The GET method used to return the data of all the orders
"""
@app.route('/food/api/v1/orders', methods=['GET'])
def get_orders():
	return jsonify({'orders': [make_public_order(order) for order in orders]})


"""
The GET method used to return the data of a single order
"""
@app.route('/food/api/v1/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = filter(lambda o: o['id'] == order_id, orders)
    if len(order) == 0:
        abort(404)
    return jsonify({'order': make_publice_order(order[0])})
	

"""
The POST method, which we will use to place a new order
"""
@app.route('/food/api/v1/orders', methods=['POST'])
def create_order():
    if not request.json or not 'title' in request.json:
        abort(400)
    order = {
        'id': orders[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    orders.append(order)
    return jsonify({'order': order}), 201


"""
The PUT method, which we will use to update the status of an order
"""
@app.route('/food/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = filter(lambda o: o['id'] == order_id, orders)
    if len(order) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    order[0]['title'] = request.json.get('title', order[0]['title'])
    order[0]['description'] = request.json.get('description', order[0]['description'])
    order[0]['done'] = request.json.get('done', order[0]['done'])
    return jsonify({'order': make_public_order(order[0])})


"""
The DELETE method, which we will use to delete an order
"""
@app.route('/food/api/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = filter(lambda o: o['id'] == order_id, orders)
    if len(order) == 0:
        abort(404)
    orders.remove(order[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug = True)
	

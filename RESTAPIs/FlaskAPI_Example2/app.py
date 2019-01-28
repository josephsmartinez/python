from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'secret_key'

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
  # Class variables
  parser = reqparse.RequestParser()
  parser.add_argument('price',
    type=float,
    required=True,
    help="This field is required!"
    )

  # A JWT token is required
  @jwt_required()
  def get(self, name):
    # A more advanced options
    # item = next(filter(lamba x:x['name'] == name, items), None)
    for item in items:
      if item['name'] == name:
        return item
    # Return using ternary conditional
    #return {'item: item'}, 200 if item else 404
    return {'item': 'null'}, 404
  
  def post(self, name):
    # If an item is found and the item is not none
    if next(filter(lambda x: x['name'] == name, items), None):
      return {'message': "An item with name '{}' already exists.".format(name)}, 400

    data = Item.parser.parse_args()
    item = {'name': name, 'price':data['price']}
    items.append(item)
    return item, 201

  def delete(self, name):
    global items
    items = list(filter(lambda x: x['name'] != name, items))
    return {'message' : 'Item deleted'}

  @jwt_required()
  def put(self, name):
    data = Item.parser.parse_args()
    #data = request.get_json()
    item = next(filter(lambda x: x['name'] == name, items), None)
    if item is None:
      item = {'name': name, 'price': data['price']}
      items.append(item)
    else:
     item.update(data)
    return item
    
    

class ItemList(Resource):
  def get(self):
    if len(items) <= 0:
      return  {'items': 'null'}, 404
    return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True, port=5000)

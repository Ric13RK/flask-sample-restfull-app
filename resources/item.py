from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel


class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.in_json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {
                'message': f"An item with name '{name}' already exists."
            }, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.in_json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()
        return item.in_json()


class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        return {'items': [item.in_json() for item in ItemModel.query.all()]}
